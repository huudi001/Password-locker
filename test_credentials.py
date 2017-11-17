from credentials import Credential
import unittest

class Credential_test(unittest.TestCase):
    def setUp(self):
        self.new_account = Credential("huudi001","khalid","hashi,""abuuanas30@hotmail.com","Shirwadheere50")
    def tearDown(self):
        Credential.user_credentials = []

    def test_init(self):
        self.assertEqual(self.new_account.user_name,"huudi001")
        self.assertEqual(self.new_account.firstname,"khalid")
        self.assertEqual(self.new_account.lastname,"hashi")
        self.assertEqual(self.new_account.email,"abuuanas30@hotmail.com")
        self.assertEqual(self.new_account.password,"Shirwadheere50")

    def test_save_new_account(self):
        self.new_credentials.save_account() # saving the new contact
        self.assertEqual(len(Credential.user_credentials),1)

     def test_delete_account(self):

            self.new_account.save_account()
            test_account = Credential("Test","user","second_user","test@user.com","Groovy50") # new contact
            test_account.save_account()

            self.new_account.delete_acount()# Deleting a contact object
            self.assertEqual(len(Credential.user_credentials),1)
    def test_display_all_accounts(self):

        self.assertEqual(Credential.display_accounts(),Credential.user_credentials)







if __name__ == '__main__':
    unittest.main()
