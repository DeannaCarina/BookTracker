from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all', views.all_books, name='books'),
    path('unread_books', views.unread_books, name='unread_books'),
    path('completed_books', views.completed_books, name='completed_books'),
    path('<int:pk>/', views.view_book, name='view_book'),
    path('add', views.add_book, name='add_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
]