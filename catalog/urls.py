from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('author/', views.AuthorListView.as_view(), name='authors'),
    path('books/<slug:slug>/', views.BookDetailView.as_view(), name='book-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),

]
