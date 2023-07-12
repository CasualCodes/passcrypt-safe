# Imports
import crud

# Screens
def LoginScreen():
    print("Welcome to Passcrypt Safe!")

    while (True):
        print("\n1 - Login")
        print("2 - Signup")
        print("3 - Exit")
        choice = int(input("> "))
        passwordIncorrect = False
        accountAlreadyExists = False
        match choice:
            case 1:
                loginUsername = input("[Login] Enter Username: ")
                loginPassword = input("[Login] Enter Password: ")
                # Login Authentication/Verification
                passwordIncorrect = not crud.read(1, loginUsername, loginPassword)
                if passwordIncorrect:
                    print("Invalid Login!\n\n")
                else:
                    MainScreen(loginUsername, loginPassword) # Insert Parameters On User Details + Load Userentries
            case 2:
                signUpUsername = input("[Signup] Enter Username: ")
                signUpPassword = input("[Signup] Enter Password: ")
                # Signup Verification
                accountAlreadyExists = crud.read(4, signUpUsername, signUpPassword)
                if accountAlreadyExists:
                    print("Invalid Signup!\n\n")
                else:
                    crud.create(1, signUpUsername, signUpPassword)
                    print("Account Successfully Created!\n\n")
            case 3:
                print ("\nThank you for using the Program!\n")
                break
            case _:
                print("Invalid Input")

def MainScreen(username, password):
    # Load Required Information
    while (True):
        print("\n\nWelcome {}!".format(username))
        print("1 - View Entries")
        print("2 - View User Settings")
        print("3 - Add Entry")
        #TODO Place logout option here instead
        choice = int(input("> "))
        match choice:
            case 1:
                #Load Entries
                print("Entries: ")
                print("0 - Exit View Entries")
                if (crud.read(2, username,password) == False):
                    print("Entries do not exist")
                    print("Returning to Main Screen")
                    continue
                else:
                    print(crud.read(2, username,password))
                    print("Select Entry: ")
                    choice = int(input("> "))
                    if (choice != 0 and choice <= crud.read(5, username, password)):
                        openEntry(username, password, choice)
                    else:
                        continue
            case 2:
                option = UserSettingScreen(username, password)
                if (option == 1):
                    return
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
        print("\n\n{}".format(username))
        print("1 - Edit Password")
        print("2 - Delete Account")
        print("3 - Logout")
        print("4 - Return to Main Screen")
        choice = int(input("> "))
        match choice:
            case 1:
                oldPassword = input("Enter Old Password: ")
                newPassword = input("Enter New Password: ")
                if oldPassword != password:
                    print("Invalid!")
                else:
                    crud.update(1, username, password, password, newPassword)
                    print("Successfully Edited Password")
                continue
            case 2:
                oldPassword = input("Enter Old Password: ")
                if oldPassword != password:
                    print("Invalid!")
                    continue
                else:
                    crud.delete(1, username, password)
                    print("Delete Success: Returning to Login Screen")
                    return 1
            case 3:
                print("Logout Success: Returning to Login Screen")
                return 1
            case 4:
                return 2
            case _:
                print("Invalid Input")

def EditViewScreen(username, password, informationSet, setIndex):
    choice = int(input("Which to edit?:\n1 - Entry Name\n2 - Entry Type\n3 - Entry Description\n4 - Entry Content\n> "))
    if (choice == 1 or choice == 2 or choice == 3 or choice == 4):
        newInformation = input("Enter New Information: ")
        crud.update(2, username, password, informationSet[choice-1], newInformation, setIndex)
    else:
        print("Invalid Input - Returning to Entry View")

# systems
def openEntry(username, password, setIndex):
    informationSet = crud.read(3, username, password, setIndex).split(",")
    print("Entry Name: {}\nEntry Type : {}\nEntry Description: {}\nEntry Content: {}\n\n".format(
        informationSet[0],informationSet[1],informationSet[2],informationSet[3]
    ))
    while (True):
        choice = int(input("Options: \n1 - Edit Entry\n2 - Delete Entry\n3 - Close Entry\n> "))
        match choice:
            case 1:
                EditViewScreen(username, password, informationSet, setIndex)
                return
            case 2:
                crud.delete(2, username, password, setIndex-1)
                return
            case 3:
                return
            case _:
                print("Invalid Input")

def main(mode : int = 1):
    # Load Starting Menu
    if (mode == 1):
        LoginScreen()
    else:
        return

main()