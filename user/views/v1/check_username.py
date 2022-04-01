
from user.models import UserModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from common.decarators import validator
from serializers.request_serializers import CheckUsernameParameterSerialzier
from drf_yasg.utils import swagger_auto_schema
from common.common_funtions import generate_200_base_response
# Create your views here.

RESPONSE = generate_200_base_response()


@swagger_auto_schema(tags=['User'], method="GET", query_serializer=CheckUsernameParameterSerialzier, responses=RESPONSE)
@api_view(["GET"])
@validator(validator=CheckUsernameParameterSerialzier)
def check_username(request, serializer):
    """
    Check if username is already in use or not  
    if  
        username available return: 200 
        except return: 400 
        error cases: 500
    """
    username = serializer.data.get("username")
    try:
        UserModel.objects.get(username=username)
    except UserModel.DoesNotExist:
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)
