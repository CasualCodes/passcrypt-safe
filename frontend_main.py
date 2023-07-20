# Imports - to be polished
import sys
import PyQt5
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

# Functions / Methods
# Using loadUI due to mainly using QtDesigner for layout editing

# Progress
# [*] Navigation
# [] Backend Integration

class LoginScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        uic.loadUi("ui/LoginScreen.ui", self)
        
        # References
        self.welcomeLabel = self.findChild(QtWidgets.QLabel, "welcomeLabel")
        self.usernameEdit = self.findChild(QtWidgets.QLineEdit, "usernameEdit")
        self.passwordEdit = self.findChild(QtWidgets.QLineEdit, "passwordEdit")
        self.loginButton = self.findChild(QtWidgets.QPushButton, "loginButton")
        self.signupButton = self.findChild(QtWidgets.QPushButton, "signupButton")
        
        # Connections
        self.loginButton.clicked.connect(self.login)
        self.signupButton.clicked.connect(self.signup)

    # Functions
    def login(self):
        # LOAD MAIN
        widget.setCurrentIndex(widget.currentIndex()+1)
        # TODO add parameters to load

    def signup(self):
        print("{} {}".format(self.getUsername(), self.getPassword()))

    def getUsername(self):
        return self.usernameEdit.text()

    def getPassword(self):
        return self.passwordEdit.text()


class MainScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        uic.loadUi("ui/MainScreen.ui", self)

        # References    
        # Topbar Elements
        self.welcomeLabel = self.findChild(QtWidgets.QLabel, "welcomeLabel")
        self.addEntryButton = self.findChild(QtWidgets.QPushButton, "addEntryButton")
        self.logoutButton = self.findChild(QtWidgets.QPushButton, "logoutButton")
        self.userSettingsButton = self.findChild(QtWidgets.QPushButton, "userSettingsButton")

        # Table Section
        self.filterCombo = self.findChild(QtWidgets.QComboBox, "filterCombo")
        self.tableWidget = self.findChild(QtWidgets.QTableWidget, "tableWidget")
        self.loadTable() # TODO ! Disable Table Editing and Other Table Features (except selecting a row,column)

        # Sidebar Stacked Widget
        self.sidebar = self.findChild(QtWidgets.QStackedWidget, "sidebar")

        # Default View
        self.sidebar.defaultView = self.findChild(QtWidgets.QWidget, "defaultView")

        # TODO - CHECK IF YOU CAN USE SHORTER NAMES AS REFERENCE

        # View Entry
        self.sidebar.selectedEntryView = self.findChild(QtWidgets.QWidget, "selectedEntryView")
        self.sidebar.selectedEntryView.deleteButton = self.findChild(QtWidgets.QPushButton, "deleteButton")
        self.sidebar.selectedEntryView.editButton = self.findChild(QtWidgets.QPushButton, "editButton")
        self.sidebar.selectedEntryView.entryContentEdit = self.findChild(QtWidgets.QLineEdit, "entryContentEdit")
        self.sidebar.selectedEntryView.entryDescriptionEdit = self.findChild(QtWidgets.QLineEdit, "entryDescriptionEdit")
        self.sidebar.selectedEntryView.entryNameEdit = self.findChild(QtWidgets.QLineEdit, "entryNameEdit")
        self.sidebar.selectedEntryView.entryTypeEdit = self.findChild(QtWidgets.QLineEdit, "entryTypeEdit")

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

        # Connections
        # Topbar
        self.addEntryButton.clicked.connect(self.loadNewEntryView)
        self.userSettingsButton.clicked.connect(self.loadSettingsView)
        self.logoutButton.clicked.connect(self.logout)

        # Table
        # -> Insert Default View Button Here <-.clicked.connect(self.loadDefault)
        self.cancelButton_3.clicked.connect(self.loadDefault)

        # -> Insert Table Button Connection Here <-.clicked.connect(self.loadSelectedEntryView)
        self.tableWidget.cellClicked.connect(self.loadSelectedEntryView)

        # Sidebar
        # Selected Entry View
        self.deleteButton.clicked.connect(self.deleteEntry)
        self.editButton.clicked.connect(self.editEntry)

        # Delete Account View
        self.deleteAccountButton.clicked.connect(self.loadAccountDeleteView)
        self.cancelButton_2.clicked.connect(self.loadSettingsView)

        # Change Password View
        self.changePasswordButton.clicked.connect(self.loadPasswordChangeView)
        self.cancelButton.clicked.connect(self.loadSettingsView)
    
    # Functions
    def logout(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
        # TODO clear parameters
    
    # TODO ! Modify setting up data from crud | Modify crud | Get Crud Logic
    def loadTable(self):
        # Default Values (for testing purposes)
        input="Name,Type,Description,Password,Name2,Type2,Description2,Password2"
        entries = input.split(",")
        rowCount = int(len(entries)/4)
        row = 0
        self.tableWidget.setRowCount(rowCount)
        index = 0
        for row in range(rowCount):
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(entries[index])))
            index += 1
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(entries[index])))
            index += 1
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(entries[index])))
            index += 2
            row += 1

    def loadDefault(self):
        self.sidebar.setCurrentWidget(self.sidebar.defaultView)
    
    def loadSelectedEntryView(self, row, column):
        # TODO ! Make Entry Content (contents) 'hidden' somehow
        input="Name,Type,Description,Password,Name2,Type2,Description2,Password2"
        entries = input.split(",")
        # Based on crud logic
        startIndex = (row+1)*4 - 4

        self.sidebar.selectedEntryView.entryNameEdit.setText(entries[startIndex])
        startIndex +=1
        self.sidebar.selectedEntryView.entryTypeEdit.setText(entries[startIndex])
        startIndex +=1
        self.sidebar.selectedEntryView.entryDescriptionEdit.setText(entries[startIndex])
        startIndex +=1
        self.sidebar.selectedEntryView.entryContentEdit.setText(entries[startIndex])

        self.sidebar.setCurrentWidget(self.sidebar.selectedEntryView)

    def deleteEntry(self, row):
        # Delete from table
        pass

    def editEntry(self, row):
        # Enable all line edits
        pass

    def loadSettingsView(self):
        self.sidebar.setCurrentWidget(self.sidebar.userSettingView)

    def loadAccountDeleteView(self):
        self.sidebar.setCurrentWidget(self.sidebar.accountDeleteView)

    def loadPasswordChangeView(self):
        self.sidebar.setCurrentWidget(self.sidebar.passwordChangeView)

    def loadNewEntryView(self):
        self.sidebar.setCurrentWidget(self.sidebar.newEntryView)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
loginScreen = LoginScreen()
mainScreen = MainScreen()
widget.addWidget(loginScreen)
widget.addWidget(mainScreen)
widget.setCurrentIndex(0)
widget.show()
sys.exit(app.exec())