import string
import random
from random import choice

from user import User
from user import Credentials  #importing the user class

def create_user(first_name,pass_word): #created the function create_user

    new_user = User(first_name,pass_word) #created new user object and return it
    return new_user

def save_users(user): # created function

    user.save_user() #function calls method to save the user


def find_user(first_name):

    return User.find_by_username(first_name) 

def check_existing_users(first_name):

    return User.user_exists(first_name)

def create_credentials(account_name,login_name,pass_word): #created the function create_user
    '''
    Function to create a new user
    '''

    new_credentials = Credentials(account_name,login_name,pass_word) #created new user object and return it
    return new_credentials

def save_credentials(credential): # created function
    '''
    function to save credentials
    '''
    Credentials.save_credentials
    Credentials.save_credentials(credential) #function calls method to save the credential

def del_credentials(credential):
    '''
    function to delete a credential
    '''
    Credentials.delete_credentials(credential)

def find_credentials(first_name):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Credentials.find_by_account_name(first_name) 

def check_existing_credentials(first_name):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Credentials.credentials_exist(first_name)

def display_credentials():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_all_users()

def main():
    print("Hello Welcome to your user list.What is your name?")
    first_name = input()
    print("*****************************************************************")
    print(f"Hello {first_name} what would you like to do?")
    print('\n')
    while True:
        print("Use these short codes: ca - create a new user ,si - sign in to your account,gp - generate password")
        in_short_code = input().lower()
        if in_short_code == 'ca':
            print("Create a new account by following the steps below:")
            print("Enter your first name")
            first_name = input()
            print("Enter password:")
            pass_word = input()

            save_users(create_user(first_name,pass_word))
            print('\n')
            print(f"Thank you {first_name}, you may now proceed to open up your account")
            print('\n')

        elif in_short_code == 'gp':
                        alphabet = string.ascii_letters + string.digits
                        pass_word = ''.join(choice(alphabet) for i in range(8))
                        print(f"Your new generated password is: {pass_word} \n")
                      
    
        elif in_short_code == 'fu':
            if check_existing_users(search_first_name):
                search_user = find_user(search_first_name)
                print(f"{search_user.first_name}")
                print(f"Password.......{search_user.pass_word}")
            else:
                print("Sorry,This account does not exist!")

        elif in_short_code =='ex':
            print("Try again later,Goodbye!...")
            break 
        elif in_short_code == 'si':
            print('\n')
            print("Enter your password-locker username:")
            user_name = input()
            print("Enter your password:")
            pass_word = input()
            if check_existing_users(user_name):
                logged_user = find_user(user_name)
                print(f"Welcome {logged_user.user_name}")
                print('\n')
                while True:
                    print("Use these other short codes : ca - create a new credential, gp - to generate password, dc-to display credential, rc - to remove credential, fc-to find credential, ex -exit the user list ")
                    in_short_code2 = input().lower()
                    if in_short_code2 == 'ca':
                        print('\n')
                        print("Create a new credential")
                        print('\n')
                        print("Enter account name e.g Twitter,Github")
                        account_name=input()
                        print("Enter your login name for the account")
                        user_name=input()
                        print("Enter your password for the account")
                        pass_word=input()
                        save_credentials(create_credential(account_name,user_name,pass_word))
                        print('\n')
                        print(f"Wooow! You have created a new credential for your {account_name} account.")
                        print('\n')
                    
                    elif in_short_code2 == 'gp':
                        alphabet = string.ascii_letters + string.digits
                        password = ''.join(choice(alphabet) for i in range(8))
                        print(f"Your new generated password is: {pass_word} \n")
                      

                    elif in_short_code2 == 'dc':
                        print('/n')
                        if display_credentials():
                            print("Here is a list of all your credentials so far:")
                            print('\n')
                            for credential in display_credentials():
                                print(f"Account: {credential.account_name}")
                                print(f"User name: {credential.user_name}")
                                print(f"Password: {credential.pass_word}")
                                print('\n')
                        else:
                            print("\n You do not have any saved credentials")

                    elif in_short_code2 == 'fc':
                        print("Enter the account name you want to search for")
                    
                        search_account_name = input()
                        if check_existing_credentials(search_account_name):
                            search_credential = find_credential(search_account_name)
                            print(f"The account name is: {search_credential.account_name}")
                            print(f"the username associated with this account is:  {search_credential.user_name}")
                            print(f"The saved password is: {search_credential.pass_word}")
                        else:
                            print("That credential does not exist")

                

                    elif in_short_code2 == 'rc':
                        print("Enter the account name you want to delete")

                        del_account_name = input()
                        if check_existing_credentials(del_account_name):
                            search_del_credential = find_credential(del_account_name)
                            del_credential(search_del_credential)
                            print(f"Deleted credentials of {del_account_name}")
                        
                        else:
                            print("That credential does not exist")

                    elif in_short_code2 =='ex':
                        print("Going back to user options....")
                        break


                else:
                    print("Account does not exist")
        else:
            print("Incorrect shortcode, was that a typo?")

        
                
if __name__ == '__main__':
    main()