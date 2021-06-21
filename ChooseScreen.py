#!/usr/bin/python3

from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QLabel

class ChooseScreen(QFrame):

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
        middleHBox = QHBoxLayout()
        middleHBox.setAlignment(QtCore.Qt.AlignCenter)
        middleHBox.setSpacing(50)
        middleHBox.setContentsMargins(50, 50, 50, 50)
        lowerHBox = QHBoxLayout()
        lowerHBox.setAlignment(QtCore.Qt.AlignRight)

        headerLabel = QLabel('What Game?', self)
        headerLabel.setStyleSheet(open("css/headerLabels.css").read())
        headerLabel.setMinimumSize(450,190)
        headerLabel.setMaximumSize(450,190)
        upperHBox.addWidget(headerLabel)

        mtgButton = QPushButton('', self)
        mtgButton.setMinimumSize(350,350)
        mtgButton.setMaximumSize(350,350)
        mtgButton.setStyleSheet(open('css/mtgButton.css').read())
        mtgButton.clicked.connect(self.containerScreenEvent)
        middleHBox.addWidget(mtgButton)

        soonButton = QPushButton('Coming Soon...?', self) 
        soonButton.setMinimumSize(350,350)
        soonButton.setMaximumSize(350,350)
        soonButton.setStyleSheet(open('css/bigButtons.css').read())
        soonButton.setEnabled(False)
        middleHBox.addWidget(soonButton)

        backButton = QPushButton('\u21A9', self) 
        backButton.setMinimumSize(50,50)
        backButton.setMaximumSize(50,50)
        backButton.setStyleSheet(open('css/returnButtons.css').read())
        backButton.clicked.connect(self.launchScreenEvent)
        lowerHBox.addWidget(backButton)

        verticalBox.addLayout(upperHBox)
        verticalBox.addLayout(middleHBox)
        verticalBox.addSpacing(999999) # large number to ensure max distance
        verticalBox.addLayout(lowerHBox)

        self.setLayout(verticalBox)

    # navigation events
    def launchScreenEvent(self):
        self.windowClass.launchScreen() 
    
    def containerScreenEvent(self):
        self.windowClass.containerScreen() 