from django.contrib import admin

from apps.my_app.models import Test, Answer, Question, Result


class QuestionsInline(admin.TabularInline):
    model = Answer


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class BookAdmin(admin.ModelAdmin):
    inlines = [QuestionsInline]


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("ProfileId", "DateTime", "UserName", "Rating")

    def has_add_permission(self, request):
        return False


