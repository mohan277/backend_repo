from datetime import datetime

from rest_framework import serializers

from rest_framework.renderers import JSONRenderer

import io

from rest_framework.parsers import JSONParser

class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance


    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email')
    #     instance.content = validated_data.get('content')
    #     instance.created = validated_data.get('created')
    #     return instance
