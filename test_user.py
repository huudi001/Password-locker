from user import User
import unittest

class Password_test(unittest.TestCase):
    def setUp(self):
        self.new_account = User("abuuanas30@hotmail.com","Groovy50")
    def tearDown(self):
        User.accounts = []


    def test_init(self):
        self.assertEqual(self.new_account.email,"abuuanas30@hotmail.com")
        self.assertEqual(self.new_account.password,"Groovy50")

    def save_account(self):



        User.accounts.append(self)

    def test_user_exists(self):

        #test to check if we can return a Boolean  if we cannot find the user.


        self.new_account.save_account()
        test_account= User("Test","user") # new user
        test_account.save_account()

        account_exists = User.account_exists("abuuanas30@hotmail.com")

        self.assertFalse(account_exists)



    def test_save_multiple_accounts(self):
        self.new_account.save_account()
        test_account = User("Test","groovy50")
        test_account.save_account()
        self.assertEqual(len(User.accounts),2)

    def test_delete_account(self):

            #test_delete_user to test if we can remove a user from  user list

            self.new_account.save_account()
            test_account = User("Test","user") # new contact
            test_account.save_account()

            self.new_account.delete_account()# Deleting a contact object
            self.assertEqual(len(User.accounts),1)

    def test_find_contact_by_password(self):


        self.new_account.save_account()
        test_account = User("abuuanas30@hotmail.com","Groovy50")
        test_account.save_account()

        found_account = User.find_account_by_password("Groovy50")

        self.assertEqual(found_account.password,test_account.password)






if __name__ == '__main__':
    unittest.main()
