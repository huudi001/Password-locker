import random
import pyperclip

class User:
    #a class variable to store user_accounts
    users =[]

    #initializing the instance variables
    def __init__(self,user_name, password):
        self.user_name = user_name
        self.password = password

     #method that saves accounts
    def save_user(self):
        User.users.append(self)


    @classmethod
    def user_exists(cls,word):
        for user in cls.users:
            if user.password == word:
                return True
        return False





    #generating a new password

    def new_password(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        pw_length = 8
        mypw = ""
        for i in range(pw_length):
            next_index = random.randrange(len(alphabet))
            mypw = mypw + alphabet[next_index]
        return mypw
