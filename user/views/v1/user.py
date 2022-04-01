
from serializers.request_serializers import UserUpdateParameterSerializer, UserModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from common.decarators import validator
from drf_yasg.utils import swagger_auto_schema
from serializers.response_serialziers import UserResponseSerializer
from rest_framework.permissions import IsAuthenticated
from common.decarators import get_user
from common.common_funtions import generate_200_model_response, generate_201_base_response, generate_200_base_response

RESPONSE_GET = generate_200_model_response(UserResponseSerializer)

RESPONSE_POST = generate_201_base_response()

RESPONSE_PATCH = generate_200_base_response()


class User(APIView):
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['User'], operation_description="Get User Information",  responses=RESPONSE_GET)
    @get_user()
    def get(self, request, user):
        """
            Get User Informations
        """
        serializer = UserModelSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(tags=['User'], operation_description="Register Api", request_body=UserModelSerializer, responses=RESPONSE_POST, USE_SESSION_AUTH=False)
    @validator("body", UserModelSerializer)
    def post(self, request, serializer):
        """
        Register User 
        ---
        username, email, password required 
        """
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    @swagger_auto_schema(tags=['User'],  request_body=UserUpdateParameterSerializer, responses=RESPONSE_PATCH, USE_SESSION_AUTH=False)
    @validator("body", UserUpdateParameterSerializer)
    @get_user()
    def patch(self, request, serializer, user):
        """
            Update User Informations
        """
        if serializer.data:
            user_serializer = UserModelSerializer(
                user, data=serializer.data, partial=True)
            if user_serializer.is_valid():
                user_serializer.save(data=serializer.data)
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
