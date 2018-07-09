from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class Contact(models.Model):
    email=models.CharField(unique=True,null=False,max_length=100)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phonenum=models.IntegerField()
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    pincode=models.IntegerField()

    def __str__(self):
        return self.email


@receiver (post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)