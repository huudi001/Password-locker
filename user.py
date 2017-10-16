import random
from credentials import Credential

class User:
    #a class variable to store users
    accounts =[]

    #initializing the instance variables
    def __init__(self,firstname,lastname,email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = pasword

    def creating_new_account(self):
        new_account = User("khalid","hassan","abuuanas30@hotmail.com","Shirwadheere50")
        return new_account

    @classmethod
    def account_exists(cls,word):
        for account in cls.accounts:
            if account.password == word:
                return True
        return False

    def save_account(self):
            User.accounts.append(self)


    def save_account_passwords(account):
        if User.account_exists(account):
            for account in User.accounts.password:
                account.accounts.append(password)
            return account
        else:
            return "acount dosent exist"

    def delete_account(self):
        User.accounts.remove(self)
    # method for displaying accounts
    @classmethod
    def display_accounts(cls):
        return cls.accounts


    @classmethod
    def find_account_by_password(cls,word):

        for account in cls.accounts:
            if account.password == word:
                return account
            return "invalid"

    @classmethod
    def save_account_passwords(cls,account):
        if User.account_exists(account):
            for account in cls.User.accounts.password:

                account.accounts.append(password)
            return account
        else:
            return "account dosent exist"
