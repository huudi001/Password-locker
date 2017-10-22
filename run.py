#!/usr/bin/env python3.5

from user import User
from credentials import Credential

def new_registration(user_name,firstname,lastname,email,password):
    new_r = Credential(user_name,firstname,lastname,email,password)
    return new_r








def loged(user_name,word):
    user = User(user_name,word)
    return user


def New_Password(new_pass):
    new_p_word = Credential.create_new_password(new_pass)
    return new_p_word


def save_user(user_name,password):

    saved_user=  User.save_user(user_name,password)
    return saved_user

def saving_credentials(credential):
    c = Credential.save_credentials(credential)
    return c


def display_credential(acouunt):
    credentials = Credential.display_credentials(account)
    return credentials


def main():
    print("Hello Welcome to passwordlocker. What is your name?")
    user_name = input()
    print("Hello", user_name, "please choose from the list of of short_code to use this app")
    print('\n')
    while True:
        print("enter NR to register for new account, enter Lg to log in with your existing credentials, enter np to create a new password", "enter ex to exit, enter DC to display credentials")
        short_code = input().lower()
        if short_code == 'nr':
            print("New Registration")
            print("-"*10)
            print ("user_name ....")
            u_name = input()

            print("first_ name ...")
            f_name = input()

            print("last_name ...")
            l_name = input()

            print("email ...")
            e_m = input()
            print("password ...")
            p_w = input()
            new_registration(u_name,f_name,l_name,e_m,p_w)
            saving_credentials(new_registration(u_name,f_name,l_name,e_m,p_w))
            ('\n')
            print ('\n')
            print("your registration has been created")
        elif short_code == "lg":

            print("to log in enter your user name and password")
            ('\n')
            print("enter your user name")
            user_name = input()
            ('\n')
            print("enter your password")
            password = input()
            loger = loged(user_name,password)
            ('\n')
            print("your are now loged in")
        elif short_code == "np":
            print("enter new password")
            new_pas= input()
            print("your new password is : "+ New_Password(new_pas))
            ('\n')

            ('\n')
        elif short_code == "dc":
            print("displaying credentials")




        else:
            short_code == 'ex'
            break
            print("BYE")





if __name__ == '__main__':

    main()
