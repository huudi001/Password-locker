import random



class Credential:
    #initializing instance variables
    def __init__(self,user_name,first_name,last_name,email,password):
        self.firstname = first_name
        self.lastname = last_name
        self.email = email
        self.password = password
        self.user_name = user_name
    # class variable that stores credential objects
    user_credentials = []

    #method that saves credentials to the list
    def register(self):
        new_account = self.Credential(user_name,first_name,last_name,email,password)
        return new_account

    def save_credentials(self):
        self.user_credentials.append(self)

    @classmethod
    def display_credentials(cls):

        return cls.user_credentials




    # creating new password
    def create_new_password(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        mPw = ""
        p_word_lenght = 8
        for i in range(p_word_lenght):
            next_index = random.randrange(len(alphabet))
            mPw+= alphabet[next_index]
        return mPw
