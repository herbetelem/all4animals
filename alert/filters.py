import django_filters
from .models import Alert_user

class Alert_user_filter(django_filters.FilterSet):
    class Meta :
        model = Alert_user
        fields = ["type_animal", "color", "gender"]
