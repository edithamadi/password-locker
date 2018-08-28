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

    

    def delete_credentials(self):
        '''
        deletes a saved credential from credentials_list
        '''

        Credentials.credentials_list.remove(self)

    @classmethod
    def display_all_credentials(cls):
        '''
        method that returns a list of all credentials saved
        '''

        return cls.credentials_list

    @classmethod
    def find_by_account_name(cls,account_name):
        '''
        method that takes in the account name and returns a credential that matches that account name
        Args:
        account_name:Account name to search for 
        Returns:
        Credentials of person that matches the account name
        '''  

        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials


    @classmethod
    def credentials_exist(cls,account_name):
        '''
        checks if a credential exists in the credentials list.
        Args:
            account_name:Account name to search if it exists
        Returns:
            Boolean:True or false depending on if the credential exists    
        '''      
        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return True

            return False  

