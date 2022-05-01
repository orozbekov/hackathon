from rest_framework import serializers

from apps.my_app.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'text', ]

