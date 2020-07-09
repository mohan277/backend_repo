from django.db.models import Count, Q, F

from fb_post.models import Post

from fb_post.constants import PositiveReactions, NegativeReactions


# Task 10
def get_posts_with_more_positive_reactions():

    positive_reactions_list = [
        reaction.value for reaction in PositiveReactions]

    negative_reactions_list = [
        reaction.value for reaction in NegativeReactions]

    positive_reactions_count = Count(
        'reaction', filter=Q(reaction__reaction__in=positive_reactions_list))
    negative_reactions_count = Count(
        'reaction', filter=Q(reaction__reaction__in=negative_reactions_list))

    post_ids_list_with_more_positive_reactions = list(Post.objects.annotate(
        pos=positive_reactions_count, neg=negative_reactions_count).filter(
            pos__gt=F('neg')).values_list('id', flat=True))

    return post_ids_list_with_more_positive_reactions
