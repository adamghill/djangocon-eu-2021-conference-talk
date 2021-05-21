from django.urls import path, include
from rest_framework import routers

from .api.views import index_view, TodoViewSet

router = routers.DefaultRouter()
router.register("todos", TodoViewSet)

urlpatterns = [
    path("", index_view, name="index"),
    path("api/", include(router.urls)),
]
