from rest_framework.serializers import ModelSerializer, Serializer, CharField
from user.models import UserModel


class UserResponseSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
