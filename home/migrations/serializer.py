from rest_framework import serializers
from .models import *

class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title','description']