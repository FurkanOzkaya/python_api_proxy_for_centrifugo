from rest_framework_simplejwt import views
from common.serializers import JWTTokenSerializer, JWTTokenRefreshSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class JWTTokenObtainPairView(views.TokenObtainPairView):
    serializer_class = JWTTokenSerializer


class JWTTokenRefreshView(views.TokenRefreshView):
    serializer_class = JWTTokenRefreshSerializer


# refresh is not work check again it could be send normal access and refresh token and there arrange that data if succes
@api_view(['POST'])
def refresh_token_ws(request):
    """
    Successful Response ==> {"result": {"user": "56"}}
    """
    user = request.data.get("user")
    response = {
        "status": 200, "data": {"token": JWTTokenRefreshSerializer.get_token(user)}
    }

    return Response(response, status=status.HTTP_200_OK)
