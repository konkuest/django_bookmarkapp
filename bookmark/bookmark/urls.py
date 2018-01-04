"""bookmark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from bookmark.views import BookmarkLV, BookmarkDV #뷰를 호출해야하니 뷰에서 쓰일 클래스를 import

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #regex로 URL을 정의해주고 어떤 view로 넘길지 연결해준다
    url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
    url(r'^bookmark/(?P<pk>\d+)$', BookmarkDV.as_view(), name='detail'),
]
