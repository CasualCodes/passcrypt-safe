# Imports
import sys
import crud
import PyQt5
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

# Using UIC LoadUI : Using .py for future changes is considered

# Login Screen
class LoginScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        uic.loadUi("ui/LoginScreen.ui", self)
        
        # References to ui elements/widgets
        self.welcomeLabel = self.findChild(QtWidgets.QLabel, "welcomeLabel")
        self.usernameEdit = self.findChild(QtWidgets.QLineEdit, "usernameEdit")
        self.passwordEdit = self.findChild(QtWidgets.QLineEdit, "passwordEdit")
        self.loginButton = self.findChild(QtWidgets.QPushButton, "loginButton")
        self.signupButton = self.findChild(QtWidgets.QPushButton, "signupButton")
        
        # Button Connections
        self.loginButton.clicked.connect(self.login)
        self.signupButton.clicked.connect(self.signup)

    # Login
    def login(self): 
        if (self.emptyInputCheck()):
            self.clearLineEdit()
            self.welcomeLabel.setText("Empty Input, Try Again")
            return

        # Authentication Logic : If username and password is not found in the data file, consider it as incorrect password
        # Can be edited if there are future crud / io overhauls
        passwordIncorrect = not crud.read(1, self.getUsername(), self.getPassword())
        if passwordIncorrect:
            self.clearLineEdit()
            self.welcomeLabel.setText("Incorrect Password, Try Again")
        else:
            mainScreen = MainScreen(self.getUsername(), self.getPassword())
            self.clearLineEdit()
            widget.addWidget(mainScreen)
            widget.setCurrentIndex(widget.currentIndex()+1)

    # Sign Up
    def signup(self): 
        if (self.emptyInputCheck()):
            self.clearLineEdit()
            self.welcomeLabel.setText("Empty Input, Try Again")
            return
        
        # Verification Logic : If username and password is found in the datafile, consider it as existing account.
        # There is no separate signup page for simplicity.
        accountAlreadyExists = crud.read(4, self.getUsername(), self.getPassword())
        if accountAlreadyExists:
            self.clearLineEdit()
            self.welcomeLabel.setText("Account already exists, Try Again")
        else:
            crud.create(1, self.getUsername(), self.getPassword())
            self.welcomeLabel.setText("Account Successfully Created!")

    # Helper Functions
    def emptyInputCheck(self):
        return self.getUsername() == "" or self.getPassword() == ""

    def clearLineEdit(self):
        self.usernameEdit.setText("")
        self.passwordEdit.setText("")

    def getUsername(self):
        return self.usernameEdit.text()

    def getPassword(self):
        return self.passwordEdit.text()

# Main Screen
class MainScreen(QtWidgets.QMainWindow):
    def __init__(self, username : str = "default", password : str = "default"): # Attempt for arguments in Main Screen
        super(MainScreen, self).__init__()
        uic.loadUi("ui/MainScreen.ui", self)
        self.username = username
        self.password = password
        self.tableLoaded = False # Legacy Variable

        # References to ui elements / widgets (some are too long)
        # Topbar Elements
        self.welcomeLabel = self.findChild(QtWidgets.QLabel, "welcomeLabel")
        self.addEntryButton = self.findChild(QtWidgets.QPushButton, "addEntryButton")
        self.logoutButton = self.findChild(QtWidgets.QPushButton, "logoutButton")
        self.userSettingsButton = self.findChild(QtWidgets.QPushButton, "userSettingsButton")

        # Table Section
        self.filterCombo = self.findChild(QtWidgets.QComboBox, "filterCombo") # UNUSED
        self.tableWidget = self.findChild(QtWidgets.QTableWidget, "tableWidget")

        # Sidebar Stacked Widget
        self.sidebar = self.findChild(QtWidgets.QStackedWidget, "sidebar")

        # Default View
        self.sidebar.defaultView = self.findChild(QtWidgets.QWidget, "defaultView")

        # View Entry
        self.sidebar.selectedEntryView = self.findChild(QtWidgets.QWidget, "selectedEntryView")
        self.sidebar.selectedEntryView.deleteButton = self.findChild(QtWidgets.QPushButton, "deleteButton")
        self.sidebar.selectedEntryView.editButton = self.findChild(QtWidgets.QPushButton, "editButton")
        self.sidebar.selectedEntryView.entryContentEdit = self.findChild(QtWidgets.QLineEdit, "entryContentEdit")
        self.sidebar.selectedEntryView.entryDescriptionEdit = self.findChild(QtWidgets.QLineEdit, "entryDescriptionEdit")
        self.sidebar.selectedEntryView.entryNameEdit = self.findChild(QtWidgets.QLineEdit, "entryNameEdit")
        self.sidebar.selectedEntryView.entryTypeCombo_2 = self.findChild(QtWidgets.QComboBox, "entryTypeCombo")

        # User Settings
        self.sidebar.userSettingView = self.findChild(QtWidgets.QWidget, "userSettingView")
        self.sidebar.userSettingView.changePasswordButton = self.findChild(QtWidgets.QPushButton, "changePasswordButton")
        self.sidebar.userSettingView.deleteAccountButton = self.findChild(QtWidgets.QPushButton, "deleteAccountButton")
        self.sidebar.userSettingView.entryCountLabel = self.findChild(QtWidgets.QLabel, "entryCountLabel")
        self.sidebar.userSettingView.paddingLabel = self.findChild(QtWidgets.QLabel, "paddingLabel")
        self.sidebar.userSettingView.usernameLabel = self.findChild(QtWidgets.QLabel, "usernameLabel")

        # Account Delete
        self.sidebar.accountDeleteView = self.findChild(QtWidgets.QWidget, "accountDeleteView")
        self.sidebar.accountDeleteView.cancelButton_2 = self.findChild(QtWidgets.QPushButton, "cancelButton_2")
        self.sidebar.accountDeleteView.confirmAccountDeleteButton = self.findChild(QtWidgets.QPushButton, "confirmAccountDeleteButton")
        self.sidebar.accountDeleteView.errorMessageLabel_2 = self.findChild(QtWidgets.QLabel, "errorMessageLabel_2")
        self.sidebar.accountDeleteView.paddingLabel_3 = self.findChild(QtWidgets.QLabel, "paddingLabel_3")
        self.sidebar.accountDeleteView.passwordEdit = self.findChild(QtWidgets.QLineEdit, "passwordEdit")
        self.sidebar.accountDeleteView.questionLabel = self.findChild(QtWidgets.QLabel, "questionLabel")

        # Password Change
        self.sidebar.passwordChangeView = self.findChild(QtWidgets.QWidget, "passwordChangeView")
        self.sidebar.passwordChangeView.cancelButton = self.findChild(QtWidgets.QPushButton , "cancelButton")
        self.sidebar.passwordChangeView.confirmChangeButton = self.findChild(QtWidgets.QPushButton , "confirmChangeButton")
        self.sidebar.passwordChangeView.errorMessageLabel = self.findChild(QtWidgets.QLabel , "errorMessageLabel")
        self.sidebar.passwordChangeView.newPasswordEdit = self.findChild(QtWidgets.QLineEdit , "newPasswordEdit")
        self.sidebar.passwordChangeView.oldPasswordEdit = self.findChild(QtWidgets.QLineEdit , "oldPasswordEdit")
        self.sidebar.passwordChangeView.paddingLabel_2 = self.findChild(QtWidgets.QLabel , "paddingLabel_2")
        
        # Add Entry
        self.sidebar.newEntryView = self.findChild(QtWidgets.QWidget, "newEntryView")
        self.sidebar.newEntryView.cancelButton_3 = self.findChild(QtWidgets.QPushButton , "cancelButton_3")
        self.sidebar.newEntryView.entryContentEdit_2 = self.findChild(QtWidgets.QLineEdit , "entryContentEdit_2")
        self.sidebar.newEntryView.entryDescriptionEdit_2 = self.findChild(QtWidgets.QLineEdit , "entryDescriptionEdit_2")
        self.sidebar.newEntryView.entryNameEdit_2 = self.findChild(QtWidgets.QLineEdit , "entryNameEdit_2")
        self.sidebar.newEntryView.entryTypeCombo = self.findChild(QtWidgets.QComboBox , "entryTypeCombo")
        self.sidebar.newEntryView.saveButton = self.findChild(QtWidgets.QPushButton , "saveButton")

        # Initialization
        self.welcomeLabel.setText("Welcome! {}".format(self.username))
        self.entryCount = self.loadTable()
        self.entryCountText = self.entryCountLabel.text()
        self.entryCountLabel.setText("{} {}".format(self.entryCountText, self.entryCount))

        # Button Connections
        # Topbar
        self.addEntryButton.clicked.connect(self.loadNewEntryView)
        self.userSettingsButton.clicked.connect(self.loadSettingsView)
        self.logoutButton.clicked.connect(self.logout)

        # Table
        self.tableWidget.cellClicked.connect(self.loadSelectedEntryView)

        # Sidebar
        # Delete Account View
        self.deleteAccountButton.clicked.connect(self.loadAccountDeleteView)
        self.cancelButton_2.clicked.connect(self.loadSettingsView)
        self.confirmAccountDeleteButton.clicked.connect(lambda: self.deleteAccount())

        # Change Password View
        self.changePasswordButton.clicked.connect(self.loadPasswordChangeView)
        self.cancelButton.clicked.connect(self.loadSettingsView)
        self.confirmChangeButton.clicked.connect(lambda: self.changePassword())

        # Add Entry View
        self.saveButton.clicked.connect(self.addNewEntry)
        self.cancelButton_3.clicked.connect(self.loadDefault)
    
    # Default Sidebar
    def loadDefault(self):
        self.sidebar.setCurrentWidget(self.sidebar.defaultView)

    # Logout
    def logout(self):
        widget.removeWidget(self)
        widget.setCurrentIndex(widget.currentIndex()-1)
    
    # Table Display/Loading
    # Logic : Get Information (a string of comma separated data) and divide it as data of the table
    # Proposal : Using an index table may help with the filter function
    def loadTable(self):
        input =  crud.read(2, self.username, self.password)
        if input == False:
            return 0
        entries = input.split(",")
        rowCount = int(len(entries)/3)
        row = 0
        self.tableWidget.setRowCount(rowCount)
        index = 0
        #print(input)
        #print(row, rowCount)
        for row in range(rowCount):
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(entries[index])))
            index += 1
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(entries[index])))
            index += 1
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(entries[index])))
            index += 1
            row += 1
        return rowCount

    # Refreshes the Main Screen
    def updateTable(self):
        # Button Disconnections
        try:
            self.editButton.clicked.disconnect()
            self.deleteButton.clicked.disconnect()
        except:
            pass

        self.logoutButton.setEnabled(True)
        self.userSettingsButton.setEnabled(True)
        self.addEntryButton.setEnabled(True)
        self.tableWidget.setEnabled(True)

        self.tableWidget.clearContents()
        self.entryCount = self.loadTable()
        self.entryCountLabel.setText("{} {}".format(self.entryCountText, self.entryCount))
        self.loadDefault()

    # Selected Entry Sidebar
    def loadSelectedEntryView(self, row):
        # TODO ! Make Entry Content (contents) 'hidden' somehow
        input = crud.read(3, self.username, self.password, row+1)
        entry = input.split(",")

        entryName = 0
        entryType = 1
        entryDescription = 2
        entryContent = 3

        if entry[entryType] == "Account":
            entryIndex = 1
        else:
            entryIndex = 0
        
        self.sidebar.selectedEntryView.entryNameEdit.setText(entry[entryName])
        self.entryTypeCombo_2.setCurrentIndex(entryIndex)
        self.sidebar.selectedEntryView.entryDescriptionEdit.setText(entry[entryDescription])
        self.sidebar.selectedEntryView.entryContentEdit.setText(entry[entryContent])
        self.sidebar.setCurrentWidget(self.sidebar.selectedEntryView)

        # Enable Selected Entry View Buttons
        self.deleteButton.clicked.connect(lambda: self.deleteEntry(row))
        self.editButton.clicked.connect(lambda: self.editEntryEnable(row))

    # New Entry Sidebar + add entry function
    def loadNewEntryView(self):
        self.sidebar.setCurrentWidget(self.sidebar.newEntryView)
    
    def addNewEntry(self):
        # Get entry contents
        entryName = self.entryNameEdit_2.text()
        entryType = self.entryTypeCombo.currentText()
        entryDescription = self.entryDescriptionEdit_2.text()
        entryContent = self.entryContentEdit_2.text()
        if (entryName == "" or entryType == "" or entryDescription == "" or entryContent == ""):
            return
        information = f"{entryName},{entryType},{entryDescription},{entryContent},"

        crud.create(2, self.username, self.password, information)
        self.entryNameEdit_2.setText("")
        self.entryTypeCombo.setCurrentIndex(0)
        self.entryDescriptionEdit_2.setText("")
        self.entryContentEdit_2.setText("")
        # Reload Table to update
        self.updateTable()

    # Entry Deletion
    def deleteEntry(self, row):
        crud.delete(2, self.username, self.password, row+1)
        self.tableWidget.setRowCount(self.tableWidget.rowCount() - 1)
        # self.loadDefault()
        self.updateTable()

    # Edit -> Enable widgets -> wait for confirm button -> edit the entry
    def editEntryEnable(self, row):
        # print(row)
        # Enable all editable widgets
        oldInformation = "{},{},{},{},".format(self.entryNameEdit.text(), self.entryTypeCombo_2.currentText(), self.entryDescriptionEdit.text(), self.entryContentEdit.text())
        self.entryNameEdit.setEnabled(True)
        self.entryTypeCombo_2.setEnabled(True)
        self.entryDescriptionEdit.setEnabled(True)
        self.entryContentEdit.setEnabled(True)

        self.logoutButton.setEnabled(False)
        self.userSettingsButton.setEnabled(False)
        self.addEntryButton.setEnabled(False)
        self.tableWidget.setEnabled(False)

        # Enable Button
        self.editButton.setText("Save")
        self.deleteButton.setText("Cancel")
        self.deleteButton.clicked.disconnect()
        self.editButton.clicked.disconnect()
        self.editButton.clicked.connect(lambda: self.editEntry(oldInformation, row))
        self.deleteButton.clicked.connect(lambda: self.editEntryCancel(oldInformation, row))

    def editEntryCancel(self, oldInformation, row):
        self.entryNameEdit.setEnabled(False)
        self.entryTypeCombo_2.setEnabled(False)
        self.entryDescriptionEdit.setEnabled(False)
        self.entryContentEdit.setEnabled(False)

        self.logoutButton.setEnabled(True)
        self.userSettingsButton.setEnabled(True)
        self.addEntryButton.setEnabled(True)
        self.tableWidget.setEnabled(True)

        self.editButton.setText("Edit")
        self.deleteButton.setText("Delete")
        self.editButton.clicked.disconnect()
        self.deleteButton.clicked.disconnect()
        self.deleteButton.clicked.connect(lambda: self.deleteEntry(row))
        self.editButton.clicked.connect(lambda: self.editEntryEnable(row))

    # Edit Logic : Replace old information with new information through the given row index
    # WARNING : Using the row index may lead to problems in future features to implement when wanted (e.g. Filter)
    def editEntry(self, information, row):
        newInformation = "{},{},{},{},".format(self.entryNameEdit.text(), self.entryTypeCombo_2.currentText(), self.entryDescriptionEdit.text(), self.entryContentEdit.text())
        self.entryNameEdit.setText("") 
        self.entryTypeCombo_2.setCurrentIndex(0) 
        self.entryDescriptionEdit.setText("")
        self.entryContentEdit.setText("")
        self.editButton.setText("Edit")
        self.deleteButton.setText("Delete")
        crud.update(3, self.username, self.password, information, newInformation, row+1)
        self.updateTable()

    # User Settings
    def loadSettingsView(self):
        self.sidebar.setCurrentWidget(self.sidebar.userSettingView)

    def loadAccountDeleteView(self):
        self.sidebar.setCurrentWidget(self.sidebar.accountDeleteView)

    def loadPasswordChangeView(self):
        self.sidebar.setCurrentWidget(self.sidebar.passwordChangeView)
    
    def deleteAccount(self):
        oldPassword = self.password
        password = self.passwordEdit.text()
        if oldPassword != password:
            self.errorMessageLabel.setText("Invalid!")
        else:
            self.errorMessageLabel.setText("")
            crud.delete(1, self.username, self.password)
            self.logout()
            
    def changePassword(self):
        oldPassword = self.oldPasswordEdit.text()
        password = self.newPasswordEdit.text()
        if oldPassword != self.password:
            self.errorMessageLabel_2.setText("Invalid!")
        else:
            self.errorMessageLabel_2.setText("")
            self.refreshUserEntries(password)
            crud.update(1, self.username, self.password, self.password, password)
            self.password = password
            self.updateTable()

    def refreshUserEntries(self, newPassword):
        # Re Encrypt All entries with new password
        informationSet : str = crud.read(6, self.username, self.password)
        crud.delete(3, self.username, self.password)
        crud.create(2, self.username, newPassword, informationSet)

# def main(): 
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
loginScreen = LoginScreen()
widget.addWidget(loginScreen)
widget.setCurrentIndex(0)
widget.show()
sys.exit(app.exec())

# main()