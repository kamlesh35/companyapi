from django.db import models

# Create your models here.

from django.db import models

# Agent Model
class Agent(models.Model):
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=100)
    voice_id = models.CharField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Campaign Model
class Campaign(models.Model):
    INBOUND = 'Inbound'
    OUTBOUND = 'Outbound'
    CAMPAIGN_TYPE_CHOICES = [(INBOUND, 'Inbound'), (OUTBOUND, 'Outbound')]

    RUNNING = 'Running'
    PAUSED = 'Paused'
    COMPLETED = 'Completed'
    CAMPAIGN_STATUS_CHOICES = [
        (RUNNING, 'Running'),
        (PAUSED, 'Paused'),
        (COMPLETED, 'Completed'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=CAMPAIGN_TYPE_CHOICES)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=CAMPAIGN_STATUS_CHOICES)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="campaigns")

    def __str__(self):
        return self.name

# CampaignResult Model
class CampaignResult(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="results")
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    cost = models.FloatField()
    outcome = models.CharField(max_length=255)
    call_duration = models.FloatField()
    recording = models.URLField()
    summary = models.TextField()
    transcription = models.TextField()

    def __str__(self):
        return self.name
