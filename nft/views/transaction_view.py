from rest_framework import viewsets
from nft.models import Transaction
from nft.serializers.transaction_serializer import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
