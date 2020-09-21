from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BoardSerializer, FoodSerializer
from .models import Board, Food


class BoardViewset(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class FoodViewset(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


