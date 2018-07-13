from django.conf.urls import url 
from . import views

#it's going to render this result for the api review
#endpoint is going to be hello-view, and it's going to render the as_view

urlpatterns = [
	url(r'^hello-view/', views.HelloApiView.as_view()),

]