from fb_post.models import Reaction

from django.db.models import Count

from .check_for_exceptions import (
    is_valid_post_id
)

# Task 8
def get_reaction_metrics(post_id):

    is_valid_post_id(post_id)

    reaction_types_count = Reaction.objects.filter(
        post_id=post_id).values_list('reaction').annotate(Count('reaction'))
    return dict(reaction_types_count)
