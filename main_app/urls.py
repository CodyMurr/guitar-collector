from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('guitars/<int:guitar_id>/', views.guitars_detail, name='detail'),
]