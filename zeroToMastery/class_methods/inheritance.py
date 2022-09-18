class SocialMedia():
    def user_sign_in(self, name, media):
        print(f'Welcome {name} Your {media} Account activated Successfully.')


class FaceBook(SocialMedia):
    def __init__(self):
        self.media = 'Facebook'
        self.User_name = input('Enter How we should call you:')
        self.user_sign_in(self.User_name, self.media)


class Twitter(SocialMedia):
    def __init__(self):
        self.media = 'Twitter'
        self.User_name = input('Enter How we should call you:')
        self.user_sign_in(self.User_name, self.media)
        self.verification()

    def verification(self):
        print(
            f'Your account will be activated shortly after a verification {self.User_name}')


class Instagram(SocialMedia):
    def __init__(self):
        self.media = 'Instagram'
        self.User_name = input('Enter How we should call you:')
        self.user_sign_in(self.User_name, self.media)


instagram = Instagram()
# facebook = FaceBook()
# twitter = Twitter()

print(isinstance(instagram, Instagram))
