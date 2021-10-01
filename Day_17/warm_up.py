import os


class User:  # You can have the '()' but you don't need it since you are not inheriting anything.
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.user_name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Daniel")
user_2 = User("002", "John")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
