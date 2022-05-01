from django.contrib import admin
from . import models


@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['name']
=======
    list_display = [
        "name",
    ]
>>>>>>> 4003f54b8e47af08f0e553e4696ec391de47d460


@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['id', 'title']
=======
    list_display = [
        "id",
        "title",
    ]
>>>>>>> 4003f54b8e47af08f0e553e4696ec391de47d460


class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
<<<<<<< HEAD
    fields = ['answer_text', 'is_right']
=======
    fields = ["answer_text", "is_right"]
>>>>>>> 4003f54b8e47af08f0e553e4696ec391de47d460


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    fields = ['title']
    list_display = ['title', 'quiz', 'date_updated']
    inlines = [AnswerInlineModel, ]
=======
    fields = [
        "title",
        "quiz",
    ]
    list_display = ["title", "quiz", "date_updated"]
    inlines = [
        AnswerInlineModel,
    ]
>>>>>>> 4003f54b8e47af08f0e553e4696ec391de47d460


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['answer_text', 'is_right', 'question']

=======
    list_display = ["answer_text", "is_right", "question"]
>>>>>>> 4003f54b8e47af08f0e553e4696ec391de47d460
