
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from common.decarators import validator
from serializers.request_serializers import UserAvatarParameterSerializer, UserModelSerializer
from drf_yasg.utils import swagger_auto_schema
from common.common_funtions import generate_200_base_response
from rest_framework.parsers import MultiPartParser, FormParser
from common.decarators import get_user


RESPONSE = generate_200_base_response()


@swagger_auto_schema(tags=['User'], operation_description="Change User Avatar", method="POST", request_body=UserAvatarParameterSerializer, responses=RESPONSE, USE_SESSION_AUTH=False)
@api_view(["POST"])
@validator("body", UserAvatarParameterSerializer)
@parser_classes([MultiPartParser, FormParser])
@get_user()
def change_avatar(request, serializer, user):
    if serializer.data:
        user_serializer = UserModelSerializer(
            user, data=request.data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save(avatar=request.data.get("avatar"))
            return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)
