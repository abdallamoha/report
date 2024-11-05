from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator, MaxValueValidator


# Create your models here.


class Trip(models.Model):
    city=models.CharField(max_length=50)
    models.CharField(max_length=50)
    start_date=models.DateField(blank=True, null=True)
    end_date=models.DateField(blank=True, null=True)
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='trips')

    def __str__(self):
        return self.city
class Note(models.Model):
    Excursion=(
        ("events","Events"),
        ("dining","Dining"),
        ("exprience","Exprience"),
        ("general","General"),
    )
    trip=models.ForeignKey(Trip,on_delete=models.CASCADE,related_name='notes')
    name=models.CharField(max_length=50)
    description=models.TextField()
    type=models.CharField(max_length=50,choices=Excursion)
    img=models.ImageField(upload_to="img/",blank=True)
    rating=models.PositiveIntegerField(default=1,validators=[MaxValueValidator(5)])

    def __str__(self):
        return f"{self.name} in {self.trip.city}"


