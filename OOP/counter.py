class User:
    counter = 0
    def __init__(self, name):
        self.name = name
        type(self).counter += 1
    def get_counter(self):
        print(User.counter)

user_object = User("New User")
user_object.get_counter()