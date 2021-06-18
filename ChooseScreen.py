#!/usr/bin/python3

from PyQt5.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QPushButton

class ChooseScreen(QFrame):

    def __init__(self, parent): # constructor
        super().__init__(parent)
        self.windowClass = parent # allows calling of parent class methods
        self.setStyleSheet('background-color: rgb(230, 150, 199)')
        self.initScreen()

    def initScreen(self):
        panelLayout = QVBoxLayout()
        
        panelOne = QFrame()

        layout = QHBoxLayout()
        
        button = QPushButton('I change to Launch Screen')
        button.clicked.connect(self.buttonEvent)
        layout.addWidget(button)
        button2 = QPushButton('I am pointless!')
        layout.addWidget(button2)
        button3 = QPushButton('I am pointless!')
        layout.addWidget(button3)

        panelOne.setLayout(layout)
        

        panelTwo = QFrame()

        layout2 = QHBoxLayout()
        
        button4 = QPushButton('I am pointless!')
        layout2.addWidget(button4)
        button5 = QPushButton('I am pointless!')
        layout2.addWidget(button5)
        button6 = QPushButton('I am pointless!')
        layout2.addWidget(button6)

        panelTwo.setLayout(layout2)

        panelLayout.addWidget(panelOne)
        panelLayout.addWidget(panelTwo)

        self.setLayout(panelLayout)


    def buttonEvent(self):
        self.windowClass.launchScreen()