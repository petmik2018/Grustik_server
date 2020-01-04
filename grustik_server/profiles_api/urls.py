from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    # path('login/', views.UserLoginApiView.as_view()),
    # path('', include(router.urls))
]