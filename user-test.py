import unittest # Importing the unittest module 
from user import User # Importing the user class
class TestUser(unittest.TestCase):
    
def setUp(self):

        self.new_user = User("Edith","Amadi","ADR5e") # create user object


def test_init(self):

        self.assertEqual(self.new_user.first_name,"Edith")
        self.assertEqual(self.new_user.last_name,"Amadi")
        self.assertEqual(self.new_pass_word.pass_word,"ADR5e")

def test_save_user(self):
       
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)
 
        
if __name__ == '__main__':
    unittest.main()