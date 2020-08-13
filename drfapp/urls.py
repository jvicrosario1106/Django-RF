from django.urls import path
from . import views
from .views import CreateApi,UpdateApi,DeleteApi

urlpatterns = [

    path("apiget/<str:pk>/",views.apiget, name="apiget"),
    path("apiall/",views.apiall, name="apiall"),
    path("apicreate/",CreateApi.as_view(), name="apicreate"),
    path("apiupdate/<str:pk>/",UpdateApi.as_view(), name="apiupdate"),
    path("apidelete/<str:pk>/",DeleteApi.as_view(), name="apidelete"),

]