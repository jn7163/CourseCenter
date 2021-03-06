"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib.staticfiles.views import serve

from Center import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^download$', views.download),
    url(r'^upload$', views.upload),
    url(r'^task/upload$', views.task_upload),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^view/course$', views.view_course),
    url(r'^view/course_source$', views.view_course_source),
    url(r'^add/task$', views.add_task),
    url(r'^view/task$', views.view_task),
    url(r'^view/submit$', views.view_submit),
    url(r'^view/worksubmit$', views.view_worksubmit),
    url(r'^view/taskinfo$', views.view_taskinfo),
    url(r'^task/download$', views.task_download),
    url(r'^submit/upload$', views.submit_upload),
    url(r'^submit/download', views.submit_download),
    url(r'^submit/task$', views.submit_task),
    url(r'^score$', views.score),
    url(r'^(?P<path>.*\.[\w]*)$', serve),
]
