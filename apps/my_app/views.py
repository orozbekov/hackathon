from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.my_app.models import News
from apps.my_app.serializers import NewsSerializer


class NewsView(APIView):
    def get(self, request):
        news = News.objects.all()
        srz = NewsSerializer(news, many=True)
        return Response(srz.data)
