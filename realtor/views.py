from django.shortcuts import render

# Create your views here.
from .models import Agent
from .serializers import AgentSerializer
from rest_framework import permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView,RetrieveDestroyAPIView, RetrieveUpdateAPIView
class AgentListView(ListAPIView):
    permission_classes=(permissions.AllowAny,)
    queryset=Agent.objects.all()
    serializer_class=AgentSerializer
    pagination_class=None

class AgentDetailView(RetrieveAPIView):
    queryset=Agent.objects.all()
    serializer_class=AgentSerializer
    
class TopsellerListView(ListAPIView):
    permission_classes=(permissions.AllowAny,)
    queryset=Agent.objects.filter(top_seller=True)
    serializer_class=AgentSerializer
    pagination_class=None