from django.db import models

class Technologies(models.Model):
    python=models.CharField(max_length=1000)
    java=models.CharField(max_length=1000)
    php=models.CharField(max_length=1000)
    React_js=models.CharField(max_length=1000)

    
class Job(Technologies):
    internship=models.CharField(max_length=1000)
    Placement=models.CharField(max_length=1000)
    Fresher=models.CharField(max_length=1000)
