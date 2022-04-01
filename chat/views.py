from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from common.decarators import get_user
from rest_framework.decorators import api_view
import logging
import time

# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name, token):
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'token': token
    })


@api_view(['POST'])
@get_user()
def connect(request, user):
    """
    Successful Response ==> {"result": {"user": "56"}}
    """
    logger.debug(request.data)
    response = {
        'result': {
            'user': str(user.id)
        }
    }
    return Response(response, status=status.HTTP_200_OK)


@api_view(['POST'])
def refresh(request):
    """
    Check  user still active or not
    request include ==> {
        "client":"9336a229-2400-4ebc-8c50-0a643d22e8a0",
        "transport":"websocket",
        "protocol": "json",
        "encoding":"json",
        "user":"56"
    }  

    Success Response ==>
    {"result": {"expire_at": 1565436268}}
    {"status": 200, "data": {"token": "JWT"}} 

    Disconenct Response ==>  Application must use numbers in the range 4000-4999 for custom disconnect codes
    {
        "disconnect": {
            "code": 4000,
            "reconnect": false,
            "reason": "custom disconnect"
            }
        }

    error Response ==>
    {
        "error": {
            "code": 1000,
            "message": "custom error"
            }
        }
    """
    logger.debug(request.body)
    current_time = time.time()
    expire_time = current_time + 300
    response = {
        'result': {"expire_at": expire_time}
    }
    return Response(response, status=status.HTTP_200_OK)


@api_view(['POST'])
def publish(request):
    """
    Write message to db. (cellery)
    Check Can user publish to that channel or not

    Success Response ==>
    {
        'result': {}
        }

    Disconenct Response ==>  Application must use numbers in the range 4000-4999 for custom disconnect codes
    {
        "disconnect": {
            "code": 4000,
            "reconnect": false,
            "reason": "custom disconnect"
            }
        }

    error Response ==>
    {
        "error": {
            "code": 1000,
            "message": "custom error"
            }
        }
    """
    logger.debug(request.body)
    print("afo publish")
    response = {
        'result': {}
    }
    return Response(response, status=status.HTTP_200_OK)


@api_view(['POST'])
def subscribe(request):
    """
    Can User listen that channel. private channels already handled by centrifugal

    Successful Message => {"result": {}}
    Disconenct Response ==>  Application must use numbers in the range 4000-4999 for custom disconnect codes
    {
        "disconnect": {
            "code": 4000,
            "reconnect": false,
            "reason": "custom disconnect"
            }
        }

    error Response ==>
    {
        "error": {
            "code": 1000,
            "message": "custom error"
            }
        }

    """
    logger.debug(request.body)
    logger.info("afo subscribe")
    response = {
        'result': {}
    }
    return Response(response, status=status.HTTP_200_OK)
