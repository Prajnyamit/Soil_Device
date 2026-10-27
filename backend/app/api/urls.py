from django.urls import path
from .auth import RegisterApiView,LoginApiView,ProfileAPIView
from .soil import SoilSampleApiView


urlpatterns =[
    path("auth/register",RegisterApiView.as_view(),name="register"),
    path("auth/profile",ProfileAPIView.as_view(),name="profile"),
    path ("auth/login",LoginApiView.as_view(),name="login"),
    path("soil/create_sample",SoilSampleApiView.as_view(),name="soil-create")
]

