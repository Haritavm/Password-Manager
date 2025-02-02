import hashlib
import getpass

password_manager = {}

def create_account(): # Function to create a new account
    username = input("Enter the Username:") # Input the username
    password = getpass.getpass("Enter the Password:")   # Input the password
    hassed_password = hashlib.sha256(password.encode()).hexdigest() # Hash the password
    password_manager[username] ={'plain':password, 'hashed': hassed_password }# Store the username and password in the dictionary
    print("Account Created Successfully") # Print the success message

def login(): # Function to login to the account
    username = input("Enter the Username:") # Input the username
    password = getpass.getpass("Enter the Password:") # Input the password
    hassed_password = hashlib.sha256(password.encode()).hexdigest() # Hash the password
    if password_manager.get(username) == hassed_password: # Check if the username and password is correct
        print("Login Successful") # Print the success message
    else:
        print("Invalid Username or Password") # Print the failure message


def show_passwords(): # Function to show the passwords
    for username, passwords in password_manager.items(): # Loop through the dictionary
        print(f"Username: {username}, Password: {passwords['plain']}") # Print the username and plain text password or hashed password

def delete_account(): # Function to delete an account
    username = input("Enter the Username: ") # Input the username
    if username in password_manager: # Check if the username exists
        del password_manager[username] # Delete the account
        print("Account Deleted Successfully") # Print the success message
    else:   
        print("Account does not exist")

def main(): # Main function
    while True: # Loop until the user chooses to exit
        choice = input("1. Create Account\n2. Login\n3. Show Password\n4. Delete Account\n5. Exit\nEnter your choice:") # Display the menu
        if choice == "1": # If the user chooses to create an account
            create_account() # Call the create_account function
        elif choice == "2": # If the user chooses to login
            login() # Call the login function
        elif choice == "3": # If the user chooses to show the passwords
            show_passwords()
        elif choice == "4": # If the user chooses to delete an account
            delete_account() # Call the delete_account function
        elif choice == "5": # If the user chooses to exit
            break # Exit the loop
        else:   
            print("Invalid Choice") # Print the invalid choice message

if __name__ == "__main__": # If the script is run directly
    main() # Call the main function
