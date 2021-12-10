from django.shortcuts import render
from rest_framework import generics
from blog_python_api import serializers
from django.contrib.auth.models import User
from blog_python_api.models import BlogPost
from rest_framework import permissions
from blog_python_api.permissions import IsOwnerOrReadOnly


# Create your views here.

"""UserList & ListAPIView is used for read-only endpoints and provides a GET method handler for registered Users."""
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

"""UserDetail & RetrieveAPIView is used for read-only endpoints and provides GET method handler for number of User blog posts uploaded"""
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

"""ListCreateAPIView is used for GET and POST methods for a list of blogposts"""
class BlogPostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer
# IsAuthenticatedOrReadOnly permission is for authenticated users who can perform any request, whereas non-authenticated users can perform only read-only requests
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

"""RetrieveUpdateDestroyAPIView is used for GET, PUT, and DELETE methods on a specific blogpost"""
class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer
    # IsAuthenticatedOrReadOnly and IsOwnerOrReadOnly are both required as updating and destroying a post should only be allowed for an authenticated user who is also the owner of the post
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                            IsOwnerOrReadOnly]