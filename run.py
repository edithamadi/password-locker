
#!/usr/bin/env python3.7
from user import User
from user import Credentials  #importing the user class

def create_user(first_name,pass_word): #created the function create_user
    '''
    Function to create a new user
    '''
    new_user = User(first_name,pass_word) #created new user object and return it
    return new_user

def save_users(user): # created function
    '''
    function to save users
    '''
    user.save_user() #function calls method to save the user

def del_user(user):
    '''
    function to delete a user
    '''
    user.delete_user()

def find_user(first_name):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return User.find_user(first_name) 

def check_existing_users(first_name):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.user_exists(first_name)

def display_users():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_all_users()


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
    credentials.save_credentials() #function calls method to save the credential

def del_credentials(credential):
    '''
    function to delete a credential
    '''
    credentials.delete_credential()

def find_credentials(first_name):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return credentials.find_by_first_name(first_name) 

def check_existing_credentials(first_name):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Credentials.ceredentials_exists(first_name)

def display_credentials():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_all_users()

def main():
    print("Hello Welcome to your user list.What is your name?")
    first_name = input()
    
    print(f"Hello {first_name} what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes: ca - create a new user ,si - sign in to your account ,dc - display credentials,fa - find account,fu- find a user,cc- create a new credential, gp - generate new password ,da- delete account ,ex - exit user list")
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

        elif in_short_code == 'si':
          print('\n')
          print("Enter your account first name:")
          first_name =input()
          print("Enter Password:")
          pass_word=input()
          if check_existing_users(first_name):
            saved_user = find_user(first_name)  
            print(f"Welcome to your account {saved_user.first_name}")  
            print('\n')

        elif in_short_code == 'fu':
            print(" \n Enter any username to find user: \n")
            search_first_name = input()
            if check_existing_users(search_first_name):
                search_user = find_user(search_first_name)
                print(f"{search_user.first_name}")
                print(f"Password.......{search_user.pass_word}")
            else:
                 print("Sorry,This account does not exist!")

        elif in_short_code =='ex' :
            print("Try again later,Goodbye!...")
            break
            
                    

        elif in_short_code == 'cc':
                        print('\n')
                        print("Follow the following steps to create a new credential;")
                        print('\n')
                        print("Enter the account name i.e Instagram/Facebook/Twitter")
                        account_name=input()
                        print("Enter your first name for the new account:")
                        first_name=input()
                        print("Enter password:")
                        pass_word=input()
                        save_credentials(create_credentials(account_name,first_name,pass_word))
                        print('\n')
                        print(f"You have successfully created a new credential for your new {account_name} account.")
                        print('\n')

        elif in_short_code == 'gp':
                        alphabet = string.ascii_letters + string.digits
                        pass_word = ''.join(choice(alphabet) for i in range(8))
                        print(f"Your new generated password is: {pass_word} \n")
                      

        elif in_short_code == 'dc':
                        print('/n')
                        if display_credentials():
                            print("Below is a list of all your credentials:")
                            print('\n')
                            for credential in display_credentials():
                                print(f"Name of Account: {credentials.account_name}")
                                print(f"Username: {credentials.first_name}")
                                print(f"Password: {credentials.pass_word}")
                                print('\n')
                        else:
                            print("\n Sorry,You do not have any credentials to display")

        elif in_short_code == 'fa':
          print("Enter name of account you'd wish to search for")
          search_account_name=input()
          if check_existing_credentials(search_account_name):
            search_credentials= find_credentials(search_account_name)
            print(f"Name of the account: {search_account_name}")
            print(f"Account Username: {search_credentials.first_name}")
            print(f"Account Password: {search_credentials.pass_word}")

          else:
            print("Sorry,The entered credential does not exist")      

        elif in_short_code == 'da':
          print("Which account do you wish to delete?")
          delete_account_name=input()
          if check_existing_credentials(delete_account_name):
            search_delete_credentials= find_credentials(delete_account_name)
            delete_credentials(search_delete_credentials)

            print(f"Your {delete_account_name} credentials have been successfully deleted")

          else:
            print("Sorry,Credential does not exist")   

        elif in_short_code == 'ex':
          print("Goodbye...")
          break

    else:
           print("Short code not found,Please use the short codes")

       

        
                
if __name__ == '__main__':
        main()



