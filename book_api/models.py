from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    num_of_pages=models.IntegerField()
    public_date=models.DateField()
    quatity=models.IntegerField()

def __str__(self):
    return self.title 


# book/list