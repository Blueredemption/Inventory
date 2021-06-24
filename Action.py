#!/usr/bin/python3

import sys

from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication

from LaunchScreen import LaunchScreen
from CollectionScreen import CollectionScreen
from ChooseScreen import ChooseScreen
from ContainerScreen import ContainerScreen
from ListScreen import ListScreen
from SearchScreen import SearchScreen

class Action(QMainWindow):

    def __init__(self): # constructor
        super().__init__()
        
        #self.setSize() # this makes the program open full screen
        self.setMinimumSize(1000,700)
        self.setWindowTitle('Inventory')
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

    def collectionScreen(self):
        self.collectionScreenObject = CollectionScreen(self)
        self.setCentralWidget(self.collectionScreenObject)
        self.show()

    def chooseScreen(self):
        self.chooseScreenObject = ChooseScreen(self)
        self.setCentralWidget(self.chooseScreenObject)
        self.show()

    def containerScreen(self):
        self.containerScreenObject = ContainerScreen(self)
        self.setCentralWidget(self.containerScreenObject)
        self.show() 

    def listScreen(self):
        self.listScreenObject = ListScreen(self)
        self.setCentralWidget(self.listScreenObject)
        self.show()

    def searchScreen(self):
        self.searchScreenObject = SearchScreen(self)
        self.setCentralWidget(self.searchScreenObject)
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