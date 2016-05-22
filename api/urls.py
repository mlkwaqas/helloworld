from django.conf.urls import url, include
from rest_framework import routers
from api.views import NameViewSet

router = routers.DefaultRouter()
router.register(r'names', NameViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

