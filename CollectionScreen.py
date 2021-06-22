#!/usr/bin/python3

from FlowLayout import FlowLayout
from PyQt5 import QtCore
from PyQt5.QtWidgets import QComboBox, QFrame, QHBoxLayout, QLabel, QScrollArea, QVBoxLayout, QPushButton, QWidget

class CollectionScreen(QFrame):

    def __init__(self, parent): # constructor
        super().__init__(parent)
        self.windowClass = parent # allows calling of parent class methods
        self.setStyleSheet(open('css/window.css').read())
        self.initScreen()

    def initScreen(self):
        verticalBox = QVBoxLayout()
        verticalBox.setAlignment(QtCore.Qt.AlignTop)

        upperHBox = QHBoxLayout()
        upperHBox.setAlignment(QtCore.Qt.AlignLeft)

        scroll = QScrollArea() 
        widget = QWidget() # Widget that contains the flowLayout            

        middleFlowLayout = FlowLayout() # The FlowLayout that contains all of the Collection buttons
        middleFlowLayout.setSpacing(15)

        headerLabel = QLabel('Your Collections', self)
        headerLabel.setStyleSheet(open("css/smallHeaderLabels.css").read())
        headerLabel.setFixedHeight(45)
        upperHBox.addWidget(headerLabel)

        tempCollections = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        for buttonName in tempCollections:
            button = QPushButton(str(buttonName), self)
            button.setMinimumSize(229,229)
            button.setMaximumSize(229,229)
            button.setStyleSheet(open('css/collectionButtons.css').read())
            button.clicked.connect(self.containerScreenEvent)
            middleFlowLayout.addWidget(button)

        newButton = QPushButton('+', self)
        newButton.setMinimumSize(229,229)
        newButton.setMaximumSize(229,229)
        newButton.setStyleSheet(open('css/plusButtons.css').read())
        newButton.clicked.connect(self.chooseScreenEvent)
        middleFlowLayout.addWidget(newButton)

        widget.setContentsMargins(0, 18, 0, 18)
        widget.setLayout(middleFlowLayout)

        #ScrollArea Properties
        scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll.setStyleSheet(open("css/scrollArea.css").read())
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget)

        lowerHBox = QHBoxLayout()
        lowerHBox.setAlignment(QtCore.Qt.AlignRight)

        comboLabel = QLabel('Sort By: ', self)
        comboLabel.setStyleSheet(open("css/smallLabels.css").read())
        comboLabel.setFixedHeight(45)
        lowerHBox.addWidget(comboLabel)
        
        tempSortList = ['Date Created    ', 'Recent', 'Color', 'Value']
        sortCombo = QComboBox(self)
        sortCombo.setEditable(True)
        sortCombo.addItems(tempSortList)
        sortCombo.setEditable(False)
        sortCombo.setFixedWidth(170)
        sortCombo.setStyleSheet(open("css/comboBoxes.css").read())
        #sortCombo.activated.connect(self.sortComboEvent)
        lowerHBox.addWidget(sortCombo)

        lowerHBox.addSpacing(999999) # large number to ensure max distance

        backButton = QPushButton('\u21A9', self) 
        backButton.setMinimumSize(50,50)
        backButton.setMaximumSize(50,50)
        backButton.setStyleSheet(open('css/returnButtons.css').read())
        backButton.clicked.connect(self.launchScreenEvent)
        lowerHBox.addWidget(backButton)

        verticalBox.addLayout(upperHBox) 
        verticalBox.addWidget(scroll)
        verticalBox.addSpacing(10) 
        verticalBox.addLayout(lowerHBox)

        self.setLayout(verticalBox)

    # navigation events
    def launchScreenEvent(self):
        self.windowClass.launchScreen()

    def chooseScreenEvent(self):
        self.windowClass.chooseScreen() 

    def containerScreenEvent(self):
        self.windowClass.containerScreen()