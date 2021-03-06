# import pyperclip
import unittest # Importing the unittest module 
import pyperclip
from user import User,Credentials # Importing the user class
class TestUser(unittest.TestCase):
    
        def setUp(self):

                self.new_user = User("Edith","ADR5e") # create user object

        def tearDown(self):
                '''
                tearDown method which does clean up after each test has run.
                '''
                User.user_list = [] 

        def test_init(self):

                self.assertEqual(self.new_user.first_name,"Edith")

        def test_save_user(self):
        
                self.new_user.save_user() # saving the new contact
                self.assertEqual(len(User.user_list),1)
        
        def test_save_multiple_contact(self):
                '''
                test_save_multiple_contact to check if we can save multiple contact
                objects to our contact_list
                '''

                self.new_user.save_user()
                test_user = User("Test","AD5e")
                test_user.save_user()
                self.assertEqual(len(User.user_list),2)

        
        def test_user_exists(self):
                '''
                test to check whether a user exists or not.
                '''
                self.new_user.save_user()
                test_user = User("Test","AD5e") # new user created
                test_user.save_user()

                user_exists =User.user_exists("Test")

                self.assertTrue(user_exists)

        def test_find_user_by_username(self):
        '''
        test to check if we can find a user by username and display information
        '''
        
        self.new_user.save_user()
        test_user = User ("Test","AD5e") # new user
        test_user.save_user()

        found_user = User.find_by_username("Test")

        self.assertEqual(found_user.pass_word,test_user.pass_word)

class TestCredentials(unittest.TestCase):

        '''
        Test class that defines test cases for credentials class behaviours.
        Args:
        unittest.TestCase:TestCase class helping in creating test cases
        '''  
                                                                                                                                

        def setUp(self):
                """
                Set up method to run before each test case.
                """
                self.new_credentials = Credentials ("edithamadi","amadiey","JAS5e") #create user object

        def tearDown(self):
                """
                tearDown method that does the clean-up after each test has run
                """ 
                Credentials.credentials_list = []

        def test_init(self):
                """
                test_init test case to test if the object is initialized properly
                """
                self.assertEqual(self.new_credentials.account_name,"edithamadi")

        def test_save_credentials(self):
                """
                test to check if the credential object is saved on credential list
                """
                self.new_credentials.save_credentials() #save user
                self.assertEqual(len(Credentials.credentials_list),1)

        def test_save_multiple_credentials(self):
                """
                To check if we can save multiple objects into list
                """
                self.new_credentials.save_credentials()
                test_credentials = Credentials ("Github","Edith","JAS5e")
                test_credentials.save_credentials()
                self.assertEqual(len(Credentials.credentials_list),2)


        def test_delete_credentials(self):
                '''
                tests if we can delete a credential from our credentials list
                '''  
                self.new_credentials.save_credentials()
                test_credentials = Credentials("Github","edithamadi","JAS5e")
                test_credentials.save_credentials()

                self.new_credentials.delete_credentials() #deletes credentials object
                self.assertEqual (len(Credentials.credentials_list),1)

        def test_find_credentials_by_account_name(self):
                '''
                to check if we can find a credential by the account name and display more information about it
                '''  
                self.new_credentials.save_credentials()
                test_credentials = Credentials("Github","edithamadi","JAS5e")
                test_credentials.save_credentials()

                found_credentials = Credentials.find_by_account_name("Github")
                self.assertEqual(found_credentials.password,test_credentials.password)

        def test_credentials_exists(self):
                '''
                checks if we can return a boolean if we cannot find the credentials
                '''  

                self.new_credentials.save_credentials()
                test_credentials = Credentials("Github","edithamadi","JAS5e")
                test_credentials.save_credentials()

                credentials_exists =Credentials.credentials_exist("Github")
                self.assertTrue(credentials_exists)

        def test_display_all_credentials(self):
                '''
                returns a list of all credentials saved 
                '''  

                self.assertEqual( Credentials.display_all_credentials(),Credentials.credentials_list)

if __name__ == '__main__':
        unittest.main()

