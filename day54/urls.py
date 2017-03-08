"""day54 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from exam_1.views import classes
from exam_1.views import teachers
from exam_1.views import students
from exam_1.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index$', index.index),


    url(r'^classes.html$', classes.get_classes),
    url(r'^add_classes.html$', classes.add_classes),
    url(r'^del_classes.html$', classes.del_classes),
    url(r'^edit_classes.html$', classes.edit_classes),

    url(r'^students.html$',students.get_students),
    url(r'^add_students.html$',students.add_students),
    url(r'^del_students.html$',students.del_students),
    url(r'^edit_students.html$',students.edit_students),

    url(r'^teachers.html$',teachers.get_teachers),
    url(r'^add_teachers.html$',teachers.add_teachers),
    url(r'^del_teachers.html$',teachers.del_teachers),
    url(r'^edit_teachers.html$',teachers.edit_teachers),
]
