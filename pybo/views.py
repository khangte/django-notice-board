# 앱의 기능을 구현하는 파일이다.

from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕하세요 pybo에 오신 것을 환영합니다.")
