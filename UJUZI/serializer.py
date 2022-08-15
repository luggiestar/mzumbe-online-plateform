from rest_framework import serializers
from online.UJUZI.models import User


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
