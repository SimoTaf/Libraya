from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView



app_name = 'library'
urlpatterns = [
    

    path('', HomeView.as_view(), name='home'),
    


    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='library:login'), name='logout'),

    path('books/', BookView.as_view(), name='book-list'),
    path('book/create/', BookCreate.as_view(), name='book-create'),
    path('book/<slug:pk>/', BookDetail.as_view(), name= 'book'),
    path('book/<slug:pk>/update/', BookUpdate.as_view(), name='book-update'),
    path('book/<slug:pk>/delete/', BookDelete.as_view(), name='book-delete'),



    path('students/', StudentView.as_view(), name='student-list'),
    path('student/create/', StudentCreate.as_view(), name='student-create'),
    path('student/<slug:pk>/', StudentDetail.as_view(), name='student-detail'),
    path('student/<slug:pk>/update/', StudentUpdate.as_view(), name='student-update'),
    path('student/<slug:pk>/delete/', StudentDelete.as_view(), name='student-delete'),


 


]
