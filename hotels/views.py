from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import *
from .models import *
# Create your views here.

class CategoryAPIView(APIView):
    def get(self, request):
        categories = CategoryModel.objects.all()
        serializer = CategoryModelSerializer(categories, many = True)
        return Response(serializer.data)

class HotelsAPIView(APIView):
    def get(self, request):
        hotels = Hotels.objects.all()
        serializer = HotelsModelSerializer(hotels, many = True)
        return Response(serializer.data)