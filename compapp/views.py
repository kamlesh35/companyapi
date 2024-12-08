from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import Agent, Campaign, CampaignResult
from .serializers import AgentSerializer, CampaignSerializer, CampaignResultSerializer

class AgentViewSet(ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class CampaignViewSet(ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class CampaignResultViewSet(ModelViewSet):
    queryset = CampaignResult.objects.all()
    serializer_class = CampaignResultSerializer
