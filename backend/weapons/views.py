from rest_framework import viewsets
from .models import Weapon, Object, PowerUp
from .serializers import WeaponSerializer, ObjectSerializer, PowerUpSerializer

class WeaponViewSet(viewsets.ModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer

class PowerUpViewSet(viewsets.ModelViewSet):
    queryset = PowerUp.objects.all()
    serializer_class = PowerUpSerializer
