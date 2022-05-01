from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.my_app.models import Test, ResultTests, Profile, Question
from apps.my_app.serializers import QuestionSerializer, TestSerializer, ResultTestsSerializer, \
    ProfileSerializer
from apps.my_app.models import Test
from apps.my_app.serializers import TestSerializer

class Mixin(APIView):
    model_name = None
    serializer_name = None

    def get(self, request):
        model = self.model_name.objects.all()
        srz = self.serializer_name(model, many=True)
        return Response(srz.data)


class TestView(Mixin):
    model_name = Test
    serializer_name = TestSerializer

    # def post(self, request):
    #     request_body = request.data
    #     new_product = self.model_name.objects.create()
    #     srz = self.serializer_name(new_product, many=False)
    #     return Response(srz.data, status=status.HTTP_201_CREATED)

class ResultTestsView(Mixin):
     model_name = ResultTests
     serializer_name = ResultTestsSerializer


class ProfileView(Mixin):
     model_name = Profile
     serializer_name = ProfileSerializer



class QestionView(Mixin):
     model_name = Question
     serializer_name = QuestionSerializer