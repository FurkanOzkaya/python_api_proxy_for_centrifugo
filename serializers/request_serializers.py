from rest_framework.serializers import ModelSerializer, Serializer, CharField, ImageField
from user.models import UserModel

# TODO add special char validation


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        exclude_field = ["avatar"]
        extra_kwargs = {
            'password': {'write_only': True},
            'groups': {'write_only': True},
            'user_permissions': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class CheckUsernameParameterSerialzier(Serializer):
    username = CharField(max_length=200, help_text="Username of User")


class LoginUserParameterSerializer(Serializer):
    username = CharField(max_length=200, help_text="Username of User")
    password = CharField(max_length=200, help_text="Password of User")


class UserAvatarParameterSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["avatar"]


class UserUpdateParameterSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        exclude = ["avatar", "groups", "username", "password",
                   "user_permissions", "last_login", "is_superuser",
                   "is_staff", "is_active", "date_joined"]
