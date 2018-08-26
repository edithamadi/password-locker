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
def find_by_first_username(cls,first_name):
        '''
        Method that takes in a first_name and returns a user that matched that first_name.
        Args:
            first_name: first_name to search for
        Returns:
             user  that matched the first_name
        '''

        for user in cls.user_list:
            if user.first_name == first_name:
                return user