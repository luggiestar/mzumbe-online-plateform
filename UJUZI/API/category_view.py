from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..models import Category
from ..serializers import CategorySerializer


class CategoryListApi(APIView):
    """api for category"""
    serializer_class = CategorySerializer

    def get(self, request: Request):
        category = Category.objects.all()
        serializer = self.serializer_class(category, many=True)

        response = {
            "msg": "Data found",
            "data": serializer.data
        }

        return Response(response, status=status.HTTP_200_OK)
