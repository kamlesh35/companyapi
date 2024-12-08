from rest_framework.routers import DefaultRouter
from .views import AgentViewSet, CampaignViewSet, CampaignResultViewSet

router = DefaultRouter()
router.register('agents', AgentViewSet)
router.register('campaigns', CampaignViewSet)
router.register('campaign-results', CampaignResultViewSet)

urlpatterns = router.urls
