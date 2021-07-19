from django.db.models import fields
from rest_framework import serializers
from .models import *

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'
