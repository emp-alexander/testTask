from rest_framework import generics
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import Transaction
from .serializers import TransactionSerializer


class TransactionAPIList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, )


    def get_queryset(self):
        # Если текущий пользователь - админ, показываем все транзакции
        if self.request.user.is_staff:
            return Transaction.objects.all()
        # Фильтруем транзакции по текущему пользователю
        return Transaction.objects.filter(user=self.request.user)


class TransactionAPIUpdate(generics.UpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAdminUser,)

class TransactionAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAdminUser, )