from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    # date = models.DateField()

    def __str__(self):
        return self.name



class Owner(models.Model):
    username = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    images = models.ImageField(upload_to='images')

    def __str__(self):
        return self.username


    # date = models.DateField()

class Finalowner(models.Model):
    username = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    images = models.ImageField(upload_to='images')

    def __str__(self):
        return self.username