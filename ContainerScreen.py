#!/usr/bin/python3

from PyQt5 import QtWidgets
from FlowLayout import FlowLayout
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QComboBox, QFrame, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QScrollArea, QVBoxLayout, QPushButton, QWidget

class ContainerScreen(QFrame):

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
        self.upperHBox.setAlignment(QtCore.Qt.AlignRight)

        self.scrollArea = QScrollArea() 
        self.widget = QWidget() # Widget that contains the flowLayout            

        self.middleFlowLayout = FlowLayout() # The FlowLayout that contains all of the Collection buttons
        self.middleFlowLayout.setSpacing(15)

        self.upperInHBox = QHBoxLayout()
        self.upperInHBox.setAlignment(QtCore.Qt.AlignLeft)

        self.editNameButton = QPushButton('\U0001F589',self)
        self.editNameButton.setFixedSize(45,45)
        self.editNameButton.setStyleSheet(open('css/pencilButtons.css').read())
        self.editNameButton.clicked.connect(self.editNameEvent)
        self.upperInHBox.addWidget(self.editNameButton)

        self.headerLabel = QLabel('Collection Name', self)
        self.headerLabel.setStyleSheet(open("css/smallHeaderLabels.css").read())
        self.headerLabel.setFixedSize(999999,45)
        self.upperInHBox.addWidget(self.headerLabel)

        self.editNameBox = QLineEdit(self)
        self.editNameBox.setFixedSize(715,45)
        self.editNameBox.returnPressed.connect(self.changeNameEvent)
        self.editNameBox.setStyleSheet(open("css/textBoxes.css").read())
        self.upperInHBox.addWidget(self.editNameBox)
        self.editNameBox.setHidden(True)

        self.upperHBox.addLayout(self.upperInHBox)

        self.sideLabel = QLabel('Information', self)
        self.sideLabel.setStyleSheet(open("css/smallHeaderLabels.css").read())
        self.sideLabel.setFixedSize(237,45)
        self.upperHBox.addWidget(self.sideLabel)

        tempCollections = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        for buttonName in tempCollections:
            self.button = QPushButton(str(buttonName), self)
            self.button.setFixedSize(229,229)
            self.button.setStyleSheet(open('css/collectionButtons.css').read())
            self.button.installEventFilter(self)
            self.button.clicked.connect(self.listScreenEvent)
            self.middleFlowLayout.addWidget(self.button)

        self.newButton = QPushButton('+', self)
        self.newButton.setFixedSize(229,229)
        self.newButton.setStyleSheet(open('css/plusButtons.css').read())
        self.newButton.clicked.connect(self.listScreenEvent)
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
        self.backButton.clicked.connect(self.collectionScreenEvent)
        self.lowerHBox.addWidget(self.backButton)

        # right side panel related widgets
        self.middleHBox = QHBoxLayout()

        self.rightMiddleVerticalBox = QVBoxLayout()
        self.rightMiddleVerticalBox.setAlignment(QtCore.Qt.AlignTop)

        self.sideLabel2 = QLabel('Stuff goes here', self)
        self.sideLabel2.setStyleSheet(open("css/regularLabels.css").read())
        self.sideLabel2.setFixedSize(237,45)
        self.rightMiddleVerticalBox.addWidget(self.sideLabel2)

        self.rightMiddleVerticalBox.addSpacing(999999) # large number to ensure max distance
        
        self.ColorButtonHBox1 = QHBoxLayout()
        tempCollections = ['c0','c1','c2','c3','c4']
        for buttonName in tempCollections:
            self.button = QPushButton(str(buttonName), self)
            self.button.setFixedSize(40,40)
            self.button.setStyleSheet(open('css/colorButtons.css').read()) # when implemented with controller, css will be dynamically chosen (there will be 10 color choices)
            self.ColorButtonHBox1.addWidget(self.button)
        self.rightMiddleVerticalBox.addLayout(self.ColorButtonHBox1)

        self.ColorButtonHBox2 = QHBoxLayout()
        tempCollections = ['c5','c6','c7','c8','c9']
        for buttonName in tempCollections:
            self.button = QPushButton(str(buttonName), self)
            self.button.setFixedSize(40,40)
            self.button.setStyleSheet(open('css/colorButtons.css').read()) # when implemented with controller, css will be dynamically chosen (there will be 10 color choices)
            self.ColorButtonHBox2.addWidget(self.button)    
        self.rightMiddleVerticalBox.addLayout(self.ColorButtonHBox2)

        #rightMiddleVerticalBox.addSpacing(20)

        self.verticalBox.addLayout(self.upperHBox) 
        self.verticalBox.addLayout(self.middleHBox)
        self.middleHBox.addWidget(self.scrollArea)
        self.middleHBox.addLayout(self.rightMiddleVerticalBox)
        self.verticalBox.addSpacing(10) 
        self.verticalBox.addLayout(self.lowerHBox)
        self.setLayout(self.verticalBox)

    # navigation events
    def collectionScreenEvent(self):
        self.windowClass.collectionScreen()

    def listScreenEvent(self):
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        
        if modifiers == QtCore.Qt.ShiftModifier:
            # I need some way to store the button that is clicked
            deleteMsg = QMessageBox()
            deleteMsg.setWindowTitle(' ')
            deleteMsg.setText('Do you want to delete this container?')
            deleteMsg.setInformativeText('This action cannot be undone.')
            #deleteMsg.setWindowIcon(QtGui.QIcon('images/Zoe_Icon_48x48.png')) # this icon will eventually be whatever the program icon will be
            deleteMsg.setIconPixmap(QtGui.QPixmap("images/Zoe_Icon_48x48.png"))
            deleteMsg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            deleteMsg.setDefaultButton(QMessageBox.No)
            deleteMsg.buttonClicked.connect(self.deleteEvent)
            deleteMsg.exec_()
        else:
            self.windowClass.listScreen()

    # delete event
    def deleteEvent(self, response):
        print(response.text())

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

    # search event
    def searchEvent(self):
        print('Search Event yet to be created')