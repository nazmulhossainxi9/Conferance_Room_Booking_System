from django.db import models

# Create your models here.

class Classroom(models.Model): 
    title = models.CharField(max_length=100)
    booked_by = models.CharField(max_length=100, default="not specified")
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.title

class BdOSN(models.Model): 
    title = models.CharField(max_length=100)
    booked_by = models.CharField(max_length=100, default="not specified")
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.title

class MasLAB(models.Model): 
    title = models.CharField(max_length=100)
    booked_by = models.CharField(max_length=100, default="not specified")
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.title