# from django.contrib.auth.models import AbstractUser
# from django.db import models
# import factory, factory.django

# # models.py
# class User(models.Model):
#     name = models.CharField(max_length=100)

# class Group(models.Model):
#     name = models.CharField(max_length=100)
#     members = models.ManyToManyField(User, through='GroupLevel')

# class GroupLevel(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     rank = models.IntegerField()


# # factories.py
# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = User

#     name = "John Doe"

# class GroupFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Group

#     name = "Admins"

# class GroupLevelFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = GroupLevel

#     user = factory.SubFactory(UserFactory)
#     group = factory.SubFactory(GroupFactory)
#     rank = 1

# class UserWithGroupFactory(UserFactory):
#     membership = factory.RelatedFactory(GroupLevelFactory, 'user')

# class UserWith2GroupsFactory(UserFactory):
#     membership1 = factory.RelatedFactory(GroupLevelFactory, 'user', group__name='Group1')
#     membership2 = factory.RelatedFactory(GroupLevelFactory, 'user', group__name='Group2')





# # models.py
# class Country(models.Model):
#     name = models.CharField(max_length=100)
#     lang = models.CharField(max_length=100)

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     lang = models.CharField(max_length=100)
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)

# class Company(models.Model):
#     name = models.CharField(max_length=100)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)



# # factories.py
# class CountryFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Country

#     name = factory.Iterator(["France", "Italy", "Spain"])
#     lang = factory.Iterator(['fr', 'it', 'es'])

# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = User

#     name = "John"
#     lang = factory.SelfAttribute('country.lang')
#     country = factory.SubFactory(CountryFactory)

# class CompanyFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Company

#     name = "ACME, Inc."
#     country = factory.SubFactory(CountryFactory)
#     owner = factory.SubFactory(UserFactory, country=factory.SelfAttribute('...country'))


# # models.py
# class User(models.Model):
#     name = models.CharField(max_length=100)

# class Post(models.Model):
#     name = models.CharField(max_length=100)
#     title = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

# # factories.py
# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = User

#     name = "Hareesh"

# class PostFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Post

#     name = "Post"
#     title = "jagadadeesh"
#     user = factory.SubFactory(UserFactory, name=factory.LazyAttribute(lambda obj: obj.factory_parent.title))



# from django.contrib.auth.models import AbstractUser
# from django.db import models


# class User(models.Model):
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)


# class AccountFactory(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     date_joined = models.DateTimeField(auto_now=True)


# class Profile(models.Model):
#     account = models.ForeignKey(User, on_delete=models.CASCADE)
#     gender = models.CharField(max_length=10)
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)





from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50)
    profile_pic = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" % (self.name, self.profile_pic)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='posts')
    posted_at = models.DateTimeField(auto_now=True)
    post_content = models.CharField(max_length=250)

    def __str__(self):
        return "%s %s" % (self.user, self.post_content)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments', default=None, null=True)
    comment_content = models.CharField(max_length=250)
    commented_at = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE,
                                       default=None, null=True,
                                       related_name='comments')


from django.db import models
from fb_post_v2.constants.enums import ReactionType


class Reactions(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,
                                default=None, null=True,
                                related_name='reactions')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None,
                             null=True, related_name='reactions')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='reactions')
    Reaction_Choice = (
        (ReactionType.LIKE.value, ReactionType.LIKE.value),
        (ReactionType.WOW.value, ReactionType.WOW.value),
        (ReactionType.HAHA.value, ReactionType.HAHA.value),
        (ReactionType.DISLIKE.value, ReactionType.DISLIKE.value),
        (ReactionType.SAD.value, ReactionType.SAD.value),
        (ReactionType.ANGRY.value, ReactionType.ANGRY.value)
    )
    reaction_type = models.CharField(max_length=10, choices=Reaction_Choice,
                                     default=None, null=True)

    def __str__(self):
        return self.reaction_type



class UserFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'user%d' %n)
    profile_pic = factory.Sequence(lambda n: 'profile_pic%d' %n)


class PostFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Post

    user = factory.SubFactory(UserFactory)
    posted_at = factory.LazyFunction(datetime.datetime.now)
    post_content = factory.Sequence(lambda n: 'post_content_%d' %n)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    comment_content = factory.Sequence(lambda n: 'comment_content_%d' %n)
    commented_at = factory.LazyFunction(datetime.datetime.now)
    parent_comment = None

    class Params:
        is_parent_comment = factory.Trait(
            parent_comment=factory.SubFactory('.CommentFactory'))


class ReactionsFactory():
    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    comment = factory.SubFactory(CommentFactory)
    reaction_type = factory.Iterator(['LIKE', 'HAHA', 'WOW', 'THUMBS-UP', 'THUMBS-DOWN'])
