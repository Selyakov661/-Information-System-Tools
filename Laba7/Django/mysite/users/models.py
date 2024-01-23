from django.db import models

# Create your models here.
# создание модели данных класса Model
class SearchingUsers(models.Model):
    # модель имеет одно текстовое поле
    ByName = models.CharField(max_length=100)