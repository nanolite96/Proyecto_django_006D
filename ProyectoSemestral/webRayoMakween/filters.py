from django.db.models import fields
import django_filters

from .models import Trabajos

class FiltroTrabajos(django_filters.FilterSet):
    class Meta:
        model = Trabajos
        fields = ["nombre","codigo"]