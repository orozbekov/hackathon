from rest_framework import generics
from rest_framework.response import Response
from .models import Quizzes, Question
from .serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer
from rest_framework.views import APIView


class Quiz(APIView):
    def get(self, request):
        queryset = Quizzes.objects.all()
        serializer_class = QuizSerializer(queryset, many=True)
        return Response(serializer_class.data)


class RandomQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs["topic"]).order_by("?")[
            :1
        ]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):
    def get(self, request):
        quiz = Question.objects.all()
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)
