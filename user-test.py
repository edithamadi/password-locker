import pyperclip
import unittest # Importing the unittest module 
from user import User # Importing the user class
class TestUser(unittest.TestCase):
    
    def setUp(self):

        self.new_user = User("Edith","ADR5e") # create user object


def test_init(self):

        self.assertEqual(self.new_user.first_name,"Edith")
        self.assertEqual(self.new_pass_word.pass_word,"ADR5e")

def test_save_user(self):
       
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)
 

def tearDown(self):
        '''
        tearDown method which does clean up after each test has run.
        '''
        User.user_list = [] 


def test_save_multiple_contact(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''

            self.new_user.save_user()
            test_user = User("Test","AD5e")
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

def test_delete_user(self):
        '''
        test_delete_user to test if it's possible to remove a user from user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","AD5e") #added user
        test_user.save_user()

        self.new_user.delete_user() #deletes user object
        self.assertEqual(len(User.user_list),1)

def test_user_exists(self):
        '''
        test to check whether a user exists or not.
        '''
        self.new_user.save_user()
        test_user = User("Test","gL1998") # new user created
        test_user.save_user()

        user_exists =User.user_exists("Test")

        self.assertTrue(user_exists)

def test_display_users(self):
        '''
        method that returns a list of all users saved in the user_list
        '''

        self.assertEqual( User.display_users(),User.user_list)

        
if __name__ == '__main__':
    unittest.main()