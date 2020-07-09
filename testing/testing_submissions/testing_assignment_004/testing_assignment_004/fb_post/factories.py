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
    posted_by = factory.Iterator(User.objects.all())


class CommentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Comment

    content = factory.Sequence(lambda n: 'comment_content_%d' %n)
    commented_at = factory.LazyFunction(datetime.datetime.now)
    commented_by = factory.Iterator(User.objects.all())
    post = factory.Iterator(Post.objects.all())
    parent_comment = None

    class Params:
        is_parent_comment = factory.Trait(
            parent_comment = factory.Iterator(Comment.objects.all())
        )


class ReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reaction

    reacted_by = factory.Iterator(User.objects.all())
    reacted_at = factory.LazyFunction(datetime.datetime.now)
    reaction = factory.Iterator(['LIKE', 'HAHA', 'WOW', 'THUMBS-UP', 'THUMBS-DOWN'])
    post = None
    comment = None


    class Params:
        is_post_reaction = factory.Trait(
            post = factory.Iterator(Post.objects.all())
        )
        is_comment_reaction = factory.Trait(
            comment = factory.Iterator(Comment.objects.all())
        )


# class GetPostFactory:
#     UserFactory.create_batch(3)
#     PostFactory.create_batch(3)
#     CommentFactory.create_batch(3)
#     CommentFactory.create_batch(3, is_parent_comment=True)
#     ReactionFactory.create_batch(6, is_post_reaction=True)
#     ReactionFactory.create_batch(6, is_comment_reaction=True)
