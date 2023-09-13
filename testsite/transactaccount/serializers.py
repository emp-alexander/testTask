from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Transaction


# class TransactionModel:
#     def __init__(self, summa):
#         self.summa = summa
class TransactionSerializer(serializers.Serializer):
    summa = serializers.DecimalField(max_digits=6, decimal_places=2)
    date = serializers.DateField(read_only=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

# def encode():
#     model = TransactionModel('11.01')
#     model_sr = TransactionSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)