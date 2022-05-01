from django.db import models

from apps.users.models import CustomUser


class Category(models.Model):
    pass


class Test(models.Model):
    question = models.CharField('Текст вопроса', max_length=150)
    answer = models.BooleanField('Ответы', default=False) # Да/Нет (тут храним правильный ответ)


class ResultTests(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    result = models.BooleanField('Результат', default=False) # true если ответ был верный


class Profile(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название теста')
    work_time = models.IntegerField(verbose_name='Время выполнения (мин)')
    questions_count = models.IntegerField(verbose_name='Количество вопросов')
    statisfactorily = models.IntegerField(verbose_name='Удовлетворительно')
    good = models.IntegerField(verbose_name='Хорошо')
    perfect = models.IntegerField(verbose_name='Отлично')

    class Meta:
        verbose_name = 'Тесты'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.name


class Question(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Тест')
    text = models.TextField(verbose_name='Текст вопроса')
    weight = models.FloatField(default=1, verbose_name='Вес')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    is_right = models.BooleanField()

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.text


class Result(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Тест')
    username = models.CharField(max_length=300, verbose_name="ФИО")
    datetime = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Время завершения")
    rating = models.FloatField(verbose_name="Проценты")

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

