# from .models import *
# from .exceptions import *
# from django.db.models import *

# # Task 15
# def get_replies_for_comment(comment_id):

    # reply_objs = Comment.objects.filter(
        # parent_comment_id=comment_id).select_related('commented_by')

#     if Comment.objects.filter(id=comment_id).exists() is False:
#         raise InvalidCommentException

#     replies = []
#     for reply_obj in reply_objs:
#         if reply_obj.parent_comment_id == comment_id:
#             reply_dict = {
#                 'comment_id': reply_obj.id,
#                 'commenter': {
#                     'user_id': reply_obj.commented_by.id,
#                     'name': reply_obj.commented_by.name,
#                     'profile_pic': reply_obj.commented_by.profile_pic
#                 },
#                 'commented_at': str(reply_obj.commented_at)[:-6],
#                 'comment_content': reply_obj.content
#             }
#             replies.append(reply_dict)
#     return replies
