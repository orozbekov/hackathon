from dataclasses import field
from rest_framework import serializers
from rest_framework.response import Response

from apps.my_app.admin import AnswerAdmin

from .models import Category, Quizzes, Question, Answer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "name",
        ]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["question", "answer_text", "is_right"]


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = [
            "title",
            "answer",
        ]


class QuestionSerializerWithoutRight(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question', 'answer_text']


class QuizSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    question = QuestionSerializer(many=True, read_only=True)
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Quizzes
        fields = ["title", "category_name", "question", "answer",]

    def get_category_name(self, instance):
        return instance.category.name
