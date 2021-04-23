from django.contrib import admin
from .models import *

class SudokuAdmin(admin.ModelAdmin):
    list_display = ('completed', )

admin.site.register(Sudoku)