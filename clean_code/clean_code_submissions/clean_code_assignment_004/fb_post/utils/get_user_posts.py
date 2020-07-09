# from .models import *
# from .exceptions import *
# from django.db.models import *

# # Task 14
# def get_user_posts(user_id):
#     user_obj = User.objects.filter(id=user_id)

#     if user_obj:
        # post_objs = list(Post.objects.filter(
        #     posted_by_id=user_id).select_related(
        #         'posted_by').prefetch_related(
        #             'comment_set', 'comment_set__commented_by',
        #             'comment_set__reaction_set', 'reaction_set'))

#         # user_posts_list = []
#         # for post_obj in post_objs:
#         #     user_posts_list.append(post_details(post_obj))
#         # return user_posts_list
#         return [post_details(post_obj) for post_obj in post_objs]

#     else:
#         raise InvalidUserException
