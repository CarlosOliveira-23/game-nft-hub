from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserService:
    """ Class of Service for user-related operations """

    @staticmethod
    def create_user(username: str, password: str):
        """ Creates a user and returns the access token """
        user = User.objects.create_user(username=username, password=password)
        refresh = RefreshToken.for_user(user)
        return {
            "user": user,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    @staticmethod
    def get_user_by_username(username: str):
        """ Search for a user by username """
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    @staticmethod
    def delete_user(user_id: int):
        """ Remove a user by ID """
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return True
        except User.DoesNotExist:
            return False
