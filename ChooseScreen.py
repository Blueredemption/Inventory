#!/usr/bin/python3

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import  QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QLabel

class ChooseScreen(QFrame):

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
        self.middleHBox = QHBoxLayout()
        self.middleHBox.setAlignment(QtCore.Qt.AlignCenter)
        self.middleHBox.setSpacing(50)
        self.middleHBox.setContentsMargins(50, 50, 50, 50)
        self.lowerHBox = QHBoxLayout()
        self.lowerHBox.setAlignment(QtCore.Qt.AlignRight)
        self.upperHBox.addSpacing(122)

        self.headerLabel = QLabel('What Game?', self)
        self.headerLabel.setStyleSheet(open("css/headerLabels.css").read())
        self.headerLabel.setFixedSize(490,195)
        self.upperHBox.addWidget(self.headerLabel)

        self.mtgButton = QPushButton('', self)
        self.mtgButton.setFixedSize(350,350)
        self.mtgButton.setStyleSheet(open('css/mtgButton.css').read())
        self.mtgButton.clicked.connect(self.containerScreenEvent)
        self.middleHBox.addWidget(self.mtgButton)

        self.soonButton = QPushButton('Coming Soon...?', self) 
        self.soonButton.setFixedSize(350,350)
        self.soonButton.setStyleSheet(open('css/bigButtons.css').read())
        self.soonButton.setEnabled(False)
        self.middleHBox.addWidget(self.soonButton)

        self.backButton = QPushButton('\u21A9', self) 
        self.backButton.setFixedSize(50,50)
        self.backButton.setStyleSheet(open('css/returnButtons.css').read())
        self.backButton.clicked.connect(self.launchScreenEvent)
        self.lowerHBox.addWidget(self.backButton)

        self.verticalBox.addLayout(self.upperHBox)
        self.verticalBox.addLayout(self.middleHBox)
        self.verticalBox.addSpacing(999999) # large number to ensure max distance
        self.verticalBox.addLayout(self.lowerHBox)
        self.setLayout(self.verticalBox)

    # navigation events
    def launchScreenEvent(self):
        self.windowClass.launchScreen() 
    
    def containerScreenEvent(self):
        self.windowClass.containerScreen() 