from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response

from .models import Transaction
from .serializers import TransactionSerializer


class TransactionAPIView(generics.ListAPIView):
    def get(self, request):
        t = Transaction.objects.all()
        return Response({'posts': TransactionSerializer(t, many=True).data})

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})