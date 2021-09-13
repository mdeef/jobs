from django.db import models
from django.db.models.enums import Choices

# Create your models here.



TYPE_J= (
        ('full time', 'full time'),
        ('part time', 'part time'),
       
    )
class job(models.Model):
    title =models.CharField(max_length=100)
    name =models.CharField(max_length=100)
    job_tyep= models.CharField(max_length=100, choices=TYPE_J)
    description= models.TextField(max_length=1000)
    published_at= models.DateTimeField(auto_now=True)
    vacancy = models.BigIntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    Image= models.ImageField(upload_to='jobs/')



    def __str__(self):
        return self.title

class category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

 