from django.urls import path
from . import views

urlpatterns = [
	path('', views.main, name = 'main'),
  path('signup', views.signup, name = 'signup'),
  path('deluser', views.deluser, name = 'deluser'),
]
