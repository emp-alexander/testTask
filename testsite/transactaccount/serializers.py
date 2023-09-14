from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Transaction
        fields = "__all__"

