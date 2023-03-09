
# Brandon Scheiber 
# COP3502

def prompt(): 
    '''prints out a menu for the user -> str'''
    print("Menu\n"
          "------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")

    user_input = input("Please enter an option: ")
    return user_input

def encode():
    '''8-digit integer --> list of number '''

    password = input("Please enter your password to encode: ")
    password = list(password)
    new_password = [(int(num) + 3) for num in password]

    print("Your password has been encoded and stored!")
    return new_password

    

def decode(n_password):
    '''decodes password'''
    pass
    


def main():
    user_input = prompt()
    if user_input == "1":
        n_password = encode()
        # print(str(n_password))  #For testing

    elif user_input == "2":
        #decode(n_password)
        pass

    else: #quit
        pass






if __name__ == "__main__":
    main()