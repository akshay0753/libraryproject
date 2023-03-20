from django.db import models

# Create your models here.

class Common(models.Model):
    def __str__(self):
        return f"{self.id}------{self.name}"
    class Meta:
        abstract = True
    
class Book(Common):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    qty = models.IntegerField()
    is_published = models.BooleanField(default = 0)
    is_available = models.BooleanField(default=1)
    class Meta:
        db_table = "book"
        
        
        
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
    def save(self,commit=True):
        user = super(NewUserForm,self).save(commit=False)
        if commit:
            user.save()
        return user