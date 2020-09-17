from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BoardSerializer
from .models import Board

class BoardViewset(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
# Create your views here.
