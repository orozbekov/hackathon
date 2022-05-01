from dataclasses import fields
from rest_framework import serializers

from apps.my_app.models import Answer, Profile, Question, Result, ResultTests, Test
from apps.my_app.models import ResultTests, Test


class TestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Test
        fields = ('id', 'question', 'answer')

    
class ResultTestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResultTests
        fields = ('id' , 'test', 'user', 'result')


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ('id','name', 'work_time', 'questions_count', 'statisfactorily', 'good', 'perfect')


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'profile_id', 'text', 'weight')


class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields = ('id', 'question_id', 'text', 'is_right')


class ResultSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Result
        fields = ('id', 'profile_id', 'username', 'datetime', 'rating')

