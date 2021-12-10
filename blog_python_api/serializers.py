from rest_framework import serializers
from blog_python_api.models import BlogPost
from django.contrib.auth.models import User

"""BlogPostSerializer that inherits from the model BlogPost class """
class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'author', 'image', 'body', 'created', 'updated'  ]


"""Django’s users are created from the User model defined in django.contrib.auth"""
class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']
        