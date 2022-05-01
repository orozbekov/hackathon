from dataclasses import fields
from rest_framework import serializers

from apps.my_app.models import ResultTests, Test


class TestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Test
        fields = ('id', 'question', 'answer')


class ResultTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResultTests
        fields = ('id', 'test', 'user', 'result' )