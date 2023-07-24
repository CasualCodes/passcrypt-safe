from pathlib import Path
import os
import encryption

# file-crud-revamp branch

# Path Definitions
usersPath = "data/users.bin"
userEntriesPath = "data/userentries/{}.bin"
passwordIndex = 4

# Global variables
userCount : int = 10 # Placeholder
userEntryCount : int = 5 # Placeholder

# Dictionary Initialization [Attempt - NOT FINAL]
users : dict = [dict(userName = "", password = "") for x in range(userCount)]
userEntries : dict = [dict(entryName = "", entryType = "", entryDescription = "", entryContent = "") for x in range(userEntryCount)]

userMode = False
userEntriesMode = True

# Functions
def fileExists(mode, username : str = "default"):
    if (mode == 1):
        return os.path.exists(usersPath)
    else:
        return os.path.exists(userEntriesPath.format(username))

# *CREATE - Establishes File Structure
def create(createFunc : int, username : str, password : str, information : str = "information"):
    key = encryption.getKey(password)

    match createFunc:
        case 1: # Create User Account
            # Check if File Exists
            usersFile = fileExists(1)

            if not usersFile:
                # ENCRYPT
                toEncrypt = "{},{},".format(username, password)
                encryption.encrypt(key, userMode, usersPath, toEncrypt)
            else:
                # READ and ENCRYPT [FOR APPENDING]
                toEncrypt : str = encryption.decrypt(key, userMode, usersPath)
                toEncrypt += "{},{},".format(username, password)
                encryption.encrypt(key, userMode, usersPath, toEncrypt)

        case 2: # Create User Entry
            # Check if File Exists
            entryFile = fileExists(2, username)
            # information = "entryName,entryType,entryDescription,entryContent" [Handled By Frontend]

            if not entryFile:
                # ENCRYPT
                toEncrypt = "{}".format(information)
                encryption.encrypt(key, userEntriesMode, userEntriesPath.format(username), toEncrypt)
            else:
                # READ and ENCRYPT [FOR APPENDING]
                toEncrypt = encryption.decrypt(key, userMode, userEntriesPath.format(username))
                toEncrypt += "{}".format(information)
                encryption.encrypt(key, userEntriesMode, userEntriesPath.format(username), toEncrypt)            

# READ - Manages Data Dictionaries for Data Retrieval
def read(readFunc : int, username : str = "default", password : str = "default", setIndex : int = 1):
    key = encryption.getKey(password)

    match readFunc:
        case 1: # (Bool) Check for Match (User Authentication / Signup Validation)
            if (not fileExists(1)):
                return False

            # DECRYPT
            decryptFile = encryption.decrypt(key, userMode, usersPath)
            users = decryptFile.split(",")
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

            return False # Account Not Found

        case 2: # (String) All Nonsensitive Data Retrieval (Main Window Display)
            if (not fileExists(2, username)):
                return False

            # DECRYPT
            decryptFile = encryption.decrypt(key, userEntriesMode, userEntriesPath.format(username))
            informationSet = decryptFile.split(",")
            returnInformation = ""

            # TODO ! Modify returnInformation Format
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

            return returnInformation
        
        case 3: # (String) Specific Set Data Retrieval
            if (not fileExists(2, username)):
                return False

            # DECRYPT
            decryptFile = encryption.decrypt(key, userEntriesMode, userEntriesPath.format(username))
            informationSet = decryptFile.split(",")
            returnInformation : str = ""

            startingIndex = (setIndex-1) * passwordIndex
            endIndex = setIndex * passwordIndex

            x = startingIndex
            while (x < endIndex):
                returnInformation = returnInformation + informationSet[x] + ","
                x += 1

            return returnInformation

        case 4: # (Bool) Duplicate username check
            if (not fileExists(1)):
                return False
            
            # DECRYPT
            decryptFile = encryption.decrypt(key, userMode, usersPath)
            users = decryptFile.split(",")
            userCheck = False

            for user in users:
                # check username and password
                if (username == user):
                    userCheck = True
                    return True

            return False
        case 5 : # (Int) Entry Count # NOT NEEDED FOR ACTUAL APP- ONLY FOR EXCEPTION HANDLING
            if (not fileExists(2, username)):
                return False

            # DECRYPT
            decryptFile = encryption.decrypt(key, userEntriesMode, userEntriesPath.format(username))
            informationSet = decryptFile.split(",")

            x = 1
            y = 0
            while (x < len(informationSet)):
                if (x % passwordIndex == 0):
                    pass
                else:
                    if ((x+1) % passwordIndex == 0):
                        y += 1
                    else:
                        pass
                x += 1

            return y
        
# UPDATE - Updates the Data Dictionaries
def update(updateFunc : int, username : str, password : str, informationToChange :str , newInformation : str, setIndex : int = 1, entryIndex : int = 0):
    key = encryption.getKey(password)

    # Assuming that the user exists and usernames are unique
    match updateFunc:
        case 1: # User Password Update

            # DECRYPT
            decryptFile = encryption.decrypt(key, userMode, usersPath)
            users = decryptFile.split(",")
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
            
            # Ovewrite with new data
            # ENCRYPT
            toEncrypt : str = ""
            for user in users:
                if (user==""):
                    continue
                else:
                    # ENCRYPT
                    toEncrypt += "{},".format(user)
            encryption.encrypt(key, userMode, usersPath, toEncrypt)

        case 2: # User Entry Update

            decryptFile = encryption.decrypt(key, userEntriesMode, userEntriesPath.format(username))
            informationSet = decryptFile.split(",")

            startingIndex = (setIndex-1) * passwordIndex
            editIndex = startingIndex + entryIndex

            # TODO? Add Password Verification for authenticated password editing
            if (entryIndex == 4 and informationSet[editIndex] != informationToChange):
                print("Old Password is Incorrect")
                return
            informationSet[editIndex] = newInformation

            toEncrypt : str = ""
            for information in informationSet:
                if(information != ""):
                    toEncrypt += "{},".format(information)
            encryption.encrypt(key, userEntriesMode, userEntriesPath.format(username), toEncrypt)

# *DELETE
def delete(delFunc : int, username, password, delIndex : int = 1):
    key = encryption.getKey(password)
    if (delIndex == 0):
        delIndex = 1

    match delFunc:
        case 1: # Delete User
            # DECRYPT
            decryptFile = encryption.decrypt(key, userMode, usersPath)
            users = decryptFile.split(",")
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
            
            # ENCRYPT
            toEncrypt : str = ""
            for user in users:
                if (user==""):
                    continue
                else:
                    toEncrypt += "{},".format(user)
            
            # If no users remain, delete user file
            if (toEncrypt == ""):
                if os.path.exists(usersPath):
                    os.remove(usersPath)
            else:
                encryption.encrypt(key, userMode, usersPath, toEncrypt)

            # Delete editeduser file 
            if os.path.exists(userEntriesPath.format(username)):
                os.remove(userEntriesPath.format(username))

        case 2: # Delete User Entry
            
            # DECRYPT
            decryptFile = encryption.decrypt(key, userEntriesMode, userEntriesPath.format(username))
            informationSet = decryptFile.split(",")

            startingIndex = (delIndex-1) * passwordIndex
            endIndex = delIndex * passwordIndex

            x = startingIndex
            while (x < endIndex):
                informationSet[x] = ""
                x += 1
            
            toEncrypt : str = ""
            for information in informationSet:
                if(information != ""):
                    toEncrypt += "{},".format(information)

            # If no entries remain, delete entry file
            if (toEncrypt == ""):
                if os.path.exists(userEntriesPath.format(username)):
                    os.remove(userEntriesPath.format(username))
            else:
                encryption.encrypt(key, userEntriesMode, userEntriesPath.format(username), toEncrypt)