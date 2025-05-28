"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
장고의 urls.py 파일은 페이지 요청이 발생하면 가장 먼저 호출되는 파일로
URL과 뷰 함수를 연결하는 역할을 한다.
프로젝트 전반적인 URL을 관리하는 파일로,
앱별 URL 매핑은 여기에 포함되지 않는 것이 바람직하다.
따라서 pybo 앱 전용 매핑은 pybo.urls에 추가한다.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
]
