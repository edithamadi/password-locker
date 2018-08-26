import unittest # Importing the unittest module 
from user import User # Importing the user class
class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Edith","Amadi","ADR5e") # create user object


def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Edith")
        self.assertEqual(self.new_user.last_name,"Amadi")
        self.assertEqual(self.new_pass_word.pass_word,"ADR5e")

def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)

        
if __name__ == '__main__':
    unittest.main()