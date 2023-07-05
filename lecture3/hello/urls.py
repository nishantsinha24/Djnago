from django.urls import path

from . import views


urlpatterns = [
    path("", views.index , name="index"),
    path("mohan", views.mohan , name="mohan"),
    path("sohan", views.sohan , name=""),
    path("<str:name>" , views.greet , name="greet")
]
