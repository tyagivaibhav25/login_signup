from django.db import models



class user(models.Model):
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=20)

    def __str__(self):
        return self.username
