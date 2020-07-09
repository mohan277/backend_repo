import factory
from .objects import *


class UserFactory(factory.Factory):
    class Meta:
        model = User

    firstname = factory.Sequence(lambda f_name: '%s' %f_name)
    lastname = factory.Sequence(lambda l_name: '%s' %l_name)
    username = factory.LazyAttribute(lambda obj: '%s%s' %(obj.firstname,obj.lastname))
    email = factory.LazyAttribute(lambda obj: '%s@gmail.com' %obj.username)
