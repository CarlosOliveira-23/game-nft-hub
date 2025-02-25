from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from nft.services import UserService
from nft.exceptions import UserAlreadyExistsException
from nft.handlers import ResponseHandler

User = get_user_model()


class RegisterSerializer(ModelSerializer):
    """ Serializer for creating users """

    class Meta:
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        """ Registra um novo usuário e retorna os tokens JWT """
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user_data = UserService.create_user(
                username=serializer.validated_data["username"],
                password=serializer.validated_data["password"],
            )

            return ResponseHandler.success(
                data={
                    "refresh": user_data["refresh"],
                    "access": user_data["access"],
                },
                message="User registered successfully",
                status_code=status.HTTP_201_CREATED
            )

        except UserAlreadyExistsException as e:
            return ResponseHandler.error(str(e), status.HTTP_400_BAD_REQUEST)

        except ValidationError as e:
            return ResponseHandler.error(str(e), status.HTTP_400_BAD_REQUEST)
