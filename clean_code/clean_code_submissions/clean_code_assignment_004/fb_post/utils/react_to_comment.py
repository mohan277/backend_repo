from fb_post.models import Reaction

from .check_for_exceptions import (
    is_valid_user_id,
    is_valid_comment_id,
    is_valid_reaction_type,
)


# Task 6
def react_to_comment(user_id, comment_id, reaction_type):

    is_valid_user_id(user_id)
    is_valid_comment_id(comment_id)
    is_valid_reaction_type(reaction_type)

    try:
        reaction_obj = Reaction.objects.get(
            reacted_by_id=user_id, comment_id=comment_id)

        for_updating_or_deleting_reaction_if_reaction_exists(
            reaction_obj, reaction_type)

    except Reaction.DoesNotExist:
        reaction_obj = Reaction.objects.create(
            reacted_by_id=user_id, comment_id=comment_id,
            reaction=reaction_type)

def for_updating_or_deleting_reaction_if_reaction_exists(
        reaction_obj, reaction_type):

    if reaction_obj.reaction == reaction_type:
        reaction_obj.delete()
    else:
        reaction_obj.reaction = reaction_type
        reaction_obj.save()
