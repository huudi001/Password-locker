#!/usr/bin/env python3.5

from user import User
from credentials import Credential

def create_account(firstname,lastname,email,password):
    new_account= Credential(firstname,lastname,email,password)
    return new_account

def Password(new_pass):
    return Credential.new_password(new_pass)


def save_accounts(acount):

    return User.save_account(acount)

def new_password_for_new_account(account):
    return User.save_account_passwords(account)

def display_accounts():
    return User.display_accounts()

def find_contact(password):
    return User.find_account_by_password(password)


def main():
    print("Hello Welcome to your account-list. What is your name?")
    user_name = input()
    print("Hello", user_name, "what would you like to do?")
    print('\n')
    while True:
        print("Use these short codes : ca- create a new account, gp - generate password, svap -save account passwords,sa - save account, dpa - display accounts, ex -exit the account list ")
        short_code = input().lower()
        if short_code == 'ac':
            print("New Account")
            print("-"*10)
            print ("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Email address ...")
            e_address = input()

            print("Password ...")
            p_word = input

            save_accounts(create_account(f_name,l_name,e_addres,p_word))

            print ('\n')
            print("New account" "created")
            print ('\n')
        elif short_code == 'da':
             display_accounts()
             print("Here is a list of all your accounts")
             print('\n')
            

            else:
                print("you dont have any accounts saved")

        elif short_code == 'gp':
            print ("enter a pasword")
            new_pass = input()
            Password(new_pass)
            print("new password is", new_pass)

        elif short_code == 'svap':
            print("enter account you want to make a new pasword")
            account = input()
            new_password_for_new_account(account)
            print ("your account is succesfully saved")

        elif short_code == "ex":

            print("Bye .......")
            break
    else:
        print("please use the short code")



if __name__ == '__main__':

    main()
