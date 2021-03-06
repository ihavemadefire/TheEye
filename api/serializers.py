from django.db.models.base import Model
from rest_framework import fields, serializers
from .models import Event
"""Serializers"""


class EventSerializer(serializers.ModelSerializer):
    """Class for serializing events"""
    class Meta:
        model = Event
        fields = ['session_id', 'category', 'name', 'data', 'timestamp']