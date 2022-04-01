from common.database_helper import get_user_by_id
from functools import wraps
from rest_framework.response import Response
from rest_framework import status


def validator(type="query_string", validator=None):
    def inner_validator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            request = args[-1]
            if validator == None:
                print(
                    "Validator Decorator return - 400 - validator not sent to funtion")
                return Response(status=status.HTTP_400_BAD_REQUEST)
            if type == "query_string":
                serializer = validator(data=request.GET)
            elif type == "body":
                serializer = validator(data=request.data)
            else:
                print("Type is wrong")
            if serializer.is_valid():
                res = func(*args, **kwargs, serializer=serializer)
            else:
                print(
                    "Validator Decorator return - 400 - serializer is not valid: ", serializer.errors)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return res
        return wrapper
    return inner_validator


def get_user():
    def inner_validator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            request = args[-1]
            user = get_user_by_id(request.user.id)
            if user:
                res = func(*args, **kwargs, user=user)
                return res
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return wrapper
    return inner_validator
