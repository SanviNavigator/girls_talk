from django.db import models

# Create your models here.

class User(models.Model):
    userid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=500)
    password=models.CharField(max_length=20)

    def register():
       self.save()


    def __str__(self):
        return self.name
