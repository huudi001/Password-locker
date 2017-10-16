import random


class Credential:
    #initializing instance variables
    def __init__(self,firstname,lastname,email,password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
    # class variable that stores credential objects
    user_credentials = []

    #method that saves credentials to the list
    def save_credential(self):
        Credential.user_credentials.append(self)



    def new_password(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        pw_length = 8
        mPw = ""
        for i in range(pw_length):
            next_index = random.randrange(len(alphabet))
            mPw+= alphabet[next_index]
        return mPw


    @classmethod
    def credentials_exists(cls):
        for credential in cls.user_credentials:
            if credential.user_credentials:
                return True
        return False
