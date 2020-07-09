from fb_post.models import Post

from .check_for_exceptions import (
    is_valid_user_id
)

# Task 11
def get_posts_reacted_by_user(user_id):

    is_valid_user_id(user_id)

    list_of_post_ids = list(Post.objects.filter(
        reaction__reacted_by_id=user_id).values_list('id', flat=True))
    return list_of_post_ids
