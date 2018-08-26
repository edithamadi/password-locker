class User:
    user_list = [] # Empty user list

def __init__(self,first_name,pass_word):

      # docstring removed for simplicity

        self.first_name = first_name
        self.pass_word = pass_word

def save_user(self):

        '''
        save_user method saves user objects into contact_list
        '''

        User.user_list.append(self)

def delete_user(self):
    '''
    delete_user method deletes a saved user from user_list
    '''
    User.user_list.remove(self)

@classmethod
def user_exists(cls,first_name):
        '''
        Method that checks if a user exists in the user_list.
        Args:
            username: Username to search if it exists
        Returns :
            Boolean: True or false depending on if the user exists or not
        '''
        for user in cls.user_list:
            if user.first_name == first_name:
                    return True

        return False  

@classmethod
def display_users(cls):
    '''
    method which returns user list
    '''

    return cls.user_list