"""
URL 분리를 통해 프로젝트 구조를 정리하고,
각 앱이 독립적으로 동작할 수 있도록 유지 보수성을 높일 수 있다.
include('pybo.urls') 로
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
]