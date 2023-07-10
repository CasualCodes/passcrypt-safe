from pathlib import Path
import os

# file-crud-revamp branch

# Path Definitions
usersPath = "data/users.csv"
userEntriesPath = "data/userentries/{}.csv"
passwordIndex = 4

# Global variables
userCount : int = 10 # Placeholder
userEntryCount : int = 5 # Placeholder

# Dictionary Initialization [Attempt - NOT FINAL]
users : dict = [dict(userName = "", password = "") for x in range(userCount)]
userEntries : dict = [dict(entryName = "", entryType = "", entryDescription = "", entryContent = "") for x in range(userEntryCount)]

# Functions
def fileExists(mode, username : str = "default"):
    if (mode == 1):
        return os.path.exists(usersPath)
    else:
        return os.path.exists(userEntriesPath.format(username))

# *CREATE - Establishes File Structure
def create(createFunc : int, username : str, password : str, information : str = "information"):

    match createFunc:
        case 1: # Create User Account
            # Check if File Exists
            usersFile = fileExists(1)

            if not usersFile:
                writeFile = open(usersPath, 'w')
            else:
                writeFile = open(usersPath, 'a')

            #Uername is assumed to have no duplicates
            writeFile.write("{},{},".format(username, password))
            writeFile.close()

        case 2: # Create User Entry
            # Check if File Exists
            entryFile = fileExists(2, username)

            if not entryFile:
                writeFile = open(userEntriesPath.format(username), 'w')
            else:
                writeFile = open(userEntriesPath.format(username), 'a')

            # Information = "entryName,entryType,entryDescription,entryContent" [Handled By Frontend]

            writeFile.write("{},".format(information))
            writeFile.close()

# READ - Manages Data Dictionaries for Data Retrieval
def read(readFunc : int, username : str = "default", password : str = "default", setIndex : int = 1):
    if (not fileExists(1) or not fileExists(2, username)):
        return False

    match readFunc:
        case 1: # (Bool) Check for Match (User Authentication / Signup Validation)
            readFile = open("data/users.csv", 'r')
            users = readFile.read().split(",")
            userCheck = False

            for user in users:
                # check username and password
                if (username == user):
                    userCheck = True
                    continue
                elif (userCheck == True and password == user):
                    return True # Account Found
                else:
                    userCheck = False
            
            readFile.close()
            return False # Account Not Found

        case 2: # (String) All Nonsensitive Data Retrieval (Main Window Display)
            readFile = open("data/userentries/{}.csv".format(username), 'r')
            informationSet = readFile.read().split(",")
            returnInformation = ""

            x = 1
            y = 0
            while (x < len(informationSet)):
                if (x % passwordIndex == 0):
                    pass
                else:
                    if ((x+1) % passwordIndex == 0):
                        returnInformation += "{} - {}\n\n".format(y+1, informationSet[x-1])
                        y += 1
                    else:
                        returnInformation += "{} - {} ".format(y+1, informationSet[x-1])
                x += 1

            readFile.close()
            return returnInformation
        
        case 3: # (String) Specific Set Data Retrieval
            readFile = open("data/userentries/{}.csv".format(username), 'r')
            informationSet = readFile.read().split(",")
            returnInformation : str = ""

            startingIndex = (setIndex-1) * passwordIndex
            endIndex = setIndex * passwordIndex

            x = startingIndex
            while (x < endIndex):
                returnInformation = returnInformation + informationSet[x] + ","
                x += 1
            readFile.close()
            return returnInformation

        case 4: # (Bool) Duplicate username check
            readFile = open("data/users.csv", 'r')
            users = readFile.read().split(",")
            userCheck = False

            for user in users:
                # check username and password
                if (username == user):
                    userCheck = True
                    return True
            
            readFile.close()
            return False

# UPDATE - Updates the Data Dictionaries
def update(updateFunc : int, username : str, informationToChange :str , newInformation : str, setIndex : int = 1, entryIndex : int = 0):
    # Assuming that the user exists and usernames are unique
    match updateFunc:
        case 1: # User Password Update
            readFile = open("data/users.csv", 'r')
            users = readFile.read().split(",")
            userCheck = False
            for user in users:
                # check username and password
                if (username == user):
                    userCheck = True
                    print("Username exists at {}".format(users.index(user)))
                    continue
                elif (userCheck == True and informationToChange == user):
                    print ("Account Exists. Password verified at {}".format(users.index(user)))
                    users[users.index(user)] = newInformation
                    print("Password Changed")
                else:
                    userCheck = False
            readFile.close()
            
            # Ovewrite with new data
            readFile = open("data/users.csv", "w")
            for user in users:
                if (user==""):
                    continue
                else:
                    print(user)
                    readFile.write("{},".format(user))

        case 2: # User Entry Update
            """
            Entry Details:
            1 - Name of Entry
            2 - Type of Entry
            3 - Content of Entry
            4 - Sensitive Information
            """
            readFile = open("data/userentries/{}.csv".format(username), 'r')
            informationSet = readFile.read().split(",")

            startingIndex = (setIndex-1) * passwordIndex
            editIndex = startingIndex + entryIndex

            # TODO? Add Password Verification for authenticated password editing
            if (entryIndex == 4 and informationSet[editIndex] != informationToChange):
                print("Old Password is Incorrect")
                return
            informationSet[editIndex] = newInformation

            readFile.close()
            readFile = open("data/userentries/{}.csv".format(username), 'w')
            for information in informationSet:
                if(information != ""):
                    readFile.write("{},".format(information))

# *DELETE
def delete(delFunc : int, username, password, delIndex : int = 1):
    match delFunc:
        case 1: # Delete User
            readFile = open("data/users.csv", 'r')
            users = readFile.read().split(",")
            userCheck = False
            for user in users:
                # check username and password
                if (username == user):
                    userCheck = True
                    continue
                
                elif (userCheck == True and password == user):
                    print ("Account Exists. Password verified at {}".format(users.index(user)))
                    users[users.index(user)-1] = ""
                    users[users.index(user)] = ""
                    print("Account Deleted")
                else:
                    userCheck = False
            
            readFile = open("data/users.csv", "w")
            for user in users:
                if (user==""):
                    continue
                else:
                    readFile.write("{},".format(user))
            # Delete editeduser file 
            if os.path.exists("data/userentries/{}.csv".format(username)):
                os.remove("data/userentries/{}.csv".format(username))

        case 2: # Delete User Entry
            """
            Entry Details:
            1 - Name of Entry
            2 - Type of Entry
            3 - Content of Entry
            4 - Sensitive Information
            """
            
            readFile = open("data/userentries/{}.csv".format(username), 'r')
            informationSet = readFile.read().split(",")

            passwordIndex = 5
            startingIndex = (delIndex-1) * passwordIndex
            endIndex = delIndex * passwordIndex

            x = startingIndex
            while (x < endIndex):
                informationSet[x] = ""
                x += 1

            readFile.close()
            readFile = open("data/userentries/{}.csv".format(username), 'w')
            for information in informationSet:
                if(information != ""):
                    readFile.write("{},".format(information))