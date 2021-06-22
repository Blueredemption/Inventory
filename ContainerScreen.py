#!/usr/bin/python3

from FlowLayout import FlowLayout
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QComboBox, QFrame, QHBoxLayout, QLabel, QLineEdit, QScrollArea, QVBoxLayout, QPushButton, QWidget

class ContainerScreen(QFrame):

    def __init__(self, parent): # constructor
        super().__init__(parent)
        self.windowClass = parent # allows calling of parent class methods
        self.setStyleSheet(open('css/window.css').read())
        self.initScreen()

    def initScreen(self):
        verticalBox = QVBoxLayout()
        verticalBox.setAlignment(QtCore.Qt.AlignTop)

        upperHBox = QHBoxLayout()
        upperHBox.setAlignment(QtCore.Qt.AlignRight)

        scroll = QScrollArea() 
        widget = QWidget() # Widget that contains the flowLayout            

        middleFlowLayout = FlowLayout() # The FlowLayout that contains all of the Collection buttons
        middleFlowLayout.setSpacing(15)

        upperInHBox = QHBoxLayout()
        upperInHBox.setAlignment(QtCore.Qt.AlignLeft)
        upperInHBox.setGeometry

        self.editNameButton = QPushButton('\U0001F589',self)
        self.editNameButton.setMinimumSize(45,45)
        self.editNameButton.setMaximumSize(45,45)
        self.editNameButton.setStyleSheet(open('css/pencilButtons.css').read())
        self.editNameButton.clicked.connect(self.editNameEvent)
        upperInHBox.addWidget(self.editNameButton)

        self.headerLabel = QLabel('Collection Name', self)
        self.headerLabel.setStyleSheet(open("css/smallHeaderLabels.css").read())
        self.headerLabel.setFixedSize(999999,45)
        upperInHBox.addWidget(self.headerLabel)

        self.editNameBox = QLineEdit(self)
        self.editNameBox.setFixedWidth(320)
        self.editNameBox.setFixedHeight(45)
        self.editNameBox.returnPressed.connect(self.changeNameEvent)
        self.editNameBox.setStyleSheet(open("css/textBoxes.css").read())
        upperInHBox.addWidget(self.editNameBox)
        self.editNameBox.setHidden(True)

        upperHBox.addLayout(upperInHBox)

        self.sideLabel = QLabel('Information', self)
        self.sideLabel.setStyleSheet(open("css/smallHeaderLabels.css").read())
        self.sideLabel.setFixedHeight(45)
        self.sideLabel.setFixedWidth(237)
        upperHBox.addWidget(self.sideLabel)

        tempCollections = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        for buttonName in tempCollections:
            button = QPushButton(str(buttonName), self)
            button.setMinimumSize(229,229)
            button.setMaximumSize(229,229)
            button.setStyleSheet(open('css/collectionButtons.css').read())
            button.installEventFilter(self)
            button.clicked.connect(self.listScreenEvent)
            middleFlowLayout.addWidget(button)

        newButton = QPushButton('+', self)
        newButton.setMinimumSize(229,229)
        newButton.setMaximumSize(229,229)
        newButton.setStyleSheet(open('css/plusButtons.css').read())
        newButton.clicked.connect(self.listScreenEvent)
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
        backButton.clicked.connect(self.collectionScreenEvent)
        lowerHBox.addWidget(backButton)

        # right side panel related widgets
        middleHBox = QHBoxLayout()

        rightMiddleVerticalBox = QVBoxLayout()
        rightMiddleVerticalBox.setAlignment(QtCore.Qt.AlignTop)

        self.sideLabel2 = QLabel('Stuff goes here', self)
        self.sideLabel2.setStyleSheet(open("css/regularLabels.css").read())
        self.sideLabel2.setFixedHeight(45)
        self.sideLabel2.setFixedWidth(237)
        rightMiddleVerticalBox.addWidget(self.sideLabel2)

        rightMiddleVerticalBox.addSpacing(999999) # large number to ensure max distance
        
        ColorButtonHBox1 = QHBoxLayout()
        tempCollections = ['c0','c1','c2','c3','c4']
        for buttonName in tempCollections:
            button = QPushButton(str(buttonName), self)
            button.setMinimumSize(40,40)
            button.setMaximumSize(40,40)
            button.setStyleSheet(open('css/collectionButtons.css').read()) # when implemented with controller, css will be dynamically chosen (there will be 10 color choices)
            ColorButtonHBox1.addWidget(button)
        rightMiddleVerticalBox.addLayout(ColorButtonHBox1)

        ColorButtonHBox2 = QHBoxLayout()
        tempCollections = ['c5','c6','c7','c8','c9']
        for buttonName in tempCollections:
            button = QPushButton(str(buttonName), self)
            button.setMinimumSize(40,40)
            button.setMaximumSize(40,40)
            button.setStyleSheet(open('css/collectionButtons.css').read()) # when implemented with controller, css will be dynamically chosen (there will be 10 color choices)
            ColorButtonHBox2.addWidget(button)    
        rightMiddleVerticalBox.addLayout(ColorButtonHBox2)

        #rightMiddleVerticalBox.addSpacing(20)

        verticalBox.addLayout(upperHBox) 
        verticalBox.addLayout(middleHBox)
        middleHBox.addWidget(scroll)
        middleHBox.addLayout(rightMiddleVerticalBox)
        verticalBox.addSpacing(10) 
        verticalBox.addLayout(lowerHBox)

        self.setLayout(verticalBox)

    # navigation events
    def collectionScreenEvent(self):
        self.windowClass.collectionScreen()

    def listScreenEvent(self):
        self.windowClass.listScreen()

    # hover events
    def eventFilter(self, object, event): # this is going to be a switch statement into more specific methods if / once I have to filter more than one objects event
        if event.type() == 10: # event 10 is mouse entering the button
            self.sideLabel.setText("Cont. Name")
            self.sideLabel2.setText("Container Info")
            return True
        elif event.type() == 11: # event 11 is mouse leaving the button
            self.sideLabel.setText("Information")
            self.sideLabel2.setText("General Info")
            return True
        return False

    # other events
    def editNameEvent(self):
        self.headerLabel.setHidden(True)
        self.editNameBox.setHidden(False)
        self.editNameButton.setHidden(True)
        self.editNameBox.setFocus(True)

    def changeNameEvent(self):
        self.headerLabel.setHidden(False)
        self.editNameBox.setText('')
        self.editNameBox.setHidden(True)
        self.editNameButton.setHidden(False)
        # controller does something with this information
