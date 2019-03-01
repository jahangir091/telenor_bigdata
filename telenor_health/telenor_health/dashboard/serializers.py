from django.contrib.auth.models import User, Group
from models import FactTable
from rest_framework import serializers


class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactTable
        fields = ('title', 'date_created', 'date_updated')

