from django.db import models

class Sudoku(models.Model):
    completed = models.BooleanField()