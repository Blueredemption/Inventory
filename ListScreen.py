from PyQt5 import QtWidgets
from FlowLayout import FlowLayout
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QComboBox, QFrame, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QScrollArea, QVBoxLayout, QPushButton, QWidget

class ListScreen(QFrame):

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

        self.upperInHBox = QHBoxLayout()
        self.upperInHBox.setAlignment(QtCore.Qt.AlignLeft)

        self.editNameButton = QPushButton('\U0001F589',self)
        self.editNameButton.setFixedSize(45,45)
        self.editNameButton.setStyleSheet(open('css/pencilButtons.css').read())
        self.editNameButton.clicked.connect(self.editNameEvent)
        self.upperInHBox.addWidget(self.editNameButton)

        self.headerLabel = QLabel('Container Name', self)
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

        # scroll area for when the user wants to see cards as cards (is hidden when the other is active)
        self.scrollBoxes = QScrollArea() 
        self.boxWidget = QWidget() # Widget that contains the flowLayout            

        self.middleFlowLayout = FlowLayout() # The FlowLayout that contains all of the Collection buttons
        self.middleFlowLayout.setSpacing(15)

        tempCollections = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        for buttonName in tempCollections:
            self.button = QPushButton(str(buttonName), self)
            self.button.setFixedSize(229,320)
            self.button.setStyleSheet(open('css/collectionButtons.css').read())
            self.button.clicked.connect(self.detailScreenEvent)
            self.button.installEventFilter(self)
            self.middleFlowLayout.addWidget(self.button)

        self.newButton = QPushButton('+', self)
        self.newButton.setFixedSize(229,320)
        self.newButton.setStyleSheet(open('css/plusButtons.css').read())
        self.newButton.clicked.connect(self.searchScreenEvent)
        self.middleFlowLayout.addWidget(self.newButton)

        self.boxWidget.setContentsMargins(0, 18, 0, 18)
        self.boxWidget.setLayout(self.middleFlowLayout)

        #ScrollArea Properties
        self.scrollBoxes.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollBoxes.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollBoxes.setStyleSheet(open("css/scrollArea.css").read())
        self.scrollBoxes.setWidgetResizable(True)
        self.scrollBoxes.setWidget(self.boxWidget)

        # scroll area for when the user wants to see cards as a list (is hidden when the other is active)
        self.scrollLists = QScrollArea() 
        self.listWidget = QWidget() # Widget that contains the flowLayout
        
        self.leftMiddleVerticalBox = QVBoxLayout()
        self.leftMiddleVerticalBox.setAlignment(QtCore.Qt.AlignTop)

        for i in range(1, 21):
            self.listHBox = QHBoxLayout()
            
            self.button = QPushButton(str(i), self)
            self.button.setFixedSize(75,104)
            self.button.setStyleSheet(open('css/smallButtons.css').read())
            self.button.clicked.connect(self.detailScreenEvent)
            self.button.installEventFilter(self)
            self.listHBox.addWidget(self.button)

            for j in range(1, 4):
                self.listLabel = QLabel(str(i) +' '  +str(j) +' Information\n' +str(i) +' '  +str(j) +' Information\n' +str(i) +' '  +str(j) +' Information', self)
                self.listLabel.setStyleSheet(open("css/smallLabels.css").read())
                self.listLabel.installEventFilter(self)

                self.listHBox.addWidget(self.listLabel)

            self.leftMiddleVerticalBox.addLayout(self.listHBox)

        self.listHBox = QHBoxLayout()
        self.newListButton = QPushButton('+', self)
        self.newListButton.setFixedSize(75,104)
        self.newListButton.setStyleSheet(open('css/smallPlusButtons.css').read())
        self.newListButton.clicked.connect(self.searchScreenEvent)
        self.listHBox.addWidget(self.newListButton)

        # this seemingly pointless 3 labels keeps the HBoxes symetrical, allowing for them to grow as the window grows. its odd, remove this and everything sticks to the far left.
        for i in range(1, 4):
            self.listLabel = QLabel('', self)
            self.listLabel.setStyleSheet(open("css/smallLabels.css").read())
            self.listHBox.addWidget(self.listLabel)
            
        self.leftMiddleVerticalBox.addLayout(self.listHBox)

        self.listWidget.setContentsMargins(0, 9, 0, 9)
        self.listWidget.setLayout(self.leftMiddleVerticalBox)

        #ScrollArea Properties
        self.scrollLists.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollLists.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollLists.setStyleSheet(open("css/scrollArea.css").read())
        self.scrollLists.setWidgetResizable(True)
        self.scrollLists.setWidget(self.listWidget)
        self.scrollLists.setVisible(False)
        
        ####

        self.lowerHBox = QHBoxLayout()
        self.lowerHBox.setAlignment(QtCore.Qt.AlignRight)    

        self.viewCardButton = QPushButton('\U00002610', self) 
        self.viewCardButton.setFixedSize(30,30)
        self.viewCardButton.setStyleSheet(open('css/viewButtons.css').read())
        self.viewCardButton.clicked.connect(self.changeViewEvent)
        self.viewCardButton.setEnabled(False)
        self.lowerHBox.addWidget(self.viewCardButton)

        self.viewListButton = QPushButton('\U0001D119', self) 
        self.viewListButton.setFixedSize(30,30)
        self.viewListButton.setStyleSheet(open('css/viewButtons.css').read())
        self.viewListButton.clicked.connect(self.changeViewEvent)
        self.lowerHBox.addWidget(self.viewListButton)

        self.lowerHBox.addSpacing(17)

        self.comboLabel = QLabel('Sort By:', self)
        self.comboLabel.setStyleSheet(open("css/smallLabels.css").read())
        self.comboLabel.setFixedHeight(45)
        self.lowerHBox.addWidget(self.comboLabel)
        
        tempSortList = ['Card Type', 'Card Value', 'Card Set', 'Card Color', 'CMC', 'Alphabetical']
        self.sortCombo = QComboBox(self)
        self.sortCombo.setEditable(True)
        self.sortCombo.addItems(tempSortList)
        self.sortCombo.setEditable(False)
        self.sortCombo.setFixedWidth(170)
        self.sortCombo.setStyleSheet(open("css/comboBoxes.css").read())
        #self.sortCombo.activated.connect(self.sortComboEvent)
        self.lowerHBox.addWidget(self.sortCombo)

        self.lowerHBox.addSpacing(20)

        self.searchLabel = QLabel('Search:', self)
        self.searchLabel.setStyleSheet(open("css/smallLabels.css").read())
        self.searchLabel.setFixedSize(80,45)
        self.lowerHBox.addWidget(self.searchLabel)

        self.searchBox = QLineEdit(self)
        self.searchBox.setFixedSize(253,35)
        self.searchBox.returnPressed.connect(self.searchEvent)
        self.searchBox.setStyleSheet(open("css/searchBoxes.css").read())
        self.lowerHBox.addWidget(self.searchBox)

        self.lowerHBox.addSpacing(999999) # large number to ensure max distanceS
        
        self.backButton = QPushButton('\u21A9', self) 
        self.backButton.setFixedSize(50,50)
        self.backButton.setStyleSheet(open('css/returnButtons.css').read())
        self.backButton.clicked.connect(self.containerScreenEvent)
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

        self.verticalBox.addLayout(self.upperHBox) 
        self.verticalBox.addLayout(self.middleHBox)
        self.middleHBox.addWidget(self.scrollBoxes)
        self.middleHBox.addWidget(self.scrollLists)
        self.middleHBox.addLayout(self.rightMiddleVerticalBox)
        self.verticalBox.addSpacing(10) 
        self.verticalBox.addLayout(self.lowerHBox)
        self.setLayout(self.verticalBox)

    # navigation events
    def containerScreenEvent(self):
        self.windowClass.containerScreen()

    def detailScreenEvent(self):
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        
        if modifiers == QtCore.Qt.ShiftModifier:
            # I need some way to store the button that is clicked
            deleteMsg = QMessageBox()
            deleteMsg.setWindowTitle(' ')
            deleteMsg.setText('Do you want to delete this card?')
            deleteMsg.setInformativeText('This action cannot be undone.')
            #deleteMsg.setWindowIcon(QtGui.QIcon('images/Zoe_Icon_48x48.png')) # this icon will eventually be whatever the program icon will be
            deleteMsg.setIconPixmap(QtGui.QPixmap("images/Zoe_Icon_48x48.png"))
            deleteMsg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            deleteMsg.setDefaultButton(QMessageBox.No)
            deleteMsg.buttonClicked.connect(self.deleteEvent)
            deleteMsg.exec_()
        else:
            ()#self.windowClass.detailScreen()

    def searchScreenEvent(self):
        self.windowClass.searchScreen()

    # delete event
    def deleteEvent(self, response):
        print(response.text())

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

    # search event
    def searchEvent(self):
        print('Search Event yet to be created')