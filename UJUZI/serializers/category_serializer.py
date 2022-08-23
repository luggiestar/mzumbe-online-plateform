from rest_framework import serializers
from ..models import Category

class CategorySerializer(serializers.ModelSerializer):
    icon_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Category
        fields = ('name', 'icon_url')

    def get_image_url(self, obj):
        icon_url = obj.icon.url
        return icon_url