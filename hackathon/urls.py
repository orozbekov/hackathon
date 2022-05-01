from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.my_app.views import Quiz, QuizQuestion, RandomQuestion

schema_view = get_schema_view(
    openapi.Info(
        title="Wildberies API",
        default_version="v1",
        description="RESTful app for provide API for mobile & web-front applications. ",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    # regex
<<<<<<< HEAD
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),

#     path('api/v1/news/', NewsView.as_view()),
#     path('api/v1/users/', CustomUserView.as_view()),
#     path('api/v1/test', TestView.as_view()),
    path('api/v1/quiz', Quiz.as_view(), name='quiz'),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='random' ),
    path('q/<str:topic>/', QuizQuestion.as_view(), name='questions' ),
=======
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    #     path('api/v1/news/', NewsView.as_view()),
    #     path('api/v1/users/', CustomUserView.as_view()),
    #     path('api/v1/test', TestView.as_view()),
    path("", Quiz.as_view(), name="quiz"),
    path("r/<str:topic>/", RandomQuestion.as_view(), name="random"),
    path("q/<str:topic>/", QuizQuestion.as_view(), name="questions"),
>>>>>>> 4003f54b8e47af08f0e553e4696ec391de47d460
]
