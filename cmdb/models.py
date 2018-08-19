from django.db import models

# Create your models here.

class UserInfo(models.Model):

    user = models.CharField(max_length=23)
    pwd = models.CharField(max_length=23)

    def __str__(self):
        return self.user



