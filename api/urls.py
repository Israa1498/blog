from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    #path('delete/<delete_id>/', views.delete, name="delete"),
    path('<int:pk>/', views.RetrieveUpdateDestroyAPIView.as_view(), name="delete"),
    path('register/', views.RegisterView.as_view(), name='auth_register'),

]

urlpatterns = format_suffix_patterns(urlpatterns)