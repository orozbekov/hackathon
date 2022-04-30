from django.contrib import admin

from apps.my_app.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


