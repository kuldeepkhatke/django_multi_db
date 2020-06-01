from django.shortcuts import render, redirect
from .forms import ProductForm, CreateUserForm
from .models import Product, UserProfile
from django.conf import settings
from django.contrib.auth.models import User

def dashboard(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = User()
                user.username = form.cleaned_data['username']
                user.set_password(form.cleaned_data['password1'])
                user.save()
                userprofile = UserProfile()
                userprofile.user = user
                userprofile.db = ','.join(form.cleaned_data['db'])
                userprofile.save()

                data = []
                users = User.objects.all().exclude(id=request.user.id)
                for user in users:
                    obj= {"user":user,"database":[]}
                    for db in settings.DATABASES.keys():
                        obj["database"].append({"name":db, "products":Product.objects.using(db).filter(user=user.id)})
                    data.append(obj)
                form = CreateUserForm()

                
                return render(request, 'admin/adminpanel.html', {'form': form,'data':data, 'users':users})
        else:
            data = []
            users = User.objects.all().exclude(id=request.user.id)
            for user in users:
                obj= {"user":user,"database":[]}
                for db in settings.DATABASES.keys():
                    obj["database"].append({"name":db, "products":Product.objects.using(db).filter(user=user.id)})
                data.append(obj)
            form = CreateUserForm()
            return render(request, 'admin/adminpanel.html', {'form': form,'data':data})

    if request.method == 'POST':
        userprofile = UserProfile.objects.get(user=request.user)
        form = ProductForm(userprofile,request.POST)
        
        if form.is_valid():
            Product.objects.using(str(form.cleaned_data['db'])).create(name=str(form.cleaned_data['name']), user=request.user.id)
            data = []
            for db in settings.DATABASES.keys():
                data.append({"db":db, "products":Product.objects.using(db).filter(user=request.user.id)})
            userprofile = UserProfile.objects.get(user=request.user)
            form = ProductForm(userprofile) 
        return render(request, 'dashboard/dashboard.html', {'form': form,'data':data})
    else:
        data = []
        for db in settings.DATABASES.keys():
            data.append({"db":db, "products":Product.objects.using(db).filter(user=request.user.id)})
        
        userprofile = UserProfile.objects.get(user=request.user)
        form = ProductForm(userprofile) 

        return render(request, 'dashboard/dashboard.html', {'form': form,'data':data})

def delete_user(request,pk):
    User.objects.get(id=pk).delete()
    for db in settings.DATABASES.keys():
        Product.objects.using(db).filter(user=pk).delete()
    return redirect('/accounts/profile/')