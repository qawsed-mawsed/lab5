from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.register_view, name='register'),  # URL для страницы регистрации
    path('main/', views.main, name='main'),
    # Добавь другие URL-маршруты, если необходимо
]
