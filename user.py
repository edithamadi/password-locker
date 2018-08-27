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

class Credentials:
    """
    Class that generates new instances of user's credential
    """

    credentials_list = [] #Empty credentials list 

    def __init__(self,account_name,login_name,password):
        """
        __init__ method that defines properties for our objects
        Args:
            account_name: New credential acc_name.
            login_name: New credential login_name.
            password: New credential pword.
        """

        self.account_name = account_name
        self.login_name = login_name
        self.password = password

    def save_credentials(self):

    '''
    save_credentials method that saves credentials object into credentials_list
       '''

    Credentials.credentials_list.append(self)