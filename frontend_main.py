# Imports - to be polished
import sys
import PyQt5
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

# Functions / Methods
# Using loadUI due to mainly using QtDesigner for layout editing

class LoginScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        uic.loadUi("ui/LoginScreen.ui", self)
        
        # Definitions
        self.usernameEdit = self.findChild(QtWidgets.QPushButton, "usernameEdit")
        self.passwordEdit = self.findChild(QtWidgets.QPushButton, "passwordEdit")
        self.loginButton = self.findChild(QtWidgets.QPushButton, "loginButton")
        self.signupButton = self.findChild(QtWidgets.QPushButton, "signupButton")
        
        self.loginButton.clicked.connect(self.loadMain)

    def loadMain(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

class MainScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        uic.loadUi("ui/MainScreen.ui", self)

    def logout(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def loadDefault():
        pass
    
    def loadView():
        pass

    def loadSettings():
        pass

    def loadDeletion():
        pass

    def loadChange():
        pass

    def loadAdd():
        pass


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
loginScreen = LoginScreen()
mainScreen = MainScreen()
widget.addWidget(loginScreen)
widget.addWidget(mainScreen)
widget.setCurrentIndex(0)
widget.show()
sys.exit(app.exec())