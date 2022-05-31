from django.db import models


class Industry(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    foundation_date = models.DateField()

    def __str__(self):
        return self.name


class Franchise(models.Model):
    name = models.CharField(max_length=50)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    release_date = models.DateField()
    price = models.IntegerField()
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE)
