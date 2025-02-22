from rest_framework import serializers
from nft.models import NFT


class NFTSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFT
        fields = '__all__'
        