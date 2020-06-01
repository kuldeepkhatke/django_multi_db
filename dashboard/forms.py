from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Product


DB_CHOICES =( 
    ("database1", "database1"), 
    ("database2", "database2"), 
    ("database3", "database3"), 
    ("database4", "database4"), 
    ("database5", "database5"), 
) 

class ProductForm(forms.Form):
    def __init__(self, userprofile, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['db'] = forms.ChoiceField(
            choices=[(db,db) for db in userprofile.db.split(',')]
        )
    name = forms.CharField(label='Product name', max_length=100)
    # db = forms.ChoiceField(label='Database')

class CreateUserForm(UserCreationForm):
    db = forms.MultipleChoiceField(label='Database', choices = DB_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'db', 'password1', 'password2', )