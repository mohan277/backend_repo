# class User:
#     def __init__(self, firstname: str, lastname: str):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.username = lastname+firstname
#         self.email = self.username+'@gmail.com'

#     def __repr__(self):
#         return '%s (%s)' %(self.username, self.email)



# import factory
# class UserFactory(factory.Factory):
#     class Meta:
#         model = User

#     firstname = factory.Sequence(lambda f_name: '%s' %f_name)
#     lastname = factory.Sequence(lambda l_name: '%s' %l_name)


# class Account:
#     def __init__(self, username, email, date_joined):
#         self.username = username
#         self.email = email
#         self.date_joined = date_joined

#     def __repr__(self):
#         return '%s (%s)' % (self.username, self.email)


# class Profile:

#     GENDER_MALE = 'm'
#     GENDER_FEMALE = 'f'
#     GENDER_UNKNOWN = 'u'  # If the user refused to give it

#     def __init__(self, account, gender, firstname, lastname, planet='Earth'):
#         self.account = account
#         self.gender = gender
#         self.firstname = firstname
#         self.lastname = lastname
#         self.planet = planet

#     def __repr__(self):
#         return '%s %s (%s)' % (
#             self.firstname,
#             self.lastname,
#             self.account.username,
#         )


# import datetime
# import random
# class AccountFactory(factory.Factory):
#     class Meta:
#         model = Account

#     username = factory.Sequence(lambda n: '%s' % n)
#     email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)
#     date_joined = factory.LazyFunction(datetime.datetime.now)


# class ProfileFactory(factory.Factory):
#     class Meta:
#         model = Profile

#     account = factory.SubFactory(AccountFactory)
#     gender = factory.Iterator([Profile.GENDER_MALE, Profile.GENDER_FEMALE])
#     firstname = factory.Sequence(lambda f_name: '%s' %f_name)
#     lastname = factory.Sequence(lambda l_name: '%s' %l_name)
#     # firstname = u'John'
#     # lastname = u'Doe'


# def make_objects():
#     ProfileFactory.create_batch(size=0)

#     # Let's create a few, known objects.
#     list = [ProfileFactory(
#         gender=Profile.GENDER_MALE,
#         firstname='Luke',
#         lastname='Skywalker',
#         planet='Tatooine',
#     ),

#      ProfileFactory(
#         gender=Profile.GENDER_FEMALE,
#         firstname='Leia',
#         lastname='Organa',
#         planet='Alderaan',
#     ),
#     ProfileFactory(
#         gender=Profile.GENDER_MALE,
#         firstname='Luke',
#         lastname='Skywalker',
#         planet='Tatooine',
#     ),

#      ProfileFactory(
#         gender=Profile.GENDER_FEMALE,
#         firstname='Leia',
#         lastname='Organa',
#         planet='Alderaan',
#     ),
#     ProfileFactory(
#         gender=Profile.GENDER_MALE,
#         firstname='Luke',
#         lastname='Skywalker',
#         planet='Tatooine',
#     ),

#      ProfileFactory(
#         gender=Profile.GENDER_FEMALE,
#         firstname='Leia',
#         lastname='Organa',
#         planet='Alderaan',
#     ),
#     ProfileFactory(
#         gender=Profile.GENDER_MALE,
#         firstname='Luke',
#         lastname='Skywalker',
#         planet='Tatooine',
#     ),

#      ProfileFactory(
#         gender=Profile.GENDER_FEMALE,
#         firstname='Leia',
#         lastname='Organa',
#         planet='Alderaan',
#     ),
#     ProfileFactory(
#         gender=Profile.GENDER_MALE,
#         firstname='Luke',
#         lastname='Skywalker',
#         planet='Tatooine',
#     ),

#      ProfileFactory(
#         gender=Profile.GENDER_FEMALE,
#         firstname='Leia',
#         lastname='Organa',
#         planet='Alderaan',
#     )]
#     return list


