from dataclasses import field
from pyexpat import model
from statistics import mode
from .models import AdminInfo, Links,  User
from rest_framework import serializers

class AdminInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminInfo
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class LinkSrializer(serializers.ModelSerializer):
    class Meta:
        model=Links
        fields='__all__'