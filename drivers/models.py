from django.db import models
from cars_of_facts.models import Car



class Driver(models.Model):

    full_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="drivers/")
    birth_date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    experience = models.PositiveIntegerField()

    LICENSE_CHOICES = (
        ('Да', 'Да'),
        ('Нет', 'Нет'),
    )
    license = models.CharField(max_length=10, choices=LICENSE_CHOICES)

    def __str__(self):
        return self.full_name