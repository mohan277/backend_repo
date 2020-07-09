from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
import pytz
from rest_framework.response import Response
from fb_post.utils import (
    create_post,
    get_post,
    reply_to_comment,
    react_to_post,
    react_to_comment,
    delete_post,
    create_comment,
    )
from fb_post.utils.exceptions import (
    InvalidUserException,
    InvalidPostException,
    InvalidPostContent,
    InvalidCommentContent,
    InvalidCommentException,
    InvalidReplyContent,
    InvalidReactionTypeException,
    UserCannotDeletePostException
    )
from fb_post.utils.constants import ReactionChoices

REACTIONS_LIST = [reaction.value for reaction in ReactionChoices]


# Task 1
class CreatePostRequestClass:
    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content


class CreatePostRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        return CreatePostRequestClass(**validated_data)


class CreatePostResponseClass:
    def __init__(self, post_id):
        self.post_id = post_id


class CreatePostResponseSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()

    def create(self, validated_data):
        return CreatePostResponseClass(**validated_data)


@api_view(['POST'])
def create_post_function(request):
    serializer = CreatePostRequestSerializer(data=request.data)
    is_invalid_request_data = not serializer.is_valid()

    if is_invalid_request_data:
        return Response(status=400)

    serializer_obj = serializer.save()
    try:
        post_id = create_post(serializer_obj.user_id, serializer_obj.content)
    except InvalidUserException:
        return Response(status=404)
    except InvalidPostContent:
        return Response(status=400)

    post_obj = CreatePostResponseClass(post_id)
    response_serializer = CreatePostResponseSerializer(post_obj)
    return Response(response_serializer.data, status=201)


# Task 2
class UserResponseSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    profile_pic = serializers.CharField()


class ReactionResponseSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    type = serializers.MultipleChoiceField(REACTIONS_LIST)


class ReplyResponseSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()
    commenter = UserResponseSerializer()
    commented_at = serializers.DateTimeField()
    comment_content = serializers.CharField(max_length=1000)
    reactions = ReactionResponseSerializer()


class CommentResponseSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()
    commenter = UserResponseSerializer()
    commented_at = serializers.DateTimeField()
    comment_content = serializers.CharField(max_length=1000)
    reactions = ReactionResponseSerializer()
    replies_count = serializers.IntegerField()
    replies = ReplyResponseSerializer(many=True)


class PostResponseSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    posted_by = UserResponseSerializer()
    posted_at = serializers.DateTimeField()
    post_content = serializers.CharField(max_length=1000)
    reactions = ReactionResponseSerializer()
    comments = CommentResponseSerializer(many=True)
    comments_count = serializers.IntegerField()


@api_view(['GET'])
def get_post_function(request, post_id):
    try:
        post_data = get_post(post_id)
    except InvalidPostException:
        return Response(status=404)

    serializer = PostResponseSerializer(data=post_data)
    if serializer.is_valid():
        return Response(serializer.data, status=200)
    return Response(serializer.errors)


# Task 3
class ReplyToCommentRequestClass:
    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content


class ReplyToCommentRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        return ReplyToCommentRequestClass(**validated_data)


class CreateReplyToCommentResponseClass:
    def __init__(self, reply_id):
        self.reply_id = reply_id


class CreateReplyToCommentResponseSerializer(serializers.Serializer):
    reply_id = serializers.IntegerField()

    def create(self, validated_data):
        return CreateReplyToCommentResponseClass(**validated_data)


@api_view(['POST'])
def create_reply_to_comment(request, comment_id):
    serializer = CreatePostRequestSerializer(data=request.data)
    is_invalid_request_data = not serializer.is_valid()

    if is_invalid_request_data:
        return Response(status=400)

    serializer_obj = serializer.save()
    try:
        reply_id = reply_to_comment(
            serializer_obj.user_id,
            comment_id,
            serializer_obj.content
            )
    except InvalidCommentException:
        return Response(status=404)
    except InvalidReplyContent:
        return Response(status=400)

    reply_obj = CreateReplyToCommentResponseClass(reply_id)
    response_serializer = CreateReplyToCommentResponseSerializer(reply_obj)
    return Response(response_serializer.data, status=201)


# Task 4
class ReactToPostRequestClass:
    def __init__(self, user_id, reaction_type):
        self.user_id = user_id
        self.reaction_type = reaction_type


class ReactToPostRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    reaction_type = serializers.ChoiceField(REACTIONS_LIST)

    def create(self, validated_data):
        return ReactToPostRequestClass(**validated_data)


@api_view(['POST'])
def create_reaction_to_post(request, post_id):
    serializer = ReactToPostRequestSerializer(data=request.data)
    is_invalid_request_data = not serializer.is_valid()

    if is_invalid_request_data:
        return Response(status=400)

    serializer_obj = serializer.save()
    try:
        react_to_post(
            serializer_obj.user_id,
            post_id,
            serializer_obj.reaction_type
            )
    except InvalidUserException:
        return Response(status=404)
    except InvalidPostException:
        return Response(status=404)

    return Response(status=200)


# Task 4
class ReactToCommentRequestClass:
    def __init__(self, user_id, reaction_type):
        self.user_id = user_id
        self.reaction_type = reaction_type


class ReactToCommentRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    reaction_type = serializers.ChoiceField(REACTIONS_LIST)

    def create(self, validated_data):
        return ReactToCommentRequestClass(**validated_data)


@api_view(['POST'])
def create_reaction_to_comment(request, comment_id):
    serializer = ReactToCommentRequestSerializer(data=request.data)
    is_invalid_request_data = not serializer.is_valid()

    if is_invalid_request_data:
        return Response(status=400)

    serializer_obj = serializer.save()
    try:
        react_to_comment(
            serializer_obj.user_id,
            comment_id,
            serializer_obj.reaction_type
            )
    except InvalidUserException:
        return Response(status=404)
    except InvalidPostException:
        return Response(status=404)

    return Response(status=200)


# Task 6
class DeleteRequestClass:
    def __init__(self, user_id):
        self.user_id = user_id


class DeleteRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        return DeleteRequestClass(**validated_data)


@api_view(['POST'])
def delete_post_function(request, post_id):
    serializer = DeleteRequestSerializer(data=request.data)
    is_invalid_request_data = not serializer.is_valid()

    if is_invalid_request_data:
        return Response(status=400)

    serializer_obj = serializer.save()
    try:
        delete_post(serializer_obj.user_id, post_id)
    except InvalidUserException:
        return Response(status=404)
    except InvalidPostException:
        return Response(status=404)
    except UserCannotDeletePostException:
        return Response(status=403)

    return Response(status=200)


# Task 7
class CreateCommentRequestClass:
    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content


class CreateCommentRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        return CreateCommentRequestClass(**validated_data)


class CreateCommentResponseClass:
    def __init__(self, comment_id):
        self.comment_id = comment_id


class CreateCommentResponseSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()

    def create(self, validated_data):
        return CreateCommentResponseClass(**validated_data)


@api_view(['POST'])
def create_comment_function(request, post_id):
    serializer = CreateCommentRequestSerializer(data=request.data)
    is_invalid_request_data = not serializer.is_valid()

    if is_invalid_request_data:
        return Response(status=400)

    serializer_obj = serializer.save()
    try:
        comment_id = create_comment(
            serializer_obj.user_id,
            post_id,
            serializer_obj.content
            )
    except InvalidUserException:
        return Response(status=404)
    except InvalidPostException:
        return Response(status=404)
    except InvalidCommentContent:
        return Response(status=400)

    comment_obj = CreateCommentResponseClass(comment_id)
    response_serializer = CreateCommentResponseSerializer(comment_obj)
    return Response(response_serializer.data, status=201)


from django.shortcuts import redirect, render
from django.utils import timezone


def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/fb_post/timezone/')
    else:
        return render(request, 'template.html', {'value': timezone.now()})