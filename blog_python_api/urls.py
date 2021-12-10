from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from blog_python_api import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('blogposts/', views.BlogPostList.as_view()),
    path('blogposts/<int:pk>/', views.BlogPostDetail.as_view()), 
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]

urlpatterns = format_suffix_patterns(urlpatterns)