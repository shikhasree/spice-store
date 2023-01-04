from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

# Serializers for different Models using ModelSerializer


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['pk', 'title', 'category',
                  'description', 'price', 'discount_price', 'slug', 'image']


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username']


class OrderitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['ordered', 'item', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username']
