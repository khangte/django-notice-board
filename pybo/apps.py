# 앱의 구성정보를 정의하는 파일이다.
# 파이보 프로젝트에서 이 파일을 수정할 일은 없다.
from django.apps import AppConfig


class PyboConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pybo'
