from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer


# Create your views here.

# une fonction pour retourner la liste des utilisateurs
@api_view(['GET'])
def get_users(request):
    user_list = User.objects.all()
    serializer = UserSerializer(user_list, many = True)
    return Response(serializer.data)
