from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('maps/', views.maps, name="maps"),
    path('store/', views.store, name="store"),
    path('profile/', views.profile, name="profile"),
]