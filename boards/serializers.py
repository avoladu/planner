from rest_framework import serializers
from .models import *

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"


class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = [
            "id",
            "title"
        ]
