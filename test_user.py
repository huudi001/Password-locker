from user import User
import unittest

class Password_test(unittest.TestCase):
    def setUp(self):
        self.new_user = User("huudi001","Shirwadheere50")
    def tearDown(self):
        User.users = []


    def test_init(self):
        self.assertEqual(self."user_name","huudi01")
        self.assertEqual(self.password,"Shirwadheere")

    def test_save_user(self):
        User.accounts.append(self)


    def test_delete_user(self):

            #test_delete_user to test if we can remove a user from  user list

            self.new_user.user()
            test_user = User("Test","user")
            test_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(User.users),1)

    def test_find_user_by_password(self):


        self.new_user.save_user()
        test_user = User("huudi001","Shirwadheere50")
        test_user.save_user()

        found_user = User.find_user_by_password("Shirwadheere")

        self.assertEqual(found_user.password,test_user.password)

    def test_display_users(self):



   def test_save_user_password(self)











if __name__ == '__main__':
    unittest.main()
