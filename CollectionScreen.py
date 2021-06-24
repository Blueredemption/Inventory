#!/usr/bin/python3

from PyQt5 import QtGui, QtWidgets
from FlowLayout import FlowLayout
from PyQt5 import QtCore
from PyQt5.QtWidgets import QComboBox, QFrame, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QScrollArea, QVBoxLayout, QPushButton, QWidget

class CollectionScreen(QFrame):

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
        self.upperHBox.setAlignment(QtCore.Qt.AlignLeft)

        self.scrollArea = QScrollArea() 
        self.widget = QWidget() # Widget that contains the flowLayout            

        self.middleFlowLayout = FlowLayout() # The FlowLayout that contains all of the Collection buttons
        self.middleFlowLayout.setSpacing(15)

        self.headerLabel = QLabel('Your Collections', self)
        self.headerLabel.setStyleSheet(open("css/smallHeaderLabels.css").read())
        self.headerLabel.setFixedHeight(45)
        self.upperHBox.addWidget(self.headerLabel)

        tempCollections = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        for buttonName in tempCollections:
            self.button = QPushButton(str(buttonName), self)
            self.button.setFixedSize(229,229)
            self.button.setStyleSheet(open('css/collectionButtons.css').read())
            self.button.clicked.connect(self.containerScreenEvent)
            self.middleFlowLayout.addWidget(self.button)

        self.newButton = QPushButton('+', self)
        self.newButton.setFixedSize(229,229)
        self.newButton.setStyleSheet(open('css/plusButtons.css').read())
        self.newButton.clicked.connect(self.chooseScreenEvent)
        self.middleFlowLayout.addWidget(self.newButton)

        self.widget.setContentsMargins(0, 18, 0, 18)
        self.widget.setLayout(self.middleFlowLayout)

        #ScrollArea Properties
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setStyleSheet(open("css/scrollArea.css").read())
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widget)

        self.lowerHBox = QHBoxLayout()
        self.lowerHBox.setAlignment(QtCore.Qt.AlignRight)

        self.comboLabel = QLabel('Sort By: ', self)
        self.comboLabel.setStyleSheet(open("css/smallLabels.css").read())
        self.comboLabel.setFixedHeight(45)
        self.lowerHBox.addWidget(self.comboLabel)
        
        tempSortList = ['Date Created    ', 'Recent', 'Color', 'Value']
        self.sortCombo = QComboBox(self)
        self.sortCombo.setEditable(True)
        self.sortCombo.addItems(tempSortList)
        self.sortCombo.setEditable(False)
        self.sortCombo.setFixedWidth(170)
        self.sortCombo.setStyleSheet(open("css/comboBoxes.css").read())
        #self.sortCombo.activated.connect(self.sortComboEvent)
        self.lowerHBox.addWidget(self.sortCombo)

        self.lowerHBox.addSpacing(30)

        self.searchLabel = QLabel('Search:', self)
        self.searchLabel.setStyleSheet(open("css/smallLabels.css").read())
        self.searchLabel.setFixedSize(80,45)
        self.lowerHBox.addWidget(self.searchLabel)

        self.searchBox = QLineEdit(self)
        self.searchBox.setFixedSize(253,35)
        self.searchBox.returnPressed.connect(self.searchEvent)
        self.searchBox.setStyleSheet(open("css/searchBoxes.css").read())
        self.lowerHBox.addWidget(self.searchBox)

        self.lowerHBox.addSpacing(999999) # large number to ensure max distance

        self.backButton = QPushButton('\u21A9', self) 
        self.backButton.setFixedSize(50,50)
        self.backButton.setStyleSheet(open('css/returnButtons.css').read())
        self.backButton.clicked.connect(self.launchScreenEvent)
        self.lowerHBox.addWidget(self.backButton)

        self.verticalBox.addLayout(self.upperHBox) 
        self.verticalBox.addWidget(self.scrollArea)
        self.verticalBox.addSpacing(10) 
        self.verticalBox.addLayout(self.lowerHBox)
        self.setLayout(self.verticalBox)

    # navigation events
    def launchScreenEvent(self):
        self.windowClass.launchScreen()

    def chooseScreenEvent(self):
        self.windowClass.chooseScreen() 

    def containerScreenEvent(self):
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        
        if modifiers == QtCore.Qt.ShiftModifier:
            # I need some way to store the button that is clicked
            deleteMsg = QMessageBox()
            deleteMsg.setWindowTitle(' ')
            deleteMsg.setText('Do you want to delete this collection?')
            deleteMsg.setInformativeText('This action cannot be undone.')
            #deleteMsg.setWindowIcon(QtGui.QIcon('images/Zoe_Icon_48x48.png')) # this icon will eventually be whatever the program icon will be
            deleteMsg.setIconPixmap(QtGui.QPixmap("images/Zoe_Icon_48x48.png"))
            deleteMsg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            deleteMsg.setDefaultButton(QMessageBox.No)
            deleteMsg.buttonClicked.connect(self.deleteEvent)
            deleteMsg.exec_()
        else:
            self.windowClass.containerScreen()

    # delete event
    def deleteEvent(self, response):
        print(response.text())
    
    # search event
    def searchEvent(self):
        print('Search Event yet to be created')