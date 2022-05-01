from django.db import models

from apps.users.models import CustomUser

class Category(models.Model):
    pass

class Test(models.Model):
    question = models.CharField('Текст вопроса', max_length=150)
    answer = models.BooleanField('Ответы', default=False)   # Да/Нет (тут храним правильный ответ)

class ResultTests(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    result = models.BooleanField('Результат', default=False) # true если ответ был верный