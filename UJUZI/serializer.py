from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import User, Category


class UserLoginSerializer(serializers.ModelSerializer):
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


class CategorySerializer(serializers.ModelSerializer):
    icon_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Category
        fields = ('name', 'icon_url')

    def get_image_url(self, obj):
        icon_url = obj.icon.url
        return icon_url
