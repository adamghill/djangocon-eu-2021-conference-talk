from django.contrib import admin
from django.urls import path, include

from todo import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("unicorn/", include("django_unicorn.urls")),  # required for Unicorn
    path("", views.index),
]
