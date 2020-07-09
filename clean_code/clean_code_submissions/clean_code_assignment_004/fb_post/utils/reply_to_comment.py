from fb_post.models import Comment

from .check_for_exceptions import (
    is_valid_user_id,
    is_valid_comment_id,
    is_valid_reply_content
)


# Task 4
def reply_to_comment(user_id, comment_id, reply_content):

    is_valid_user_id(user_id)
    is_valid_comment_id(comment_id)
    is_valid_reply_content(reply_content)

    comment_obj = Comment.objects.get(id=comment_id)

    if comment_obj.parent_comment_id is None:
        parent_comment_id=comment_id

    else:
        parent_comment_id=comment_obj.parent_comment_id

    reply_comment_obj = Comment.objects.create(
        content=reply_content, commented_by_id=user_id,
        post_id=comment_obj.post.id, parent_comment_id=parent_comment_id)

    return reply_comment_obj.id
