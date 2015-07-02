from django.forms import widgets
from rest_framework import serializers
from gameapi.models import World

class WorldSerializer(serializers.ModelSerializer):
  class Meta:
    model = World
    fields = ('id', 'created', 'title')
