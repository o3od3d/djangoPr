from datetime import timezone

from django.db import models
from rest_framework.settings import api_settings


class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    board_title = models.CharField(max_length=200)
    board_contents = models.TextField()
    board_writer = models.CharField(max_length=200)
    board_date = models.DateTimeField(auto_now_add=True)

class Food(models.Model):
    food_name = models.CharField(max_length=100)
    food_recodeDate = models.DateTimeField(auto_now_add=True)
    food_expirationDate = models.DateTimeField(default=timezone)
    food_info = models.IntegerField()
    food_remainDate = models.DateTimeField(default=timezone)
    food_img = models.ImageField()

class User(models.Model):
    user_email = models.CharField(max_length=50)
    user_name = models.CharField(max_length=32)
    user_profile = models.ImageField()
    user_rating = models.IntegerField()

class Basket(models.Model):
    basket_contents = models.TextField()
    basket_reservationTime = models.TimeField()
    basket_info = models.IntegerField()

class Calendar(models.Model):
    calendar_date = models.DateTimeField()
    food_name = models.CharField(max_length=100)
    food_expirationDate = models.DateTimeField()

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
    comment_contents = models.TextField()
    comment_writer = models.CharField(max_length=200)
    comment_date = models.DateTimeField(auto_now_add=True)