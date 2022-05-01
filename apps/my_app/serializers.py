from dataclasses import fields
from rest_framework import serializers

from apps.my_app.models import News, ResultTests, Test


class TestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Test
        fields = ('id', 'question', 'text', 'answer')

    
    
class TestResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResultTests
        fields = ('id' , 'test', 'user', 'result')