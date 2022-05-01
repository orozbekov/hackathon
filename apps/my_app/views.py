from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.my_app.models import News
from apps.my_app.serializers import NewsSerializer


class Mixin(APIView):
    model_name = None
    serializer_name = None

    def get(self, request):
        model = self.model_name.objects.all()
        srz = self.serializer_name(model, many=True)
        return Response(srz.data)


class NewsView(Mixin):
    model_name = News
    serializer_name = NewsSerializer

    def post(self, request):
        request_body = request.data
        new_product = self.model_name.objects.create()
        srz = self.serializer_name(new_product, many=False)
        return Response(srz.data, status=status.HTTP_201_CREATED)