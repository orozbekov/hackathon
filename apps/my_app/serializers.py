from rest_framework import serializers
from rest_framework.response import Response

from .models import Category, Quizzes, Question, Answer


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['name', ]


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title']


class QuizSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    question = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quizzes
        fields = ['title', 'category_name', 'question']

    def get_category_name(self, instance):
        return instance.category.name


