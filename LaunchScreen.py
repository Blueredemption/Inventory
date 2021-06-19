#!/usr/bin/python3

from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QLabel

class LaunchScreen(QFrame):

    def __init__(self, parent): # constructor
        super().__init__(parent)
        self.windowClass = parent # allows calling of parent class methods
        self.setStyleSheet(open('css/window.css').read())
        self.initScreen()

    def initScreen(self): # 
        verticalBox = QVBoxLayout()
        verticalBox.setAlignment(QtCore.Qt.AlignTop)
        upperHBox = QHBoxLayout()
        upperHBox.setAlignment(QtCore.Qt.AlignCenter)
        lowerHBox = QHBoxLayout()
        lowerHBox.setAlignment(QtCore.Qt.AlignCenter)
        lowerHBox.setSpacing(50)
        lowerHBox.setContentsMargins(50, 50, 50, 50)

        titleLabel = QLabel('Inventory', self)
        titleLabel.setStyleSheet(open("css/titleLabels.css").read())
        titleLabel.setMinimumSize(650,190)
        titleLabel.setMaximumSize(650,190)
        upperHBox.addWidget(titleLabel)

        collectionsButton = QPushButton('Access Your\nCollections', self)
        collectionsButton.setMinimumSize(350,350)
        collectionsButton.setMaximumSize(350,350)
        collectionsButton.setStyleSheet(open('css/bigButtons.css').read())
        collectionsButton.clicked.connect(self.collectionEvent)
        lowerHBox.addWidget(collectionsButton)

        newButton = QPushButton('Make A New\nCollection', self) 
        #newButton.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        newButton.setMinimumSize(350,350)
        newButton.setMaximumSize(350,350)
        newButton.setStyleSheet(open('css/bigButtons.css').read())
        newButton.clicked.connect(self.newEvent)
        lowerHBox.addWidget(newButton)

        verticalBox.addLayout(upperHBox)
        verticalBox.addLayout(lowerHBox)

        self.setLayout(verticalBox)

    # Events
    def collectionEvent(self):
        self.windowClass.collectionScreen() 

    def newEvent(self):
        self.windowClass.chooseScreen() 