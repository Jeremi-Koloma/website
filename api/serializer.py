# Cette classe pemettra de transformer des données des models en JSON pour accès en API
from django.contrib.auth.models import User
from rest_framework import serializers

# Transformation du model User en JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # le model User
        fields = '__all__'
