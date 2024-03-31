from django.db import models

# Create your models here.
Choices = {
    ('For my team',"For my team"),
    ('For my client','For my client'),
    ('other','other')
}

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    reason = models.EmailField(max_length=100,choices=Choices)
    mssg = models.TextField()
    def __str__(self):
        return self.name
    
class Zoom(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateField()
    time = models.CharField(max_length=1000)
    def __str__(self):
        return self.name
    