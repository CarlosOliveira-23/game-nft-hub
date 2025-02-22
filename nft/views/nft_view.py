from rest_framework import viewsets
from nft.models import NFT
from nft.serializers.nft_serializer import NFTSerializer


class NFTViewSet(viewsets.ModelViewSet):
    queryset = NFT.objects.all()
    serializer_class = NFTSerializer
