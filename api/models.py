from django.db import models

# Create your models here.
class NameList(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.name
    