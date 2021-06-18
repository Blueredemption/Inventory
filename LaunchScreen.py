#!/usr/bin/python3

from PyQt5.QtWidgets import QFrame, QPushButton

class LaunchScreen(QFrame):

    def __init__(self, parent): # constructor
        super().__init__(parent)
        self.windowClass = parent # allows calling of parent class methods
        self.setStyleSheet('background-color: rgb(230, 50, 199)')
        self.initScreen()

    def initScreen(self):
        button = QPushButton('I change to Choose Screen', self)
        button.clicked.connect(self.buttonEvent)
        button.show()

    def buttonEvent(self):
        self.windowClass.chooseScreen() 