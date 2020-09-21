from django.db import models
class Board(models.Model):
    board_title = models.CharField(max_length=200)
    board_contents = models.TextField()
    board_writer = models.CharField(max_length=200)
    board_date = models.DateTimeField(auto_now_add=True)

class Food(models.Model):
    food_name = models.CharField(max_length=100)
    food_recodeDate = models.DateTimeField(auto_now_add=True)
    food_expirationDate = models.TextField()