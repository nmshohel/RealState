from django.shortcuts import render

# Create your views here.
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from .serializers import ContactSerializer
from .models import Contact

class ContactAPIView(APIView):
    def get(self, request, format=None):
        contact=Contact.objects.all()
        serializer=ContactSerializer(contact, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
