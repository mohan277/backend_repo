from fb_post.models import Post

from .check_for_exceptions import (
    is_valid_user_id,
    is_valid_post_content
)


# Task 2
def create_post(user_id, post_content):

    is_valid_user_id(user_id)
    is_valid_post_content(post_content)

    post_obj = Post.objects.create(content=post_content, posted_by_id=user_id)
    return post_obj.id
