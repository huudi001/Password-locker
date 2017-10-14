import random
import pyperclip

class User(object):
    #a class variable to store user_accounts
    users =[]

    #initializing the instance variables
    def __init__(self,account, password):
        self.account = account
        self.password = password

     #method that saves accounts
    def create_account(self):
        self.new_account = User(facebook,groovy50)
        self.save_account()
        return new_account


    @classmethod
    def account_exists(cls,word,accoun):
        for user in cls.users:
            if user.password == word and user.account ==accoun:
                return True
        return False

    def save_account(self):
        self.User.users.append(self)




class Credential(User):
    def __init__(self,credentials):
        self.credentials = credentials
    User.__init__(self,account,password)

    self.credential = []

    def save_credentials(self):
        Credential.create_account().credential.append(self)

    def new_password(self,password):
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        pw_length = 8
        for i in range(pw_length):
            next_index = random.randrange(len(alphabet))
            password+= alphabet[next_index]
        return password

    def save_password(self,password):
        Credential.new_pasword(password).credential.append(self)

    @classmethod
    def display_credential(cls)
        return cls.credential
