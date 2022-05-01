from rest_framework import serializers
from .models import Category, Quizzes, Question, Answer


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = [
            'id','name'
        ]


class QuizSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer()

    class Meta:
        model = Quizzes
        fields = [
            'title', 'category'
        ]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'id','title','answer',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'id','quiz','title','answer',
        ]