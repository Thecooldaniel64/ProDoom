from rest_framework import serializers
from .models import Weapon, Object, PowerUp

class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = '__all__'

class PowerUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerUp
        fields = '__all__'
