#!/usr/bin/python3

from PyQt5 import QtGui, QtWidgets
from FlowLayout import FlowLayout
from PyQt5 import QtCore
from PyQt5.QtWidgets import QCheckBox, QComboBox, QFrame, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QScrollArea, QVBoxLayout, QPushButton, QWidget

class SearchScreen(QFrame):

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

        self.middleFullHLayout = QHBoxLayout()

        self.scrollArea = QScrollArea() 
        self.scrollWidget = QWidget() # Widget that contains the flowLayout

        self.middleVLayout = QVBoxLayout() # contains checkboxes
        self.middleVLayout.setAlignment(QtCore.Qt.AlignTop)

        self.colorLabel = QLabel('Color', self)
        self.colorLabel.setStyleSheet(open('css/smallLabels.css').read())
        self.colorLabel.setFixedWidth(120)
        self.middleVLayout.addWidget(self.colorLabel)

        colorFields = ['Red', 'Blue', 'Black', 'White', 'Green', 'Colorless']
        for field in colorFields:
            self.box = QCheckBox(field)
            self.box.setChecked(True) # this will be controlled by the controller so they are the same when returning to the page after exiting the page
            self.box.stateChanged.connect(lambda:self.checkState(self.box))
            self.box.setStyleSheet(open('css/checkBoxes.css').read())
            self.middleVLayout.addWidget(self.box)

        self.colorLabel = QLabel('Type', self)
        self.colorLabel.setStyleSheet(open('css/smallLabels.css').read())
        self.middleVLayout.addWidget(self.colorLabel)

        typeFields = ['Creature', 'Legendary', 'Planeswalker', 'Artifact', 'Instant', 'Sorcery', 'Enchantment', 'Land']
        for field in typeFields:
            self.box = QCheckBox(field)
            self.box.setChecked(True) # this will be controlled by the controller so they are the same when returning to the page after exiting the page
            self.box.stateChanged.connect(lambda:self.checkState(self.box))
            self.box.setStyleSheet(open('css/checkBoxes.css').read())
            self.middleVLayout.addWidget(self.box)

        self.colorLabel = QLabel('Rarity', self)
        self.colorLabel.setStyleSheet(open('css/smallLabels.css').read())
        self.middleVLayout.addWidget(self.colorLabel)

        rarityFields = ['Common', 'Uncommon', 'Rare', 'Mythic']
        for field in rarityFields:
            self.box = QCheckBox(field)
            self.box.setChecked(True) # this will be controlled by the controller so they are the same when returning to the page after exiting the page
            self.box.stateChanged.connect(lambda:self.checkState(self.box))
            self.box.setStyleSheet(open('css/checkBoxes.css').read())
            self.middleVLayout.addWidget(self.box)

        self.middleV2Layout = QVBoxLayout() # contains scrollable results
        self.middleV2Layout.setSpacing(15)

        self.headerLabel = QLabel('Search:', self)
        self.headerLabel.setStyleSheet(open('css/searchHeader.css').read())
        self.headerLabel.setFixedSize(105,35)
        self.upperHBox.addWidget(self.headerLabel)

        self.searchBox = QLineEdit(self)
        self.searchBox.setFixedSize(600,35)
        #self.searchBox.returnPressed.connect(self.searchEvent)
        self.searchBox.setStyleSheet(open('css/searchHeader.css').read())
        self.upperHBox.addWidget(self.searchBox)

        self.searchBox.setFocus()

        self.leftMiddleVerticalBox = QVBoxLayout()
        self.leftMiddleVerticalBox.setAlignment(QtCore.Qt.AlignTop)

        for i in range(1, 21):
            self.listHBox = QHBoxLayout()
            
            self.button = QPushButton(str(i), self)
            self.button.setFixedSize(47,65)
            self.button.setStyleSheet(open('css/smallButtons.css').read())
            self.button.clicked.connect(self.detailScreenEvent)
            self.button.installEventFilter(self)
            self.listHBox.addWidget(self.button)

            for j in range(1, 4):
                self.listLabel = QLabel(str(i) +' '  +str(j) +' Information\n' +str(i) +' '  +str(j) +' Information', self)
                self.listLabel.setStyleSheet(open("css/smallLabels.css").read())
                self.listLabel.installEventFilter(self)
                self.listHBox.addWidget(self.listLabel)

            self.leftMiddleVerticalBox.addLayout(self.listHBox)

        self.scrollWidget.setContentsMargins(0, 9, 0, 9)
        self.scrollWidget.setLayout(self.leftMiddleVerticalBox)

        #ScrollArea Properties
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setStyleSheet(open('css/scrollArea.css').read())
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)

        self.lowerHBox = QHBoxLayout()
        self.lowerHBox.setAlignment(QtCore.Qt.AlignRight)

        self.lowerHBox.addSpacing(999999) # large number to ensure max distance

        self.backButton = QPushButton('\u21A9', self) 
        self.backButton.setFixedSize(50,50)
        self.backButton.setStyleSheet(open('css/returnButtons.css').read())
        self.backButton.clicked.connect(self.listScreenEvent)
        self.lowerHBox.addWidget(self.backButton)

        self.verticalBox.addLayout(self.upperHBox)
        self.middleFullHLayout.addLayout(self.middleVLayout)
        self.middleFullHLayout.addWidget(self.scrollArea)
        self.verticalBox.addLayout(self.middleFullHLayout)
        self.verticalBox.addSpacing(10) 
        self.verticalBox.addLayout(self.lowerHBox)
        self.setLayout(self.verticalBox)

    # navigation events
    def detailScreenEvent(self):
        self.windowClass.chooseScreen() 

    def listScreenEvent(self):
        self.windowClass.listScreen()
        
    # search event
    def searchEvent(self):
        print('Search Event yet to be created')

    # checkBoxes event
    def checkState(self,b):
        if b.isChecked() == True:
            print(b.text()+" is selected")
        else:
            print (b.text()+" is deselected")
