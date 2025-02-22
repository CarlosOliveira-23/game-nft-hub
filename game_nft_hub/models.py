from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    pass


class NFT(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="nfts")
    contract_address = models.CharField(max_length=255)
    token_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):  # Corrigido aqui!
    nft = models.ForeignKey(NFT, on_delete=models.CASCADE, related_name="transactions")
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sales")
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="purchases")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction_hash = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"Transaction {self.transaction_hash} - {self.nft.name}"
