from django.urls import path
from LibraryApp import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('', views.TemplateView.as_view(template_name='home.html'), name='home'), # another way 
    # path('home/', views.RedirectView.as_view(url='/CBV_apis'),name='home'),
    path('index/', views.RedirectView.as_view(url='/CBV_apis'),name='index '),
    path('home/', views.HomeRedirectView.as_view(), name='home_redirect'),
    path('books/',views.BookListView.as_view(),name='books'),
    path('books/<int:id>/',views.BookDetailView.as_view(),name='book_detail'),
    path('books/add/',views.BookCreateView.as_view(),name='book_add'),
    path('books/update/<int:pk>/',views.BookUpdateView.as_view(),name='book_update'),
    path('books/delete/<int:pk>/',views.BookDeleteView.as_view(),name='book_delete'),
    # path('add/',views.BookFormView.as_view(),name='book_add'), # Using FormView Class
    path('successfully_added/',views.SuccessfullyAddedView.as_view(),name='successfully_added'),



]