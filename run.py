
#!/usr/bin/env python3.7
from user import User  #importing the user class

def create_user(first_name,pass_word): #created the function create_user
    '''
    Function to create a new user
    '''
    new_user = User(first_name,pass_word) #created new user object and return it
    return new_user

