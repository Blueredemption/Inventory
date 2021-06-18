#!/usr/bin/python3

import sys

from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication

from LaunchScreen import LaunchScreen
from ChooseScreen import ChooseScreen

class Action(QMainWindow):

    def __init__(self): # constructor
        super().__init__()
        
        self.setSize()
        self.setWindowTitle('Inventory')
        self.setStyleSheet('background-color: rgb(90, 131, 199)')
        self.launchScreen() # initiates the program at the lauch screen

        ## Launches the Controller

            ## Launches the GuiDao --- Storage of graphics information (application settings etc.)
        
            ## Launches the CardDao --- Uses API to access card information 

            ## Launches the UserDao --- Storage of user's data

    ## Launch the individual pages
    def launchScreen(self):
        self.launchScreenObject = LaunchScreen(self)
        self.setCentralWidget(self.launchScreenObject)
        self.show()

    def chooseScreen(self):
        self.chooseScreenObject = ChooseScreen(self)
        self.setCentralWidget(self.chooseScreenObject)
        self.show()

    ##










    def setSize(self):
        ## Sets the window location on the screen
        screen = QDesktopWidget().screenGeometry()
        #self.setMinimumSize(1344,756) # set minimum size
        self.resize(1344,756) # set down size
        size = self.geometry() # determining screen location
        self.move(int((screen.width() - size.width()) / 2),
                  int((screen.height() - size.height()) / 2))
        self.showMaximized() # setting window to maximized

def main():
    app = QApplication([])
    window = Action()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()