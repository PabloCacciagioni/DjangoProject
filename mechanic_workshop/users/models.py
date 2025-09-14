from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=20, blank=True, null=True)
    homeAdress = models.CharField(max_length=200, blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.name} {self.lastname}'
