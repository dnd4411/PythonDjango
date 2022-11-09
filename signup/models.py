from django.db import models
from django.contrib.auth.models import User

class userotp(models.Model):
    user_otp=models.ForeignKey(User, on_delete=models.CASCADE)
    time_st=models.DateField(auto_now=True)
    otp=models.SmallIntegerField()
