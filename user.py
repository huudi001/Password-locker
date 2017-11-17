import random


class User:
    #a class variable to store users
    users =[]

    #initializing the instance variables
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password
     # method for creating new account#
    def log_in(self,user,word):
        for credential in Credential.user_credentials:
            if user ==credential.user_name  and word == credential.password:
                return True
            return False

     # saves accounts in the accounts list
    def save_user(self,user_n,p_word):
            saved_user = User.users.append(user_n,sp_word)
            return saved_user

    # method for displaying accounts
    @classmethod
    def display_users(cls):
        return cls.users
