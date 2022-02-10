# creating class and methods
class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 1000
        self.following = 0
        print(f"Check {user_id}\t{user_name}\n")

    def Follow(self, user):
        user.followers += 1
        print(user.followers)


user_1 = User("one", "Stark")
user_2 = User("two", "Rodey")

user_1.Follow(user_2)
print(user_1.followers)


class Racer:
    def race(self):
        print("Race Starts at an flash of light")


stark = Racer()
stark.race()
