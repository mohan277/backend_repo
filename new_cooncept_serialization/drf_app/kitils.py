from datetime import datetime

from rest_framework import serializers

from rest_framework.renderers import JSONRenderer

import io

from rest_framework.parsers import JSONParser


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

class CommentSerializer(serializers.Serializer):
    user = UserSerializer(required=False)
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age