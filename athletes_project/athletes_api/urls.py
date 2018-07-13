from django.conf.urls import url 
from . import views


url patterns = [
	url(r'^hello-view/', views.HelloApiView.as_view()),
]