from pyexpat import model

from rest_framework import generics
from rest_framework.response import Response
from .models import Quizzes, Question
from .serializers import QuizSerializer, QuestionSerializer
from rest_framework.views import APIView


class Mixin(APIView):
    model = None
    srz = None

    def get(self, request):
        model_name = self.model.objects.all()
        serializer_name = self.srz(model_name, many=True)
        return Response(serializer_name.data)


class Quiz(Mixin):
    model = Quizzes
    srz = QuizSerializer


# class RandomQuestion(APIView):
#     def get(self, request, format=None, **kwargs):
#         question = Question.objects.filter(quiz__title=kwargs["topic"]).order_by("?")[
#                    :1
#                    ]
#         serializer = RandomQuestionSerializer(question, many=True)
#         return Response(serializer.data)


# class QuizQuestion(Mixin):
#     model = Question
#     srz = QuestionSerializer

