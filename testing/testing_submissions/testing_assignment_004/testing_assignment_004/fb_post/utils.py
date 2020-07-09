from .models import *
from .exceptions import *
from django.db.models import *

REACTIONS_LIST = ['WOW', 'LIT', 'LOVE', 'HAHA',
                  'THUMBS-UP', 'THUMBS-DOWN', 'ANGRY', 'SAD']


# Task 2
def create_post(user_id, post_content):

    if User.objects.filter(id=user_id).exists() is False:
        raise InvalidUserException
    if not post_content:
        raise InvalidPostContent

    post_obj = Post.objects.create(content=post_content, posted_by_id=user_id)
    return post_obj.id


# Task 3
def create_comment(user_id, post_id, comment_content):

    if User.objects.filter(id=user_id).exists() is False:
        raise InvalidUserException

    if Post.objects.filter(id=post_id).exists() is False:
        raise InvalidPostException

    if not comment_content:
        raise InvalidCommentContent

    comment_obj = Comment.objects.create(content=comment_content,
                                         commented_by_id=user_id,
                                         post_id=post_id)
    return comment_obj.id


# Task 4
def reply_to_comment(user_id, comment_id, reply_content):

    comment_obj = Comment.objects.filter(id=comment_id)
    user_obj = User.objects.filter(id=user_id)
    if not user_obj:
        raise InvalidUserException

    if not comment_obj:
        raise InvalidCommentException

    if not reply_content:
        raise InvalidReplyContent

    if comment_obj[0].parent_comment_id is None:
        parent_comment_obj = Comment.objects.create(
            content=reply_content, commented_by_id=user_id,
            post_id=comment_obj[0].post.id, parent_comment_id=comment_id)
        return parent_comment_obj.id
    else:
        reply_to_comment_obj = Comment.objects.create(
            content=reply_content, commented_by_id=user_id,
            post_id=comment_obj[0].post.id,
            parent_comment_id=comment_obj[0].parent_comment_id)
        return reply_to_comment_obj.id


# Task 5
def react_to_post(user_id, post_id, reaction_type):

    reaction_obj = Reaction.objects.filter(reacted_by_id=user_id,
                                           post_id=post_id)

    if User.objects.filter(id=user_id).exists() is False:
        raise InvalidUserException

    if Post.objects.filter(id=post_id).exists() is False:
        raise InvalidPostException

    if reaction_type not in REACTIONS_LIST:
        raise InvalidReactionTypeException

    if reaction_obj:
        if reaction_obj[0].reaction == reaction_type:
            reaction_obj[0].delete()
        else:
            reaction_obj[0].reaction = reaction_type
            reaction_obj[0].save()
    else:
        reaction_obj = Reaction.objects.create(
            reacted_by_id=user_id, post_id=post_id, reaction=reaction_type)


# Task 6
def react_to_comment(user_id, comment_id, reaction_type):

    reaction_obj = Reaction.objects.filter(reacted_by_id=user_id,
                                           comment_id=comment_id)

    if User.objects.filter(id=user_id).exists() is False:
        raise InvalidUserException

    if Comment.objects.filter(id=comment_id).exists() is False:
        raise InvalidCommentException

    if reaction_type not in REACTIONS_LIST:
        raise InvalidReactionTypeException

    if reaction_obj:
        if reaction_obj[0].reaction == reaction_type:
            reaction_obj[0].delete()
        else:
            reaction_obj[0].reaction = reaction_type
            reaction_obj[0].save()
    else:
        reaction_obj = Reaction.objects.create(
            reacted_by_id=user_id, comment_id=comment_id,
            reaction=reaction_type)


# Task 7
def get_total_reaction_count():
    return Reaction.objects.aggregate(count = Count('reaction'))

# Task 8
def get_reaction_metrics(post_id):

    if Post.objects.filter(id=post_id).exists() is False:
        raise InvalidPostException

    reaction_obj = Reaction.objects.filter(
        post_id=post_id).values_list('reaction')
    return dict(reaction_obj.annotate(Count('reaction')))


# Task 9
def delete_post(user_id, post_id):

    post_obj = Post.objects.filter(id=post_id).select_related('posted_by')

    if User.objects.filter(id=user_id).exists() is False:
        raise InvalidUserException

    if not post_obj:
        raise InvalidPostException

    if post_obj[0].posted_by_id == user_id:
        post_obj[0].delete()
    else:
        raise UserCannotDeletePostException


# Task 10
def get_posts_with_more_positive_reactions():

    POSITIVE_REACTIONS = ['THUMBS-UP', 'LIT', 'LOVE', 'HAHA', 'WOW']
    NEGATIVE_REACTIONS = ['SAD', 'ANGRY', 'THUMBS-DOWN']

    positive_count = Count(
        'reaction', filter=Q(reaction__reaction__in=POSITIVE_REACTIONS))
    negative_count = Count(
        'reaction', filter=Q(reaction__reaction__in=NEGATIVE_REACTIONS))

    return list(
        Post.objects.annotate(pos=positive_count, neg=negative_count).filter(
            pos__gt=F('neg')).values_list('id', flat=True))


# Task 11
def get_posts_reacted_by_user(user_id):

    if User.objects.filter(id=user_id).exists() is False:
        raise InvalidUserException

    list_of_post_ids = Post.objects.filter(reaction__reacted_by_id = user_id).values_list('id',flat=True)
    return list(list_of_post_ids)


# Task 12
def get_reactions_to_post(post_id):

    post_obj = Post.objects.filter(id=post_id)

    if post_obj:
        reactions = Reaction.objects.filter(post_id=post_id).values('reacted_by_id','reacted_by__name','reacted_by__profile_pic','reaction')
        reactions_list = []

        for reaction in reactions:
            reaction_dict = {
                'user_id': reaction['reacted_by_id'],
                'name': reaction['reacted_by__name'],
                'profile_pic': reaction['reacted_by__profile_pic'],
                'reaction':reaction['reaction']
            }
            reactions_list.append(reaction_dict)
        return reactions_list
    else:
        raise InvalidPostException


# Task 13
def get_post(post_id):

    try:
        post_objs = list(Post.objects.filter(id=post_id).select_related('posted_by').prefetch_related('comment_set','comment_set__commented_by','comment_set__reaction_set','reaction_set'))
        return post_details(post_objs[0])
    except:
        raise InvalidPostException

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

# Task 14
def get_user_posts(user_id):
    user_obj = User.objects.filter(id=user_id)

    if user_obj:
        post_objs = list(Post.objects.filter(posted_by_id=user_id).select_related('posted_by').prefetch_related('comment_set','comment_set__commented_by','comment_set__reaction_set','reaction_set'))

        # user_posts_list = []
        # for post_obj in post_objs:
        #     user_posts_list.append(post_details(post_obj))
        # return user_posts_list
        return [post_details(post_obj) for post_obj in post_objs]

    else:
        raise InvalidUserException

# Task 15
def get_replies_for_comment(comment_id):

    reply_objs = Comment.objects.filter(parent_comment_id=comment_id).select_related('commented_by')

    if Comment.objects.filter(id=comment_id).exists() is False:
        raise InvalidCommentException

    replies = []
    for reply_obj in reply_objs:
        if reply_obj.parent_comment_id == comment_id:
            reply_dict = {
                'comment_id': reply_obj.id,
                'commenter': {
                    'user_id': reply_obj.commented_by.id,
                    'name': reply_obj.commented_by.name,
                    'profile_pic': reply_obj.commented_by.profile_pic
                },
                'commented_at': str(reply_obj.commented_at)[:-6],
                'comment_content': reply_obj.content
            }
            replies.append(reply_dict)
    return replies


# def invalid_user_exception():
# def invalid_post_exception():
# def invalid_comment_exception():
# def invalid_post_content():
# def user_cannot_delete_post_exception():
# def invalid_reaction_type_exception():
# def invalid_reply_content():