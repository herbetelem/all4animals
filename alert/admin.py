from django.contrib import admin
from .models import Type_animal, Gender, Type_alert, Alert_user, Color


# Register your models here.

admin.site.register(Type_animal)
admin.site.register(Gender)
admin.site.register(Type_alert)
admin.site.register(Alert_user)
admin.site.register(Color)