from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location=settings.MEDIA_ROOT)

class Customers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    Select_Date = models.DateField(null=True,blank= True)  
    Select_Time = models.TimeField()  # Change to TimeField
    requestat = models.DateTimeField(auto_now_add=True)  # Corrected field name and changed to DateTimeField
    

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    primary_image = models.ImageField()

    def __str__(self):
        return self.title

class Picture(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ManyToManyField('Image', related_name='pictures')

    def __str__(self):
        return str(self.project.title)

class Image(models.Model):
    image = models.ImageField()
    def __str__(self):
        return str(self.image)


class ScheduleAppointment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name