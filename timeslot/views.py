from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializers
from .models import Register


# Create your views here.


@api_view(['GET'])
def RegisterList(request):
    datas = Register.objects.all()
    serializer = RegisterSerializers(datas, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def User_Register(request):
    serializer = RegisterSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
