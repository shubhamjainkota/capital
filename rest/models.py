from django.db import models

# Create your models here.

class employees(models.Model):

    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    emp_id = models.IntegerField(default=0000,primary_key=True)

    def __str__(self):
        return str(self.emp_id)

