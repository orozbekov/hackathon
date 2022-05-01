from django.contrib import admin

from apps.my_app.models import Test, Answer, Question, Result, ResultTests, Profile


class QuestionsInline(admin.TabularInline):
    model = Answer


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class BookAdmin(admin.ModelAdmin):
    inlines = [QuestionsInline]


@admin.register(ResultTests)
class ResultTestsAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    pass

    def has_add_permission(self, request):
        return False


