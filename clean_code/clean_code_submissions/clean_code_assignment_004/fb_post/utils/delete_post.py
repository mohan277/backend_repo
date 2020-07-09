from fb_post.models import Post

from .check_for_exceptions import (
    is_valid_user_id,
    is_valid_post_id,
    is_valid_user_can_delete_the_post
)

# Task 9
def delete_post(user_id, post_id):

    is_valid_user_id(user_id)
    is_valid_post_id(post_id)
    is_valid_user_can_delete_the_post(user_id, post_id)

    post_obj = Post.objects.select_related('posted_by').get(id=post_id)
    post_obj.delete()
