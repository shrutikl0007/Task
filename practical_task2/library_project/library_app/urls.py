
from django.urls import path
from library_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('add_book/', views.add_book, name='add_book'),
    path('approve_requests/', views.approve_requests, name='approve_requests'),
    path('view_books/', views.view_books, name='view_books'),
    path('logout/', views.logout, name='logout'),
]
