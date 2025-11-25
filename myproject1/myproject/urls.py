"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from basic.views import sample
from basic.views import sample1
from basic.views import sampleinfo
from basic.views import dynamicResponse
from calculations.views import addition
from calculations.views import substraction
from calculations.views import multiplication
from calculations.views import division
from calculations.views import fdivision
from basic.views import health
from basic.views import addStudent
from basic.views import student_api,job1,job2
from basic.views import signUp
from basic.views import movie,movies_review,login
from basic.views import check,changepassword


urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet', sample),
    path('nani', sample1),
    path('info', sampleinfo),
    path('dynamic',dynamicResponse),
    path("add",addition),
    path("sub",substraction),
    path("mul",multiplication),
    path("div",division),
    path("fdiv",fdivision),
    path("hel",health),
    path("Student",addStudent),
    path("getbyid",student_api),
    path('job1/',job1),
    path('job2',job2),
    path('signup/',signUp),
    path("movie/",movie),
    path("movies/",movies_review),
    path("check/",check),
    path("login/",login),
    path("changepassword/",changepassword)
]

