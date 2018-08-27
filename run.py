#!/usr/bin/env python3.7
from user import User

def create_user(first_name,pass_word):
    '''
    Function to create a new contact
    '''
    new_user = User(first_name)
    return new_user