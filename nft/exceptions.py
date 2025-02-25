from rest_framework.exceptions import APIException


class UserAlreadyExistsException(APIException):
    """ Exceção para quando um usuário já existe """
    status_code = 400
    default_detail = "A user with this username already exists."
    default_code = "user_already_exists"
