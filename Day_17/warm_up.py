import os


class User():
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.user_name = username
        self.followers = 0


user_1 = User("001", "Daniel")

print(user_1.user_name)
