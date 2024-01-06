from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    dob = models.DateField()

    def __str__(self):
        return f"{self.name}"


class Pair(models.Model):
    cats = models.ManyToManyField(Cat)
    listing = models.URLField()

    def __str__(self):
        cat_list = []
        for cat in self.cats.all():
            cat_list.append(cat)
        return f"{cat_list[0]} and {cat_list[1]} are a bonded pair."
