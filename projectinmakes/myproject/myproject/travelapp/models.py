from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=350)
    img=models.ImageField(upload_to='pictures')
    desc=models.TextField()

    def __str__(self):
        return self.name

class person(models.Model):
    name = models.CharField(max_length=350)
    img = models.ImageField(upload_to='pictures')
    desc = models.TextField()

    def __str__(self):
        return self.name
