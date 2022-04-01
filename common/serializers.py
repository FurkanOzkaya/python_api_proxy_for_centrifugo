
from rest_framework_simplejwt import serializers


class JWTTokenSerializer(serializers.TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['sub'] = str(user.id)
        return token


class JWTTokenRefreshSerializer(serializers.TokenRefreshSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['sub'] = str(user.id)
        return token
