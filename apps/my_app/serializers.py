from dataclasses import fields
from rest_framework import serializers

from apps.my_app.models import  Profile, Question, ResultTests, Test


class TestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Test
        fields = ('id', 'question', 'text', 'answer')

    
    
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
    pass

class ResultSerializer(serializers.ModelSerializer):
    pass