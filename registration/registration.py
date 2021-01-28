from django.forms import ModelForm
from .models import User_data
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        #Préciser a Django le model choisit
        model =  User_data
        # Préciser les champs a récupérer 
        fields = ["street", "postal_code"]

class UserDjango(ModelForm):
    class Meta:
        #Préciser a Django le model choisit
        model =  User
        # Préciser les champs a récupérer 
        fields = ["username", "first_name", "last_name", "password", "email"]