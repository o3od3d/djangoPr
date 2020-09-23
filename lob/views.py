from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BoardSerializer, FoodSerializer, BasketSerializer, CalendarSerializer, UserSerializer
from .models import Board, Food, Basket, User, Calendar


class BoardViewset(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class FoodViewset(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BasketViewset(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

class CalendarViewset(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
