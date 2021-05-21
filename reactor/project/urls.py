from django.urls import path

from reactor.channels import ReactorConsumer

from todo import views

urlpatterns = [path("", views.index)]

websocket_urlpatterns = [
    path("__reactor__", ReactorConsumer),
]
