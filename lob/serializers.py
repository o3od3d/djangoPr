from .models import Board, Food, Basket, User, Calendar
from rest_framework import serializers


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('board_id','board_title', 'board_contents', 'board_writer', 'board_date')

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('food_name', 'food_recodeDate', 'food_expirationDate','food_info', 'food_remainDate', 'food_img')

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('basket_contents', 'basket_reservationTime', 'basket_info')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_email', 'user_name', 'user_profile', 'user_rating')

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ('calendar_date', 'food_name', 'food_expirationDate')