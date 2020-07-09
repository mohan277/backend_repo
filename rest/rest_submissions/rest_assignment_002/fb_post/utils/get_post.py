from fb_post.models import Post

from .check_for_exceptions import (
    is_valid_post_id
)

# Task 13
def get_post(post_id):

    is_valid_post_id(post_id)
    post_obj = Post.objects.select_related('posted_by').prefetch_related(
            'comment_set', 'comment_set__commented_by',
            'comment_set__reaction_set', 'reaction_set').get(id=post_id)

    return post_details(post_obj)

def post_details(post_obj):

    comment_objs = post_obj.comment_set.all()
    comments_list = []
    for comment_obj in comment_objs:

        replies = []
        for reply in comment_objs:
            if reply.parent_comment_id == comment_obj.id:
                reply_dict = {
                    'comment_id': reply.id,
                    'commenter': {
                        'user_id': reply.commented_by.id,
                        'name': reply.commented_by.name,
                        'profile_pic': reply.commented_by.profile_pic
                    },
                    'commented_at': str(reply.commented_at)[:-6],
                    'comment_content': reply.content,
                    'reactions': {
                        'count': len(reply.reaction_set.all()),
                        'type': list(dict.fromkeys([reaction.reaction for reaction in reply.reaction_set.all()]))
                    },
                }
                replies.append(reply_dict)

        if comment_obj.parent_comment_id is None:
            comment_dict = {
                'comment_id': comment_obj.id,
                'commenter': {
                    'user_id': comment_obj.commented_by.id,
                    'name': comment_obj.commented_by.name,
                    'profile_pic': comment_obj.commented_by.profile_pic
                },
            'commented_at': str(comment_obj.commented_at)[:-6],
            'comment_content':  comment_obj.content,
            'reactions': {
                'count': len(comment_obj.reaction_set.all()),
                'type': list(dict.fromkeys([reaction.reaction for reaction in comment_obj.reaction_set.all()]))
            },
            'replies_count': len(replies),
            'replies': replies
            }
            comments_list.append(comment_dict)

    post_details_dict = {
        'post_id': post_obj.id,
        'posted_by': {
            'name': post_obj.posted_by.name,
            'user_id': post_obj.posted_by.id,
            'profile_pic': post_obj.posted_by.profile_pic
        },
        'posted_at': str(post_obj.posted_at)[:-6],
        'post_content': post_obj.content,
        'reactions': {
            'count': len(post_obj.reaction_set.all()),
            'type': list(dict.fromkeys([reaction.reaction for reaction in post_obj.reaction_set.all()]))

        },

        'comments':comments_list,
        "comments_count": len(comments_list)
    }
    return post_details_dict
