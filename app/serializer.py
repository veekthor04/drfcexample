from django.contrib.auth import get_user_model
from rest_framework import serializers, validators
from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'
        depth = 2
    #   lookup_field = "user_id"
    
    
class AnonymousCarSerializer(serializers.ModelSerializer):
    """CarSerializer for an Anonymous user that excludes price"""
    class Meta:
        model = CarModel
        exclude = ['price',]
        depth = 2
