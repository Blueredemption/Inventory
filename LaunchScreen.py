#!/usr/bin/python3

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QLabel

class LaunchScreen(QFrame):

    def __init__(self, parent): # constructor
        super().__init__(parent)
        self.windowClass = parent # allows calling of parent class methods
        self.setStyleSheet(open('css/window.css').read())
        self.initScreen()

    def initScreen(self): # gui
        QtGui.QFontDatabase.addApplicationFont("fonts\Lora\static\Lora-Regular.ttf")

        self.verticalBox = QVBoxLayout()
        self.verticalBox.setAlignment(QtCore.Qt.AlignTop)
        self.upperHBox = QHBoxLayout()
        self.upperHBox.setAlignment(QtCore.Qt.AlignCenter)
        self.lowerHBox = QHBoxLayout()
        self.lowerHBox.setAlignment(QtCore.Qt.AlignCenter)
        self.lowerHBox.setSpacing(50)
        self.lowerHBox.setContentsMargins(50, 50, 50, 50)

        self.upperHBox.addSpacing(35)
        
        self.titleLabel = QLabel('Inventory', self)
        self.titleLabel.setStyleSheet(open("css/titleLabels.css").read())
        self.titleLabel.setFixedSize(650,195)
        self.upperHBox.addWidget(self.titleLabel)

        self.collectionsButton = QPushButton('Access Your\nCollections', self)
        self.collectionsButton.setFixedSize(350,350)
        self.collectionsButton.setStyleSheet(open('css/bigButtons.css').read())
        self.collectionsButton.clicked.connect(self.collectionEvent)
        self.lowerHBox.addWidget(self.collectionsButton)

        self.newButton = QPushButton('Make A New\nCollection', self) 
        self.newButton.setFixedSize(350,350)
        self.newButton.setStyleSheet(open('css/bigButtons.css').read())
        self.newButton.clicked.connect(self.newEvent)
        self.lowerHBox.addWidget(self.newButton)

        self.verticalBox.addLayout(self.upperHBox)
        self.verticalBox.addLayout(self.lowerHBox)
        self.setLayout(self.verticalBox)

    # navigation events
    def collectionEvent(self):
        self.windowClass.collectionScreen() 

    def newEvent(self):
        self.windowClass.chooseScreen() 