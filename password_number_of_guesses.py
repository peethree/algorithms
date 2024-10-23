def get_num_guesses(length):

    password_characters = 26
    
    # Base cases
    if length == 0:
        return 0
    if length == 1:
        return password_characters
    
    # Recursive case
    return password_characters + password_characters * get_num_guesses(length - 1)