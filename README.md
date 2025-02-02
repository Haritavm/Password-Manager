# Password Manager
The current file, manage_pass.py, is part of a project named Password Manager. This file includes functionality for managing user accounts, including creating accounts, logging in, showing passwords, and deleting accounts.

Key Components:
1-Imports:
  > hashlib: Used for hashing passwords.
  > getpass: Used for securely getting password input from the user.
2-Global Variables:
  > password_manager: A dictionary to store user information, including plain text and hashed passwords.
3-Functions:
  > create_account(): Creates a new user account.
  Process:
    > Prompts the user for a username and password.
    > Hashes the password using SHA-256.
    > Stores the username along with the plain text and hashed passwords in the password_manager dictionary.
    > Prints a success message.
  login(): Logs in to an existing user account.
  Process:
    > Prompts the user for a username and password.
    > Hashes the password using SHA-256.
    > Checks if the hashed password matches the stored hashed password for the given username.
    > Prints a success message if the login is successful, otherwise prints an error message.
  show_passwords(): Displays all stored usernames and their plain text passwords.
  Process:
    > Loops through the password_manager dictionary.
    > Prints each username and its corresponding plain text password.
  delete_account(): Deletes an existing user account.
  Process:
    > Prompts the user for a username.
    > Checks if the username exists in the password_manager dictionary.
    > Deletes the account if it exists and prints a success message.
Example Usage:
    Creating an Account:
    Logging In:
    Showing Passwords:
    Deleting an Account:
Notes:
The password_manager dictionary stores both the plain text and hashed passwords for each user.
The getpass.getpass() function is used to securely input passwords without displaying them on the screen.
Storing plain text passwords is not recommended due to security concerns. Consider storing only hashed passwords for better security.
This documentation provides an overview of the functionality and structure of the manage_pass.py file in the Password Manager project.
