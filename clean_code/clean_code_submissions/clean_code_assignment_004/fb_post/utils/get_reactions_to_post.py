from fb_post.models import Reaction

from .check_for_exceptions import (
    is_valid_post_id
)

# Task 12
def get_reactions_to_post(post_id):

    is_valid_post_id(post_id)

    reaction_details_list = Reaction.objects.filter(
        post_id=post_id).values(
            'reacted_by_id','reacted_by__name','reacted_by__profile_pic','reaction')

    list_of_dictionaries = []

    for reaction in reaction_details_list:
        user_details_dict = {
            'user_id': reaction['reacted_by_id'],
            'name': reaction['reacted_by__name'],
            'profile_pic': reaction['reacted_by__profile_pic'],
            'reaction':reaction['reaction']
        }
        list_of_dictionaries.append(user_details_dict)
    return list_of_dictionaries
