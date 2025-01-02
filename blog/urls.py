from django.urls import path
from . import views

urlpatterns = [
	path('', views.viewDashboard, name = "alias_viewBlogDashboard"),
	path('profile/', views.viewProfile, name = "alias_viewProfile"),
]