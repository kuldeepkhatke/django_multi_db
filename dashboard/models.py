from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    db = models.TextField()

    def __str__(self):
        return self.user.username

class Product(models.Model):
    name = models.CharField(max_length=100)
    user = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table="product"
