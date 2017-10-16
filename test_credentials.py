from credentials import Credential
import unittest

class Credential_test(unittest.TestCase):
    def setUp(self):
        self.new_credentials = Credential("khalid","Hassan","abuuanas30@hotmail.com","Shirwadheere50")
    def tearDown(self):
        Credential.user_credentials = []

    def test_init(self):
        self.assertEqual(self.new_credentials.firstname,"khalid")
        self.assertEqual(self.new_credentials.lastname,"Hassan")
        self.assertEqual(self.new_credentials.email,"abuuanas30@hotmail.com")
        self.assertEqual(self.new_credentials.password,"Shirwadheere50")

    def test_save_credential(self):
        self.new_credentials.save_credential() # saving the new contact
        self.assertEqual(len(Credential.user_credentials),1)




if __name__ == '__main__':
    unittest.main()
