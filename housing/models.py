from django.db import models


class Housing_planning(models.Model):

    user = models.ForeignKey('registration.User_data', on_delete=models.CASCADE)
    type_animal = models.ForeignKey('alert.Type_animal', on_delete=models.CASCADE)
    number = models.IntegerField() 
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.user

    class Meta:

        verbose_name = "Housing planning"
        verbose_name_plural = "Planning des hébergements"
        ordering = ["user"]

class Animal(models.Model):

    name = models.CharField(max_length=100)
    type_animal = models.ForeignKey('alert.Type_animal', on_delete=models.CASCADE)
    gender = models.ForeignKey('alert.Gender', on_delete=models.CASCADE)
    color = models.ForeignKey('alert.Color', on_delete=models.CASCADE)
    commentary = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Animal"
        verbose_name_plural = "Animal"
        ordering = ["name"]

class Housing_animal(models.Model):

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    housing_planning = models.ForeignKey(Housing_planning, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.animal

    class Meta:

        verbose_name = "Housing animal"
        verbose_name_plural = "Housing animal"
        ordering = ["animal"]