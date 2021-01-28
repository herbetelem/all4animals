from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Type_animal(models.Model):

    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

    class Meta:

        verbose_name = "Type animal"
        verbose_name_plural = "Type d'animal"
        ordering = ["type"]


class Gender(models.Model):

    gender = models.CharField(max_length=100)
    
    def __str__(self):
        return self.gender

    class Meta:

        verbose_name = "Gender"
        verbose_name_plural = "Sexe de l'animal"
        ordering = ["gender"]

class Type_alert(models.Model):

    alert = models.CharField(max_length=100)

    def __str__(self):
        return self.alert

    class Meta:

        verbose_name = "Type Alert"
        verbose_name_plural = "Type d'alerte"
        ordering = ["alert"]

class Color(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Color"
        verbose_name_plural = "Couleurs"
        ordering = ["name"]


class Alert_user(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    type_alert = models.ForeignKey(Type_alert, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    type_animal = models.ForeignKey(Type_animal, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    email = models.EmailField(max_length=70)
    street = models.CharField(max_length=100)
    postal_code = models.IntegerField() 
    city = models.CharField(max_length=100)
    date = models.DateField(max_length=300)
    commentary = models.CharField(max_length=300)
    img = models.ImageField(upload_to='')

    def __str__(self):
        return self.type_animal.type

    class Meta:

        verbose_name = "Alert user"
        verbose_name_plural = "Les alertes utilisateurs"
        ordering = ["user"]