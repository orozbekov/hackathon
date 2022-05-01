from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quizzes(models.Model):

    title = models.CharField(max_length=255, default="New Quiz", verbose_name="Quiz Title")
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.title


class Updated(models.Model):

    date_updated = models.DateTimeField(verbose_name="Last Updated", auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):

    quiz = models.ForeignKey(Quizzes, related_name="question", on_delete=models.DO_NOTHING)
    technique = models.IntegerField(default=0, verbose_name="Type of Question")
    title = models.CharField(max_length=255, verbose_name="Title")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    is_active = models.BooleanField(default=False, verbose_name="Active Status")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.title


class Answer(Updated):

    question = models.ForeignKey(Question, related_name="answer", on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name="Answer Text")
    is_right = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return self.answer_text
