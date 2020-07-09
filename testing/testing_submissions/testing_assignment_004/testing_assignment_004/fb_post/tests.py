from django.test import TestCase
from .models import *
from .exceptions import *
from .constants import PositiveReactions, NegativeReactions
from .utils import *
import pytest
from collections import Counter
from django.db.models import *

from .factories import *

from freezegun import freeze_time
import datetime

pytestmark = pytest.mark.django_db

# _____________________populate_database__________________

@pytest.fixture
@freeze_time('2020-04-18')
def user():
    User.objects.bulk_create([
    User(name = 'user1',profile_pic = 'profile1'),
    User(name = 'user2',profile_pic = 'profile2'),
    User(name = 'user3',profile_pic = 'profile3'),
    User(name = 'user4',profile_pic = 'profile4'),
    User(name = 'user5',profile_pic = 'profile5'),
    User(name = 'user6',profile_pic = 'profile6'),
    User(name = 'user7',profile_pic = 'profile7'),
    User(name = 'user8',profile_pic = 'profile8'),
    ])

@pytest.fixture
@freeze_time('2020-04-18')
def post(user):
    Post.objects.bulk_create([
    Post(content = 'post1',posted_by_id = 1),
    Post(content = 'post2',posted_by_id = 2),
    Post(content = 'post3',posted_by_id = 3),
    Post(content = 'post4',posted_by_id = 4),
    Post(content = 'post5',posted_by_id = 3),
    Post(content = 'post6',posted_by_id = 6),
    ])


@pytest.fixture
@freeze_time('2020-04-18')
def comment(post):
    Comment.objects.bulk_create([
    Comment(content = 'comment1',commented_by_id = 1,post_id = 1),
    Comment(content = 'comment2',commented_by_id = 2,post_id = 1),
    Comment(content = 'comment4',commented_by_id = 4,post_id = 4),
    Comment(content = 'comment5',commented_by_id = 7,post_id = 6),
    ])


@pytest.fixture
@freeze_time('2020-04-18')
def reply(comment):
    Comment.objects.bulk_create([
    Comment(content = 'reply1',commented_by_id = 1,post_id = 1,parent_comment_id = 1),
    Comment(content = 'reply2',commented_by_id = 2,post_id = 1,parent_comment_id = 1),
    Comment(content = 'reply3',commented_by_id = 3,post_id = 1,parent_comment_id = 2),
    Comment(content = 'reply4',commented_by_id = 1,post_id = 1,parent_comment_id = 2)
    ])


@pytest.fixture
@freeze_time('2020-04-18')
def post_reaction(post):
    Reaction.objects.bulk_create([
    Reaction(post_id = 1,reaction = 'WOW',reacted_by_id = 1),
    Reaction(post_id = 1,reaction = 'LIT',reacted_by_id = 2),
    Reaction(post_id = 1,reaction = 'LOVE',reacted_by_id = 3),
    Reaction(post_id = 2,reaction = 'LIT',reacted_by_id = 1),
    Reaction(post_id = 2,reaction = 'WOW',reacted_by_id = 2),
    Reaction(post_id = 2,reaction = 'LOVE',reacted_by_id = 3),
    Reaction(post_id = 2,reaction = 'THUMBS-UP',reacted_by_id = 4),
    Reaction(post_id = 3,reaction = 'SAD',reacted_by_id = 1),
    Reaction(post_id = 3,reaction = 'SAD',reacted_by_id = 2),
    Reaction(post_id = 3,reaction = 'ANGRY',reacted_by_id = 4),
    ])


@pytest.fixture
@freeze_time('2020-04-18')
def comment_reaction(comment):
    Reaction.objects.bulk_create([
    Reaction(comment_id = 1,reaction = 'ANGRY',reacted_by_id = 1),
    Reaction(comment_id = 2,reaction = 'WOW',reacted_by_id = 2),
    Reaction(comment_id = 3,reaction = 'LIT',reacted_by_id = 3),
    ])



def test_create_post_with_invalid_user_id_raise_exception(user):

    # Arrange
    user_id = 10
    post_content = 'Hello'

    # Act

    # Assert
    with pytest.raises(InvalidUserException):
        create_post(user_id, post_content)


def test_create_post_with_invalid_post_content_raise_exception(user):

    # Arrange
    user_id = 5
    post_content = ''

    # Act

    # Assert
    with pytest.raises(InvalidPostContent):
        create_post(user_id, post_content)


@freeze_time('2020-04-18')
def test_create_post_with_valid_details_returns_post_id(user):

    # Arrange
    expected_user_id = 1
    expected_post_content = 'Hello'
    expected_post_id = 1

    # Act
    post_id  = create_post(expected_user_id, expected_post_content)

    # Assert
    post_obj = Post.objects.get(id=post_id)
    assert post_obj.posted_by_id == expected_user_id
    assert post_obj.id == expected_post_id
    assert post_obj.content == expected_post_content
    assert post_obj.posted_at.replace(tzinfo=None) == datetime.datetime(2020, 4, 18)



def test_create_comment_with_invalid_user_id_raise_exception(user):

    # Arrange
    user_id = 10
    post_id = 2
    comment_content = 'Thank you'

    # Act

    # Assert
    with pytest.raises(InvalidUserException):
        create_comment(user_id, post_id, comment_content)


def test_create_comment_with_invalid_post_id_raise_exception(user):

    # Arrange
    user_id = 4
    post_id = 10
    comment_content = 'Thank you'

    # Act

    # Assert
    with pytest.raises(InvalidPostException):
        create_comment(user_id, post_id, comment_content)


def test_create_comment_with_invalid_comment_content_raise_exception(comment):

    # Arrange
    user_id = 4
    post_id = 4
    comment_content = ''

    # Act

    # Assert
    with pytest.raises(InvalidCommentContent):
        create_comment(user_id, post_id, comment_content)


@freeze_time('2020-04-18')
def test_create_comment_with_valid_details_returns_comment_id(comment):

    # Arrange
    expected_user_id = 1
    expected_post_id = 2
    expected_comment_content = 'Thank you'

    # Act
    comment_id = create_comment(expected_user_id,
                                expected_post_id,
                                expected_comment_content)
    # Assert
    comment_obj = Comment.objects.get(id=comment_id)
    assert comment_obj.id == comment_id
    assert comment_obj.content == expected_comment_content
    assert comment_obj.commented_by_id == expected_user_id
    assert comment_obj.post_id == expected_post_id
    assert comment_obj.commented_at.replace(tzinfo=None) == datetime.datetime(2020, 4, 18)
    assert comment_obj.parent_comment_id is None


def test_reply_to_comment_with_invalid_user_id_raise_exception(reply):

    # Arrange
    user_id = 10
    comment_id = 4
    reply_content = 'Good looking'

    # Act

    # Assert
    with pytest.raises(InvalidUserException):
        reply_to_comment(user_id, comment_id, reply_content)


def test_reply_to_comment_with_invalid_comment_id_raise_exception(reply):

    # Arrange
    user_id = 1
    comment_id = 50
    reply_content = 'Good looking'

    # Act

    # Assert
    with pytest.raises(InvalidCommentException):
        reply_to_comment(user_id, comment_id, reply_content)


def test_reply_to_comment_with_invalid_reply_content_raise_exception(reply):

    # Arrange
    user_id = 1
    comment_id = 4
    reply_content = ''

    # Act

    # Assert
    with pytest.raises(InvalidReplyContent):
        reply_to_comment(user_id, comment_id, reply_content)


@freeze_time('2020-04-18')
def test_reply_to_comment_with_valid_details_returns_reply_comment_id(reply):

    # Arrange
    expected_user_id = 1
    expected_comment_id = 4
    expected_reply_content = 'Good looking'
    expected_parent_comment_id = 4

    # Act
    reply_comment_id = reply_to_comment(expected_user_id,
                                        expected_comment_id,
                                        expected_reply_content)

    # Assert
    reply_comment_obj = Comment.objects.get(id=reply_comment_id)
    assert reply_comment_obj.id == reply_comment_id
    assert reply_comment_obj.content == expected_reply_content
    assert reply_comment_obj.commented_by_id == expected_user_id
    assert reply_comment_obj.commented_at.replace(tzinfo=None) == datetime.datetime(2020, 4, 18)
    assert reply_comment_obj.parent_comment_id == expected_parent_comment_id


def test_react_to_post_with_invalid_user_id_raise_exception(post):

    # Arrange
    user_id = 10
    post_id = 2
    reaction_type = 'WOW'

    # Act

    # Assert
    with pytest.raises(InvalidUserException):
        react_to_post(user_id, post_id, reaction_type)


def test_react_to_post_with_invalid_post_id_raise_exception(post):

    # Arrange
    user_id = 2
    post_id = 10
    reaction_type = 'WOW'

    # Act

    # Assert
    with pytest.raises(InvalidPostException):
        react_to_post(user_id, post_id, reaction_type)


def test_react_to_post_with_invalid_reaction_type_raise_exception(post):

    # Arrange
    user_id = 2
    post_id = 2
    reaction_type = 'NICE'

    # Act

    # Assert
    with pytest.raises(InvalidReactionTypeException):
        react_to_post(user_id, post_id, reaction_type)

@freeze_time('2020-4-18')
def test_react_to_post_with_valid_details(post):

    # Arrange
    expected_user_id = 1
    expected_post_id = 1
    expected_reaction_type = 'WOW'
    expected_reaction_id = 1

    # Act
    react_to_post(expected_user_id, expected_post_id, expected_reaction_type)

    # Assert
    reaction_obj = Reaction.objects.get(id=1)
    assert reaction_obj.id == expected_reaction_id
    assert reaction_obj.post_id == expected_post_id
    assert reaction_obj.reacted_by_id == expected_user_id
    assert reaction_obj.reaction == expected_reaction_type
    assert reaction_obj.reacted_at.replace(tzinfo=None) == datetime.datetime(2020, 4, 18)


def test_react_to_comment_with_invalid_user_id_raise_exception(comment):

    # Arrange
    user_id = 10
    comment_id = 2
    reaction_type = 'WOW'

    # Act

    # Assert
    with pytest.raises(InvalidUserException):
        react_to_comment(user_id, comment_id, reaction_type)


def test_react_to_comment_with_invalid_comment_id_raise_exception(comment):

    # Arrange
    user_id = 1
    comment_id = 50
    reaction_type = 'WOW'

    # Act

    # Assert
    with pytest.raises(InvalidCommentException):
        react_to_comment(user_id, comment_id, reaction_type)


def test_react_to_comment_with_invalid_reaction_type_raise_exception(comment):

    # Arrange
    user_id = 1
    comment_id = 2
    reaction_type = 'NICE'

    # Act

    # Assert
    with pytest.raises(InvalidReactionTypeException):
        react_to_comment(user_id, comment_id, reaction_type)

@freeze_time('2020-4-18')
def test_react_to_comment_with_valid_details(comment):

    # Arrange
    expected_user_id = 1
    expected_comment_id = 1
    expected_reaction_type = 'ANGRY'
    expected_reaction_id = 1

    # Act
    react_to_comment(expected_user_id, expected_comment_id, expected_reaction_type)

    # Assert
    reaction_obj = Reaction.objects.get(id=1)
    assert reaction_obj.id == expected_reaction_id
    assert reaction_obj.comment_id == expected_comment_id
    assert reaction_obj.reaction == expected_reaction_type
    assert reaction_obj.reacted_by_id == expected_user_id
    assert reaction_obj.reacted_at.replace(tzinfo=None) == datetime.datetime(2020, 4, 18)

# get_total_reaction_count()
def test_get_total_reaction_count_returns_total_number_of_reactions(user, post, comment, reply, comment_reaction, post_reaction):

    # Arrange
    expected_count = 13

    # Act
    total_recations_count = get_total_reaction_count()

    # Assert
    assert total_recations_count['count'] == expected_count


def test_get_total_reaction_count_returns_zero_reactions(user, post, comment, reply):

    # Arrange
    expected_count = 0

    # Act
    total_recations_count = get_total_reaction_count()

    # Assert
    assert total_recations_count['count'] == expected_count


def test_get_reaction_metrics_with_invalid_post_id_raise_exception(post, post_reaction):

    # Arrange
    post_id = 10

    # Act

    # Assert
    with pytest.raises(InvalidPostException):
        get_reaction_metrics(post_id)


def test_get_reaction_metrics_with_valid_details_returns_count_for_each_reaction_type(post, post_reaction):

    # Arrange
    expected_post_id = 1
    expected_output = {'WOW': 1, 'LIT': 1, 'LOVE': 1}

    # Act
    count_for_each_reaction_type = get_reaction_metrics(expected_post_id)

    # Assert
    assert count_for_each_reaction_type == expected_output


def test_delete_post_with_invalid_user_id_raise_exception(user):

    # Arrange
    user_id = 10
    post_id = 3

    # Act

    # Assert
    with pytest.raises(InvalidUserException):
        delete_post(user_id, post_id)


def test_delete_post_with_invalid_post_id_raise_exception(post):

    # Arrange
    user_id = 1
    post_id = 10

    # Act

    # Assert
    with pytest.raises(InvalidPostException):
        delete_post(user_id, post_id)


def test_delete_post_when_given_user_id_is_not_the_creator_of_the_post_raise_exception(post):

    # Arrange
    user_id = 2
    post_id = 1

    # Act

    # Assert
    with pytest.raises(UserCannotDeletePostException):
        delete_post(user_id, post_id)


def test_delete_post_with_valid_details_delete_the_post(post):

    # Arrange
    user_id = 1
    post_id = 1
    # expected_output =

    # Act
    delete_post(user_id, post_id)

    # Assert
    assert Post.objects.filter(id=post_id).exists() is False
    assert Comment.objects.filter(post_id=post_id).exists() is False
    assert Reaction.objects.filter(post_id=post_id).exists() is False


def test_get_posts_with_more_positive_reactions():

    # Arrange
    POSITIVE_REACTIONS_LIST = [reaction.value for reaction in PositiveReactions]
    NEGATIVE_REACTIONS_LIST = [reaction.value for reaction in NegativeReactions]
    positive_reactions_count = Count(
        'reaction', filter=Q(reaction__reaction__in=POSITIVE_REACTIONS_LIST))
    negative_reactions_count = Count(
        'reaction', filter=Q(reaction__reaction__in=NEGATIVE_REACTIONS_LIST))
    expected_output = []

    # Act
    post_ids_list_with_more_positive_reactions = list(Post.objects.annotate(
        pos=positive_reactions_count, neg=negative_reactions_count).filter(
            pos__gt=F('neg')).values_list('id', flat=True))

    # Assert
    assert expected_output == post_ids_list_with_more_positive_reactions


# def get_posts_reacted_by_user(user_id):
def test_get_posts_reacted_by_user_with_invalid_user_id_raise_exception(user):

    # Arrange
    user_id = 10

    # Act

    # Assert
    with pytest.raises(InvalidUserException):
        get_posts_reacted_by_user(user_id)


def test_get_posts_reacted_by_user_with_valid_details_returns_post_ids(user, post_reaction):

    # Arrange
    user_id = 1
    expected_output = [3, 2, 1]

    # Act
    list_of_post_ids = get_posts_reacted_by_user(user_id)

    # Assert
    assert Counter(expected_output) == Counter(list_of_post_ids)


def test_get_reactions_to_post_with_invalid_post_id_raise_exception(post):

    # Arrange
    post_id = 10

    # Act

    # Assert
    with pytest.raises(InvalidPostException):
        get_reactions_to_post(post_id)


def test_get_reactions_to_post_with_valid_details_returns_list_of_dictionaries(post, post_reaction):

    # Arrange
    post_id = 1
    expected_output = [
        {'user_id': 1, 'name': 'user1', 'profile_pic': 'profile1', 'reaction': 'WOW'},
        {'user_id': 2, 'name': 'user2', 'profile_pic': 'profile2', 'reaction': 'LIT'},
        {'user_id': 3, 'name': 'user3', 'profile_pic': 'profile3', 'reaction': 'LOVE'}]

    # Act
    list_of_dictionaries = get_reactions_to_post(post_id)

    # Assert
    assert list_of_dictionaries == expected_output



def test_get_post_with_invalid_post_id_raise_exception(post):

    # Arrange
    post_id = 10

    # Act

    # Assert
    with pytest.raises(InvalidPostException):
        get_post(post_id)

@freeze_time('2020-04-18')
def test_get_post_with_valid_details_returns_post_details(snapshot):

    # Arrange
    post_id = 1
    UserFactory.create_batch(3)
    PostFactory.create_batch(3)
    CommentFactory.create_batch(3)
    CommentFactory.create_batch(3, is_parent_comment=True)
    ReactionFactory.create_batch(6, is_post_reaction=True)
    ReactionFactory.create_batch(6, is_comment_reaction=True)

    e ={
        'comments': [{'comment_content': 'comment1',
                      'comment_id': 1,
                      'commented_at': '2020-04-18 00:00:00',
                      'commenter': {'name': 'user1',
                                    'profile_pic': 'profile1',
                                    'user_id': 1},

                      'reactions': {'count': 1,
                                    'type': ['ANGRY']},

                      'replies': [{'comment_content': 'reply1',
                                   'comment_id': 5,
                                   'commented_at': '2020-04-18 00:00:00',

                                   'commenter': {'name': 'user1',
                                                 'profile_pic': 'profile1',
                                                 'user_id': 1},
                                   'reactions': {'count': 0,
                                                 'type': []}},

                                 {'comment_content': 'reply2',
                                  'comment_id': 6,
                                  'commented_at': '2020-04-18 00:00:00',

                                  'commenter': {'name': 'user2',
                                                'profile_pic': 'profile2',
                                                'user_id': 2},

                                  'reactions': {'count': 0,
                                                'type': []}}],
                     'replies_count': 2},

                    {'comment_content': 'comment2',
                     'comment_id': 2,
                     'commented_at': '2020-04-18 00:00:00',

                     'commenter': {'name': 'user2',
                                   'profile_pic': 'profile2',
                                   'user_id': 2},

                     'reactions': {'count': 1,
                                   'type': ['WOW']},

                     'replies': [{'comment_content': 'reply3',
                                  'comment_id': 7,
                                  'commented_at': '2020-04-18 00:00:00',

                                  'commenter': {'name': 'user3',
                                                'profile_pic': 'profile3',
                                                'user_id': 3},

                                  'reactions': {'count': 0,
                                                'type': []}},

                                 {'comment_content': 'reply4',
                                  'comment_id': 8,
                                  'commented_at': '2020-04-18 00:00:00',

                                  'commenter': {'name': 'user1',
                                                'profile_pic': 'profile1',
                                                'user_id': 1},

                                  'reactions': {'count': 0,
                                                'type': []}}],
                     'replies_count': 2}],
       'comments_count': 2,
       'post_content': 'post1',
       'post_id': 1,
       'posted_at': '2020-04-18 00:00:00',
       'posted_by': {'name': 'user1',
                     'profile_pic': 'profile1',
                     'user_id': 1},
       'reactions': {'count': 3,
                     'type': ['WOW',
                              'LIT',
                              'LOVE']},
    }

    # Act
    output = get_post(post_id=post_id)

    # Assert
    snapshot.assert_match(output, 'post_details')

def for_check_post_details(expected_output, output):

    assert expected_output['post_id'] == output['post_id']
    assert expected_output['posted_by'] == output['posted_by']
    assert expected_output['posted_at'] == output['posted_at']
    assert expected_output['post_content'] == output['post_content']
    assert expected_output['reactions'] == output['reactions']
    assert expected_output['reactions']['count'] == output['reactions']['count']
    assert expected_output['reactions']['type'] == output['reactions']['type']

def for_check_comment_details(expected_output, output,i):

    assert expected_output['comments'][i]['comment_id'] == output['comments'][i]['comment_id']
    assert expected_output['comments'][i]['comment_content'] == output['comments'][i]['comment_content']
    assert expected_output['comments'][i]['commented_at'] == output['comments'][i]['commented_at']
    assert expected_output['comments'][i]['commenter']['user_id'] == output['comments'][i]['commenter']['user_id']
    assert expected_output['comments'][i]['commenter']['name'] == output['comments'][i]['commenter']['name']
    assert expected_output['comments'][i]['commenter']['profile_pic'] == output['comments'][i]['commenter']['profile_pic']
    assert expected_output['comments'][i]['reactions']['count'] == output['comments'][i]['reactions']['count']
    assert expected_output['comments'][i]['reactions']['type'] == output['comments'][i]['reactions']['type']
    for_check_replies_details(expected_output, output, i, 0)
    for_check_replies_details(expected_output, output, i, 1)
    assert expected_output['comments'][i]['replies_count'] == output['comments'][i]['replies_count']

def for_check_replies_details(expected_output, output, i, j):

    assert expected_output['comments'][i]['replies'][j]['comment_id'] == output['comments'][i]['replies'][j]['comment_id']
    assert expected_output['comments'][i]['replies'][j]['comment_content'] == output['comments'][i]['replies'][j]['comment_content']
    assert expected_output['comments'][i]['replies'][j]['commented_at'] == output['comments'][i]['replies'][j]['commented_at']
    assert expected_output['comments'][i]['replies'][j]['commenter']['user_id'] == output['comments'][i]['replies'][j]['commenter']['user_id']
    assert expected_output['comments'][i]['replies'][j]['commenter']['name'] == output['comments'][i]['replies'][j]['commenter']['name']
    assert expected_output['comments'][i]['replies'][j]['commenter']['profile_pic'] == output['comments'][i]['replies'][j]['commenter']['profile_pic']
    assert expected_output['comments'][i]['replies'][j]['reactions']['count'] == output['comments'][i]['replies'][j]['reactions']['count']
    assert expected_output['comments'][i]['replies'][j]['reactions']['type'] == output['comments'][i]['replies'][j]['reactions']['type']


def test_get_post_when_no_comments_returns_post_details(post_reaction,
                                                          comment_reaction,
                                                          reply):

    # Arrange
    post_id = 5
    expected_output = {
        'comments': [],
        'comments_count': 0,
        'post_content': 'post5',
        'post_id': 5,
        'posted_at': '2020-04-18 00:00:00',
        'posted_by': {'name': 'user3',
                      'profile_pic': 'profile3',
                      'user_id': 3},
        'reactions': {'count': 0,
                      'type': []},
      }

    # Act
    output = get_post(post_id)

    # Assert
    assert expected_output == output
    for_check_post_details(expected_output, output)
    assert expected_output['comments'] == output['comments']
    assert expected_output['comments_count'] == output['comments_count']


def test_get_post_when_no_replies_returns_post_details(post_reaction,
                                                       comment_reaction,
                                                       reply):

    # Arrange
    post_id = 6
    expected_output = {
       'comments': [{'comment_content': 'comment5',
                     'comment_id': 4,
                     'commented_at': '2020-04-18 00:00:00',
                     'commenter': {'name': 'user7',
                                   'profile_pic': 'profile7',
                                   'user_id': 7},
                     'reactions': {'count': 0,
                                   'type': []},
                     'replies': [],
                     'replies_count': 0}],
       'comments_count': 1,
       'post_content': 'post6',
       'post_id': 6,
       'posted_at': '2020-04-18 00:00:00',
       'posted_by': {'name': 'user6',
                     'profile_pic': 'profile6',
                     'user_id': 6},
       'reactions': {'count': 0,
                     'type': []},
      }

    # Act
    output = get_post(post_id)

    # Assert
    assert expected_output == output
    for_check_post_details(expected_output, output)
    assert expected_output['comments'][0]['comment_id'] == output['comments'][0]['comment_id']
    assert expected_output['comments'][0]['comment_content'] == output['comments'][0]['comment_content']
    assert expected_output['comments'][0]['commented_at'] == output['comments'][0]['commented_at']
    assert expected_output['comments'][0]['commenter']['user_id'] == output['comments'][0]['commenter']['user_id']
    assert expected_output['comments'][0]['commenter']['name'] == output['comments'][0]['commenter']['name']
    assert expected_output['comments'][0]['commenter']['profile_pic'] == output['comments'][0]['commenter']['profile_pic']
    assert expected_output['comments'][0]['reactions']['count'] == output['comments'][0]['reactions']['count']
    assert expected_output['comments'][0]['reactions']['type'] == output['comments'][0]['reactions']['type']
    assert expected_output['comments'][0]['replies'] == output['comments'][0]['replies']
    assert expected_output['comments'][0]['replies_count'] == output['comments'][0]['replies_count']


def test_get_post_when_no_reactions_for_post_returns_post_details(post_reaction,
                                                                  comment_reaction,
                                                                  reply):

    # Arrange
    post_id = 6
    expected_output = {
       'comments': [{'comment_content': 'comment5',
                     'comment_id': 4,
                     'commented_at': '2020-04-18 00:00:00',
                     'commenter': {'name': 'user7',
                                   'profile_pic': 'profile7',
                                   'user_id': 7},
                     'reactions': {'count': 0,
                                   'type': []},
                     'replies': [],
                     'replies_count': 0}],
       'comments_count': 1,
       'post_content': 'post6',
       'post_id': 6,
       'posted_at': '2020-04-18 00:00:00',
       'posted_by': {'name': 'user6',
                     'profile_pic': 'profile6',
                     'user_id': 6},
       'reactions': {'count': 0,
                     'type': []},
      }

    # Act
    output = get_post(post_id)

    # Assert
    assert expected_output == output
    for_check_post_details(expected_output, output)
    assert expected_output['comments'][0]['comment_id'] == output['comments'][0]['comment_id']
    assert expected_output['comments'][0]['comment_content'] == output['comments'][0]['comment_content']
    assert expected_output['comments'][0]['commented_at'] == output['comments'][0]['commented_at']
    assert expected_output['comments'][0]['commenter']['user_id'] == output['comments'][0]['commenter']['user_id']
    assert expected_output['comments'][0]['commenter']['name'] == output['comments'][0]['commenter']['name']
    assert expected_output['comments'][0]['commenter']['profile_pic'] == output['comments'][0]['commenter']['profile_pic']
    assert expected_output['comments'][0]['reactions']['count'] == output['comments'][0]['reactions']['count']
    assert expected_output['comments'][0]['reactions']['type'] == output['comments'][0]['reactions']['type']
    assert expected_output['comments'][0]['replies'] == output['comments'][0]['replies']
    assert expected_output['comments'][0]['replies_count'] == output['comments'][0]['replies_count']


def test_get_post_when_no_reactions_for_comment_returns_post_details(post_reaction,
                                                                  comment_reaction,
                                                                  reply):

    # Arrange
    post_id = 6
    expected_output = {
       'comments': [{'comment_content': 'comment5',
                     'comment_id': 4,
                     'commented_at': '2020-04-18 00:00:00',
                     'commenter': {'name': 'user7',
                                   'profile_pic': 'profile7',
                                   'user_id': 7},
                     'reactions': {'count': 0,
                                   'type': []},
                     'replies': [],
                     'replies_count': 0}],
       'comments_count': 1,
       'post_content': 'post6',
       'post_id': 6,
       'posted_at': '2020-04-18 00:00:00',
       'posted_by': {'name': 'user6',
                     'profile_pic': 'profile6',
                     'user_id': 6},
       'reactions': {'count': 0,
                     'type': []},
      }

    # Act
    output = get_post(post_id)

    # Assert
    assert expected_output == output
    for_check_post_details(expected_output, output)
    assert expected_output['comments'][0]['comment_id'] == output['comments'][0]['comment_id']
    assert expected_output['comments'][0]['comment_content'] == output['comments'][0]['comment_content']
    assert expected_output['comments'][0]['commented_at'] == output['comments'][0]['commented_at']
    assert expected_output['comments'][0]['commenter']['user_id'] == output['comments'][0]['commenter']['user_id']
    assert expected_output['comments'][0]['commenter']['name'] == output['comments'][0]['commenter']['name']
    assert expected_output['comments'][0]['commenter']['profile_pic'] == output['comments'][0]['commenter']['profile_pic']
    assert expected_output['comments'][0]['reactions']['count'] == output['comments'][0]['reactions']['count']
    assert expected_output['comments'][0]['reactions']['type'] == output['comments'][0]['reactions']['type']
    assert expected_output['comments'][0]['replies'] == output['comments'][0]['replies']
    assert expected_output['comments'][0]['replies_count'] == output['comments'][0]['replies_count']


def test_get_user_posts_with_invalid_user_id_raise_exception(user):

    # Arrange
    user_id = 10

    # Act

    # Assert
    with pytest.raises(InvalidUserException):
        get_user_posts(user_id)


def test_get_user_posts_when_user_has_no_posts_returns_empty_list(post_reaction, comment_reaction, reply):

    # Arrange
    user_id = 8
    expected_output = []

    # Act
    output = get_user_posts(user_id)

    # Assert
    assert expected_output == output


def test_get_user_posts_with_valid_details_returns_list_of_posts(post_reaction, comment_reaction, reply):

    # Arrange
    user_id = 1
    expected_output = [
        {'comments': [{'comment_content': 'comment1',
                       'comment_id': 1,
                       'commented_at': '2020-04-18 00:00:00',

                       'commenter': {'name': 'user1',
                                     'profile_pic': 'profile1',
                                     'user_id': 1},

                       'reactions': {'count': 1,
                                     'type': ['ANGRY']},

                       'replies': [{'comment_content': 'reply1',
                                    'comment_id': 5,
                                    'commented_at': '2020-04-18 00:00:00',
                                    'commenter': {'name': 'user1',
                                                  'profile_pic': 'profile1',
                                                  'user_id': 1},
                                    'reactions': {'count': 0,
                                                  'type': []}},
                                   {'comment_content': 'reply2',
                                    'comment_id': 6,
                                    'commented_at': '2020-04-18 00:00:00',
                                    'commenter': {'name': 'user2',
                                                  'profile_pic': 'profile2',
                                                  'user_id': 2},
                                    'reactions': {'count': 0,
                                                  'type': []}}],
                       'replies_count': 2},
                      {'comment_content': 'comment2',
                       'comment_id': 2,
                       'commented_at': '2020-04-18 00:00:00',
                       'commenter': {'name': 'user2',
                                     'profile_pic': 'profile2',
                                     'user_id': 2},
                       'reactions': {'count': 1,
                                     'type': ['WOW']},
                       'replies': [{'comment_content': 'reply3',
                                    'comment_id': 7,
                                    'commented_at': '2020-04-18 00:00:00',
                                    'commenter': {'name': 'user3',
                                                  'profile_pic': 'profile3',
                                                  'user_id': 3},
                                    'reactions': {'count': 0,
                                                  'type': []}},
                                   {'comment_content': 'reply4',
                                    'comment_id': 8,
                                    'commented_at': '2020-04-18 00:00:00',
                                    'commenter': {'name': 'user1',
                                                  'profile_pic': 'profile1',
                                                  'user_id': 1},
                                    'reactions': {'count': 0,
                                                  'type': []}}],
                       'replies_count': 2}],
         'comments_count': 2,
         'post_content': 'post1',
         'post_id': 1,
         'posted_at': '2020-04-18 00:00:00',
         'posted_by': {'name': 'user1',
                       'profile_pic': 'profile1',
                       'user_id': 1},
         'reactions': {'count': 3,
                       'type': ['WOW',
                                'LIT',
                                'LOVE']}}
    ]


    # Act
    output = get_user_posts(user_id)

    # Assert
    assert expected_output == output
    for_check_post_details(expected_output[0], output[0])
    for_check_comment_details(expected_output[0], output[0],0)
    for_check_comment_details(expected_output[0], output[0],1)
    assert expected_output[0]['comments_count'] == output[0]['comments_count']


def test_get_replies_for_comment_with_invalid_comment_id_raise_exception(comment):

    # Arrange
    comment_id = 20

    # Act

    # Assert
    with pytest.raises(InvalidCommentException):
        get_replies_for_comment(comment_id)


def test_get_replies_for_comment_with_valid_details_returns_list_of_replies(comment, reply):

    # Arrange
    comment_id = 1
    expected_output = [
        {'comment_content': 'reply1',
         'comment_id': 5,
         'commented_at': '2020-04-18 00:00:00',
         'commenter': {'name': 'user1',
                       'profile_pic': 'profile1',
                       'user_id': 1}},
        {'comment_content': 'reply2',
         'comment_id': 6,
         'commented_at': '2020-04-18 00:00:00',
         'commenter': {'name': 'user2',
                       'profile_pic': 'profile2',
                       'user_id': 2}},
    ]


    # Act
    output = get_replies_for_comment(comment_id)

    # Assert
    assert expected_output == output
    check_reply_details_for_get_replies_for_comment(expected_output[0], output[0])
    check_reply_details_for_get_replies_for_comment(expected_output[1], output[1])

def check_reply_details_for_get_replies_for_comment(expected_output, output):
    assert expected_output['comment_id'] == output['comment_id']
    assert expected_output['comment_content'] == output['comment_content']
    assert expected_output['commented_at'] == output['commented_at']
    assert expected_output['commenter']['user_id'] == output['commenter']['user_id']
    assert expected_output['commenter']['name'] == output['commenter']['name']
    assert expected_output['commenter']['profile_pic'] == output['commenter']['profile_pic']
