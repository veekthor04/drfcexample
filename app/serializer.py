from dataclasses import fields
from django.contrib.auth import get_user_model
from rest_framework import serializers, validators

from app.models import CarModel, Engine


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'
        depth = 2
    #   lookup_field = "user_id"
    

class AnonymousEngineSerializer(serializers.ModelSerializer):
    """EngineSerializer for an Anonymous user that excludes price"""
    class Meta:
        model = Engine
        exclude = ['maker',]


class AnonymousCarSerializer(serializers.ModelSerializer):
    """CarSerializer for an Anonymous user that excludes price and engine__maker"""
    engine = AnonymousEngineSerializer()
    
    class Meta:
        model = CarModel
        fields = ['id', 'car_name', 'engine']
