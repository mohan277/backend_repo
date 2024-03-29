from django.db.models import Count
from fb_post.models import Reaction


# Task 7
def get_total_reaction_count():
    return Reaction.objects.aggregate(count=Count('reaction'))
