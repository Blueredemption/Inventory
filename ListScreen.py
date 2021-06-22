from FlowLayout import FlowLayout
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QComboBox, QFrame, QHBoxLayout, QLabel, QLineEdit, QScrollArea, QVBoxLayout, QPushButton, QWidget

class ListScreen(QFrame):

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

        upperInHBox = QHBoxLayout()
        upperInHBox.setAlignment(QtCore.Qt.AlignLeft)
        upperInHBox.setGeometry

        self.editNameButton = QPushButton('\U0001F589',self)
        self.editNameButton.setMinimumSize(45,45)
        self.editNameButton.setMaximumSize(45,45)
        self.editNameButton.setStyleSheet(open('css/pencilButtons.css').read())
        self.editNameButton.clicked.connect(self.editNameEvent)
        upperInHBox.addWidget(self.editNameButton)

        self.headerLabel = QLabel('Container Name', self)
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

        # scroll area for when the user wants to see cards as cards (is hidden when the other is active)
        self.scrollBoxes = QScrollArea() 
        boxWidget = QWidget() # Widget that contains the flowLayout            

        middleFlowLayout = FlowLayout() # The FlowLayout that contains all of the Collection buttons
        middleFlowLayout.setSpacing(15)

        tempCollections = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        for buttonName in tempCollections:
            button = QPushButton(str(buttonName), self)
            button.setMinimumSize(229,320)
            button.setMaximumSize(229,320)
            button.setStyleSheet(open('css/collectionButtons.css').read())
            #button.clicked.connect(self.detailScreenEvent)
            button.installEventFilter(self)
            middleFlowLayout.addWidget(button)

        newButton = QPushButton('+', self)
        newButton.setMinimumSize(229,320)
        newButton.setMaximumSize(229,320)
        newButton.setStyleSheet(open('css/plusButtons.css').read())
        #newButton.clicked.connect(self.searchScreenEvent)
        middleFlowLayout.addWidget(newButton)

        boxWidget.setContentsMargins(0, 18, 0, 18)
        boxWidget.setLayout(middleFlowLayout)

        #ScrollArea Properties
        self.scrollBoxes.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollBoxes.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollBoxes.setStyleSheet(open("css/scrollArea.css").read())
        self.scrollBoxes.setWidgetResizable(True)
        self.scrollBoxes.setWidget(boxWidget)

        # scroll area for when the user wants to see cards as a list (is hidden when the other is active)
        self.scrollLists = QScrollArea() 
        listWidget = QWidget() # Widget that contains the flowLayout
        
        leftMiddleVerticalBox = QVBoxLayout()
        leftMiddleVerticalBox.setAlignment(QtCore.Qt.AlignTop)

        for i in range(1, 21):
            listHBox = QHBoxLayout()
            
            button = QPushButton(str(i), self)
            button.setMinimumSize(57,80)
            button.setMaximumSize(57,80)
            button.setStyleSheet(open('css/smallButtons.css').read())
            #button.clicked.connect(self.detailScreenEvent)
            button.installEventFilter(self)
            listHBox.addWidget(button)

            for j in range(1, 4):
                listLabel = QLabel(str(i) +' '  +str(j) +' Information', self)
                listLabel.setStyleSheet(open("css/smallLabels.css").read())
                listLabel.installEventFilter(self)
                listLabel.setFixedHeight(50)
                listHBox.addWidget(listLabel)

            leftMiddleVerticalBox.addLayout(listHBox)

        listHBox = QHBoxLayout()
        newListButton = QPushButton('+', self)
        newListButton.setMinimumSize(57,80)
        newListButton.setMaximumSize(57,80)
        newListButton.setStyleSheet(open('css/smallPlusButtons.css').read())
        #newListButton.clicked.connect(self.searchScreenEvent)
        listHBox.addWidget(newListButton)

        # this seemingly pointless 3 labels keeps the HBoxes symetrical, allowing for them to grow as the window grows. its odd, remove this and everything sticks to the far left.
        for i in range(1, 4):
            listLabel = QLabel('', self)
            listLabel.setStyleSheet(open("css/smallLabels.css").read())
            listLabel.setFixedHeight(50)
            listHBox.addWidget(listLabel)
            
        leftMiddleVerticalBox.addLayout(listHBox)

        listWidget.setContentsMargins(0, 9, 0, 9)
        listWidget.setLayout(leftMiddleVerticalBox)

        #ScrollArea Properties
        self.scrollLists.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollLists.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollLists.setStyleSheet(open("css/scrollArea.css").read())
        self.scrollLists.setWidgetResizable(True)
        self.scrollLists.setWidget(listWidget)
        self.scrollLists.setVisible(False)
        
        ####

        lowerHBox = QHBoxLayout()
        lowerHBox.setAlignment(QtCore.Qt.AlignRight)    

        comboLabel = QLabel('Sort By: ', self)
        comboLabel.setStyleSheet(open("css/smallLabels.css").read())
        comboLabel.setFixedHeight(45)
        lowerHBox.addWidget(comboLabel)
        
        tempSortList = ['Card Type', 'Card Value', 'Card Set']
        sortCombo = QComboBox(self)
        sortCombo.setEditable(True)
        sortCombo.addItems(tempSortList)
        sortCombo.setEditable(False)
        sortCombo.setFixedWidth(170)
        sortCombo.setStyleSheet(open("css/comboBoxes.css").read())
        #sortCombo.activated.connect(self.sortComboEvent)
        lowerHBox.addWidget(sortCombo)

        lowerHBox.addSpacing(999999) # large number to ensure max distance

        self.viewCardButton = QPushButton('\U00002610', self) 
        self.viewCardButton.setMinimumSize(30,30)
        self.viewCardButton.setMaximumSize(30,30)
        self.viewCardButton.setStyleSheet(open('css/viewButtons.css').read())
        self.viewCardButton.clicked.connect(self.changeViewEvent)
        self.viewCardButton.setEnabled(False)
        lowerHBox.addWidget(self.viewCardButton)

        self.viewListButton = QPushButton('\U0001D119', self) 
        self.viewListButton.setMinimumSize(30,30)
        self.viewListButton.setMaximumSize(30,30)
        self.viewListButton.setStyleSheet(open('css/viewButtons.css').read())
        self.viewListButton.clicked.connect(self.changeViewEvent)
        lowerHBox.addWidget(self.viewListButton)

        lowerHBox.addSpacing(211)

        backButton = QPushButton('\u21A9', self) 
        backButton.setMinimumSize(50,50)
        backButton.setMaximumSize(50,50)
        backButton.setStyleSheet(open('css/returnButtons.css').read())
        backButton.clicked.connect(self.containerScreenEvent)
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
        middleHBox.addWidget(self.scrollBoxes)
        middleHBox.addWidget(self.scrollLists)
        middleHBox.addLayout(rightMiddleVerticalBox)
        verticalBox.addSpacing(10) 
        verticalBox.addLayout(lowerHBox)

        self.setLayout(verticalBox)

    # navigation events
    def containerScreenEvent(self):
        self.windowClass.containerScreen()

    # hover events
    def eventFilter(self, object, event): # this is going to be a switch statement into more specific methods if / once I have to filter more than one objects event
        if event.type() == 10: # event 10 is mouse entering the button
            self.sideLabel.setText("Card Name")
            self.sideLabel2.setText("Card Info")
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

    def changeViewEvent(self):
        Boolean = self.scrollLists.isVisible()
        self.scrollLists.setVisible(not Boolean)
        self.scrollBoxes.setVisible(Boolean)
        self.viewListButton.setEnabled(not Boolean)
        self.viewCardButton.setEnabled(Boolean)