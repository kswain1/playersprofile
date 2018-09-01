from django.conf.urls import url 
from django.conf.urls import include 

from rest_framework.routers import DefaultRouter 

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)

#it's going to render this result for the api review
#endpoint is going to be hello-view, and it's going to render the as_view

urlpatterns = [
	url(r'^hello-view/', views.HelloApiView.as_view()),
	url(r'',include(router.urls))
]
