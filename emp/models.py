from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=20)
    emp_id=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=50)

    def __str__(self):
        return self.name