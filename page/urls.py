
from django.urls import url
from django.urls import path
from . import views

urlpatterns=[
     path('',views.Homepages1(TemplateView),name='home'),
 ]