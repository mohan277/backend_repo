from fb_post.models import Reaction

from fb_post.constants import ReactionChoices

from .check_for_exceptions import (
    is_valid_user_id,
    is_valid_post_id,
    is_valid_reaction_type
)


# Task 5
def react_to_post(user_id, post_id, reaction_type):

    is_valid_user_id(user_id)
    is_valid_post_id(post_id)
    is_valid_reaction_type(reaction_type)

    try:
        reaction_obj = Reaction.objects.get(
            reacted_by_id=user_id, post_id=post_id)

        for_updating_or_deleting_reaction_if_reaction_for_post_exists(
            reaction_obj, reaction_type)

    except:

        reaction_obj = Reaction.objects.create(
            reacted_by_id=user_id, post_id=post_id, reaction=reaction_type)

def for_updating_or_deleting_reaction_if_reaction_for_post_exists(
    reaction_obj, reaction_type):

    if reaction_obj.reaction == reaction_type:
        reaction_obj.delete()
    else:
        reaction_obj.reaction = reaction_type
        reaction_obj.save()