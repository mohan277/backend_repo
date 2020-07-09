import datetime
import factory, factory.django
from .models import *

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Sequence(lambda n: 'user%d' %n)
    profile_pic = factory.Sequence(lambda n: 'profile_pic%d' %n)


class PostFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Post

    content = factory.Sequence(lambda n: 'post_content_%d' %n)
    posted_at = factory.LazyFunction(datetime.datetime.now)
    posted_by = factory.SubFactory(UserFactory)


class CommentFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = Comment

    content = factory.Sequence(lambda n: 'comment_content_%d' %n)
    commented_at = factory.LazyFunction(datetime.datetime.now)
    commented_by = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    parent_comment = None

    class Params:
        is_parent_comment = factory.Trait(
            parent_comment=factory.SubFactory('.CommentFactory'))


class ReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reaction

    reacted_by = factory.SubFactory(UserFactory)
    reacted_at = factory.LazyFunction(datetime.datetime.now)
    reaction = factory.Iterator(['LIKE', 'HAHA', 'WOW', 'THUMBS-UP', 'THUMBS-DOWN'])
    post = None
    comment = None


    class Params:
        is_post_reaction = factory.Trait(
            post = factory.SubFactory(PostFactory)
        )
        is_comment_reaction = factory.Trait(
            comment = factory.SubFactory(CommentFactory)
        )

class ReplyFactory(factory.django.DjangoModelFactory):
