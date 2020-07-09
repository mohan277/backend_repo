from fb_post.exceptions import (
    InvalidUserException,
    InvalidPostException,
    InvalidPostContent,
    InvalidCommentException,
    InvalidCommentContent,
    InvalidReplyContent,
    InvalidReactionTypeException,
    UserCannotDeletePostException)

from fb_post.models import User, Post, Comment
from fb_post.constants import ReactionChoices


def is_valid_user_id(user_id):
    try:
        User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise InvalidUserException


def is_valid_post_id(post_id):
    try:
        Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise InvalidPostException


def is_valid_post_content(post_content):

    empty_post_content = not post_content
    if empty_post_content:
        raise InvalidPostContent


def is_valid_comment_id(comment_id):
    try:
        Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        raise InvalidCommentException


def is_valid_comment_content(comment_content):

    empty_comment_content = not comment_content
    if empty_comment_content:
        raise InvalidCommentContent


def is_valid_reply_content(reply_content):
    empty_reply_content = not reply_content
    if empty_reply_content:
        raise InvalidReplyContent


def is_valid_reaction_type(reaction_type):

    REACTIONS_LIST = [reaction.value for reaction in ReactionChoices]

    is_valid_reaction = reaction_type not in REACTIONS_LIST
    if is_valid_reaction:
        raise InvalidReactionTypeException


def is_valid_user_can_delete_the_post(user_id, post_id):

    try:
        Post.objects.get(id=post_id, posted_by_id=user_id)

    except Post.DoesNotExist:
        raise UserCannotDeletePostException
