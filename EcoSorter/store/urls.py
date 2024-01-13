from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView

urlpatterns = [
    path('',views.home, name="home"),
    path('store/',views.store, name="store"),
    path('map/',views.map, name="map"),
    path('login/',views.login_user, name="login"),
    path('logout/',views.logout_user, name="logout"),
    path('register/',views.register_user, name="register"),
    path('profile/',views.profile, name="profile"),
    path('product/<int:pk>',views.product, name="product"),
    path('category/<str:foo>',views.category, name="category"),
    path('password/',PasswordsChangeView.as_view(template_name="changepass.html"), name = "password"),
    # path('password/',auth_views.PasswordChangeView.as_view(template_name="changepass.html")),

]
