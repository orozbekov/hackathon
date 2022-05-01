from rest_framework import serializers

from apps.users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """Вывод списка CustomUser"""

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'age', 'email']

        