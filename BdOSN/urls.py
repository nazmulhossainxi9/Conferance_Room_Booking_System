from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("profile/signout/", views.signout, name="signout"),
    path("classroom", views.classroom,  name="classroom"),
    path("bdosn", views.bdosn, name="bdosn"),
    path("maslab", views.maslab, name="maslab")
]
