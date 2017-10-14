from user import User
import unittest

class Password_test(unittest.TestCase):
    def setUp(self):
        self.new_user = User("khalid","Groovy50")
    def tearDown(self):
        User.users = []


    def test_init(self):
        self.assertEqual(self.new_user.user_name,"khalid")
        self.assertEqual(self.new_user.password,"Groovy50")

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Test","user") # new user
        test_user.save_user()

        user_exists = User.user_exist("abuuanas30@hotmail.com")

        self.assertTrue(user_exists)



    def test_save_multiple_users(self):
        self.new_user.save_user()
        test_user = User("Test","groovy50")
        test_user.save_user()
        self.assertEqual(len(User.users),2)

    def test_user_exists(self):
        self.new_user.save_user()
        test_user = User("Test","user",) # new contact
        test_user.save_user()

        user_exist = User.user_exists("Groovy50")

        self.assertTrue(user_exist)





if __name__ == '__main__':
    unittest.main()
