from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'phone', 'first_name', 'last_name')


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ("email", "password", 'phone')

    # validate email and phone number
    def validate(self, attrs):
        email_exist = User.objects.filter(email=attrs['email']).exists()
        phone_exist = User.objects.filter(email=attrs['phone']).exists()
        if email_exist:
            raise ValidationError("Email already taken")

        if phone_exist:
            raise ValidationError("Phone number already taken")

        return super().validate(attrs)

    # hash user password and create token for new user
    def create(self, validated_data):

        password = validated_data.pop('password')

        user = super().create(validated_data)

        user.set_password(password)

        user.save()

        Token.objects.create(user=user)

        return user


