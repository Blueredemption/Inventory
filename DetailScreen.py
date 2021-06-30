#!/usr/bin/python3

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QCheckBox, QComboBox, QFrame, QHBoxLayout, QLabel, QRadioButton, QSizePolicy, QVBoxLayout, QPushButton

class DetailScreen(QFrame):

    def __init__(self, parent): # constructor
        super().__init__(parent)
        self.windowClass = parent # allows calling of parent class methods
        self.setStyleSheet(open('css/window.css').read())
        self.initScreen()

    def initScreen(self): # gui
        QtGui.QFontDatabase.addApplicationFont("fonts\Lora\static\Lora-Regular.ttf")

        self.verticalBox = QVBoxLayout()
        self.verticalBox.setAlignment(QtCore.Qt.AlignTop)

        self.middleHBox = QHBoxLayout()
        self.middleHBox.setAlignment(QtCore.Qt.AlignCenter)
        
        self.middleLeftVBox = QVBoxLayout()
        self.middleLeftVBox.setAlignment(QtCore.Qt.AlignLeft)

        self.middleRightVBox = QVBoxLayout()
        self.middleRightVBox.setAlignment(QtCore.Qt.AlignTop)
        self.middleRightVBox.setContentsMargins(10, 1, 1, 0)

        self.lowerHBox = QHBoxLayout()
        self.lowerHBox.setAlignment(QtCore.Qt.AlignRight)

        self.headerLabel = QLabel('Card Name', self)
        self.headerLabel.setStyleSheet(open("css/smallHeaderLabels.css").read())
        self.headerLabel.setFixedHeight(45)
        self.middleLeftVBox.addWidget(self.headerLabel)

        self.largeLabel = QLabel('Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?')
        self.largeLabel.setWordWrap(True)
        self.largeLabel.setAlignment(QtCore.Qt.AlignTop)
        self.largeLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.largeLabel.setStyleSheet(open('css/smallLabels.css').read())
        self.middleLeftVBox.addWidget(self.largeLabel)

        self.imageLabel = QLabel('', self)
        self.imageLabel.setStyleSheet('QLabel {background-color: blue;}') # this will just be an image added by the controller, hence the lack of a .css file
        self.imageLabel.setFixedSize(444,620)
        self.middleRightVBox.addWidget(self.imageLabel)

        self.box = QCheckBox('Foil')
        self.box.setChecked(False) # this will be controlled by the controller so they are the same when returning to the page after exiting the page
        self.box.stateChanged.connect(lambda:self.checkState(self.box))
        self.box.setStyleSheet(open('css/smallLabels.css').read())
        self.lowerHBox.addWidget(self.box)

        self.lowerHBox.addSpacing(20)

        conditions = ['Near Mint','Lightly Played','Moderately Played','Heavily Played','Damaged']
        for index, condition in enumerate(conditions):
            self.radioButton = QRadioButton(condition)
            if (index == 0): self.radioButton.setChecked(True)
            self.radioButton.condition = condition
            self.radioButton.setStyleSheet(open('css/smallLabels.css').read())
            self.radioButton.toggled.connect(self.radioButtonEvent)
            self.lowerHBox.addWidget(self.radioButton)

        self.spacerLabel = QLabel('', self)
        self.spacerLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.lowerHBox.addWidget(self.spacerLabel)

        if (True): # need controller
            self.addButton = QPushButton('Add Card', self)
            self.addButton.setFixedSize(170,35)
            self.addButton.setStyleSheet(open('css/smallButtons.css').read())
            self.addButton.clicked.connect(self.addCardEvent)
            self.lowerHBox.addWidget(self.addButton)
        else:
            tempList = ['Move Card', 'Remove Card', 'Container 1', 'Container 2', 'Container 3', 'Add Another']
            self.optionsCombo = QComboBox(self)
            self.optionsCombo.setEditable(True)
            self.optionsCombo.addItems(tempList)
            self.optionsCombo.setEditable(False)
            self.optionsCombo.setFixedWidth(170)
            self.optionsCombo.setStyleSheet(open("css/comboBoxes.css").read())
            #self.optionsCombo.activated.connect(self.optionsComboEvent)
            self.lowerHBox.addWidget(self.optionsCombo)

        self.spacerLabel = QLabel('', self)
        self.spacerLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.lowerHBox.addWidget(self.spacerLabel)

        self.backButton = QPushButton('\u21A9', self) 
        self.backButton.setFixedSize(50,50)
        self.backButton.setStyleSheet(open('css/returnButtons.css').read())
        self.backButton.clicked.connect(self.listOrSearchScreenEvent)
        self.lowerHBox.addWidget(self.backButton)

        self.verticalBox.addLayout(self.middleHBox)
        self.middleHBox.addLayout(self.middleLeftVBox)
        self.middleHBox.addSpacing(0)
        self.middleHBox.addLayout(self.middleRightVBox)
        self.verticalBox.addLayout(self.lowerHBox)
        self.setLayout(self.verticalBox)

    # navigation events
    def listOrSearchScreenEvent(self): # back button has two potential pages 
        self.windowClass.listScreen() 

    def listScreenEvent(self):
        self.windowClass.listScreen() 

    def addCardEvent(self):
        () # need controller 

    # radioButton event
    def radioButtonEvent(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print(radioButton.condition)

    # checkBox event
    def checkState(self,b):
        if b.isChecked() == True:
            print(b.text()+" is selected")
        else:
            print (b.text()+" is deselected")
    