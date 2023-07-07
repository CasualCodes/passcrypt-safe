# Imports
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from pathlib import Path
import os
import crud

# GENERAL TODO
# 1 - Use Dictionaries For Data Structuring
# > 1 Dictionary for Users > 1 Dictionary Where NonSensitiveInformation is the Key and Sensitive Information is the Value

# Global Variables
users : dict = {}
userEntries : dict = {}

# Screens
def LoginScreen():
    print("Welcome to Passcrypt Safe!\n\n")

    while (True):
        print("1 - Login")
        print("2 - Signup")
        print("3 - Exit")
        choice = input("> ")
        passwordIncorrect = False
        accountAlreadyExists = False
        match choice:
            case 1:
                loginUsername = input("[Login] Enter Username: ")
                loginPassword = input("[Login] Enter Password: ")
                # Login Authentication/Verification
                passwordIncorrect = crud.read(1, loginUsername, loginPassword)
                if passwordIncorrect:
                    print("Invalid Login!\n\n")
                else:
                    MainScreen(loginUsername, loginPassword) # Insert Parameters On User Details + Load Userentries
            case 2:
                signUpUsername = input("[Signup] Enter Username: ")
                signUpPassword = input("[Signup] Enter Password: ")
                # Signup Verification
                crud.read(1, signUpUsername, signUpPassword)
                if accountAlreadyExists:
                    print("Invalid Signup!\n\n")
                else:
                    crud.create(1, signUpUsername, signUpPassword)
                    print("Account Successfully Created!\n\n")
            case 3:
                print ("Thank you for using the Program!")
                break
            case _:
                print("Invalid Input\n\n")

def MainScreen(username, password):
    # Load Required Information
    # TODO crud.read(displayAll) adjustments
    while (True):
        print("Welcome User!")
        print("1 - View Entries")
        print("2 - View User Settings")
        print("3 - Add Entry")
        choice = input("> ")
        match choice:
            case 1:
                #Load Entries
                print("Entries: ")
                print("0 - Exit View Entries")
                #crud.read(2, username,password)
                print("Select Entry: ")
                choice = input("> ")
                if (choice != 0):
                    openEntry(username, password, choice-1)
                else:
                    continue
            case 2:
                option = UserSettingScreen(username, password)
                if (option == 1):
                    return #Logout
                elif (option == 2):
                    continue
            case 3:
                entryName = input("Input Entry Name: ")
                entryType = input("Input/Choose Entry Type: ")
                entryDescription = input("Input Entry Description: ")
                entryContent = input("Input Entry Contents: ") # sensitive information
                information = f"{entryName},{entryType},{entryDescription},{entryContent}"

                crud.create(2, username, password, information)
            case _:
                print("Invalid Input")

def UserSettingScreen(username, password):
    while (True):
        print("{}".format(username))
        print("Account Created") # ???
        print("1 - Edit Password")
        print("2 - Delete Account")
        print("3 - Logout")
        print("4 - Return to Main Screen")
        choice = input("> ")
        match choice:
            case 1:
                oldPassword = input("Enter Old Password: ")
                newPassword = input("Enter New Password: ")
                if oldPassword != password:
                    print("Invalid!")
                else:
                    crud.update(1, username, password, newPassword)
                    print("Successfully Edited Password")
                continue
            case 2:
                crud.delete(1, username, password)
                print("Delete Success: Returning to Login Screen")
                return 1
            case 3:
                print("Logout Success: Returning to Login Screen")
                return 1
            case 4:
                return 2

def EditViewScreen(a, b, c):
    # load entry details
    

    print("Entry Name: ") # c.something
    print("Entry Type: ") # c.something
    print("...")        # c.something

# systems
def openEntry(a,b,c):
    # Load entry as c
    d = c #converted to dictionary
    EditViewScreen(a, b, d)

def initUser():
    pass

def initUserEntries(username):
    pass

def main(mode : int = 1):
    # TODO User Navigation
    # Load Starting Menu
    if (mode == 1):
        LoginScreen()
    else:
        print("Testing Mode:")
        # CRUD Testing Ground
        #crud.create(1, "username", "password")
        #crud.create(1, "newUser", "newPassword")
        #crud.create(2, "newUser", "newPassword", "Gmail,Account,Gmail@gmail.com,Account For Gmail,password12345678,1,2,3,4,5")
        #crud.create(1, "editedUser", "noneditedPassword")
        #crud.create(2, "editedUser", "noneditedPassword", "1,1,1,1,1")
        #crud.create(2, "username", "password", "1,2,3,4,5")
        #crud.read(1, "newUser", "newPassword")
        #crud.read(2, "newUser", "newPassword")
        #crud.read(3, "newUser", "newPassword")
        #crud.read(3, "newUser", "newPassword", 2)
        #crud.read(1, "editedUser", "noneditedPassword")
        #crud.update(1, "editedUser", "noneditedPassword", "editedPassword")
        #crud.read(1, "editedUser", "editedPassword")
        #crud.update(2, "username", "5", "newpassword", 1, 4)
        #crud.delete(1, "editedUser", "editedPassword")
        #crud.delete(2, "newUser", "newPassword", 2)

main()
#main(2)