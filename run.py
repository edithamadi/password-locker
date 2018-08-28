
#!/usr/bin/env python3.7
from user import User  #importing the user class

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

def del_user(user)
    '''
    function to delete a user
    '''
    user.delete_user()

def find_user(first_name):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return User.find_by_first_name(first_name) 

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





