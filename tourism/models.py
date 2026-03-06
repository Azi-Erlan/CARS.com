from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tour(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


# 1 к 1
class Booking(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    booking_date = models.DateField()

    def __str__(self):
        return f"{self.person} - {self.tour}"


# 1 ко многим
class Review(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.author} - {self.tour}"