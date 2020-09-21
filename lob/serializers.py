from .models import Board, Food
from rest_framework import serializers


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('board_title', 'board_contents', 'board_writer', 'board_date')

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('food_name', 'food_recodeDate', 'food_expirationDate')
