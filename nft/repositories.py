from django.contrib.auth import get_user_model


User = get_user_model()


class UserRepository:
    """ Repositorio para operacoes relacionadas a usuarios """
    
    @staticmethod
    def get_user_by_username(username: str):
        """ Busca usuario pelo username """
        return User.objects.filter(username=username).first()
    
    @staticmethod
    def create_user(username: str, password: str):
        """ Cria um novo usuario """
        return User.objects.create_user(username=username, password=password)
