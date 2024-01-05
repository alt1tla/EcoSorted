from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.home, name="home"),
    path('store/',views.store, name="store"),
    path('map/',views.map, name="map"),
    path('login/',views.login_user, name="login"),
    path('logout/',views.logout_user, name="logout"),
    path('register/',views.register_user, name="register"),
    path('profile/',views.profile, name="profile"),
    path('product/<int:pk>',views.product, name="product"),
]
