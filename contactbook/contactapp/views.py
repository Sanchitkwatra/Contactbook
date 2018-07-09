from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters 
# Create your views here.
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from . import models
from . import serializers
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.authtoken.models import Token

@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})

@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data={'sample_data':123}
    return Response(data,status=HTTP_200_OK)

class ContactList(generics.ListCreateAPIView):
    queryset=models.Contact.objects.all()
    serializer_class=serializers.ContactSerializer
    filter_backends = (filters.SearchFilter,)
    filter_fields=('email','first_name','last_name')
    search_fields=('email','first_name','last_name')

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Contact.objects.all()
    serializer_class=serializers.ContactSerializer
    filter_fields=('email','first_name','last_name')
    search_fields=('email','first_name','last_name')