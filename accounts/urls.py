from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),

    path('profilee/', views.profile, name='profilee'),
    path('profile/<pk>/', views.Profile.as_view(), name='profile')
]
