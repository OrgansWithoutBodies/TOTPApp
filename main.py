import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QIcon
import random 
import os

PINE_SCREEN_WID = 720
PINE_SCREEN_HEI = 1440

FAC = 0.5

BG_COLOR= "#222222"
BUTTON_BG_COLOR= "#333333"
FONT_COLOR_PRIMARY= "#cccccc"

class Code():
    def __init__(self,buttons):
        self.set_buttons(buttons)
    def set_buttons(self,buttons):
        self.buttons=buttons
        
    def set_code(self,code):
        for bb in range(len(self.buttons)):
            self.buttons[bb].setText(str(code[bb]))
            
        #Todo something to acknowledge
    def set_random_code(self,source):
        btns=self.buttons

        code=[random.randint(0,9) for cc in range(6)]
        self.set_code(code)    
        sourceIndex=source.currentIndex()
        
class CodeDial():
    def __init__(self):
        self.widget=QPushButton('*')
        self.widget.setFixedHeight(200)
        self.widget.setFixedWidth(50)
        self.widget.setFont(QFont('Arial', 20))
        self.widget.setStyleSheet("border-radius: 10px;border: 2px solid {0}; background-color: {1}; color:{0};".format(FONT_COLOR_PRIMARY,BUTTON_BG_COLOR))
    def setText(self,code):
        self.widget.setText(code)
def get_code():
    pass
def run_get_code():
    pass

def run_app(window):
    
    pinLayout=QHBoxLayout()
    pinButtons=[]
    for pp in range(6):
        btn=CodeDial()
        pinButtons.append(btn)
        pinLayout.addWidget(btn.widget)
    CODE=Code(pinButtons)
    
    parentLayout=QVBoxLayout() 
    parentLayout.addLayout(pinLayout)
#    mfarcBtn=QPushButton("SET MFARC")
    currentdir=os.getcwd()
    codes={"OKTA":{"logo":"/logos/oktalogo.png"},
           "AWS":{"logo":"/logos/awslogo.png"},
           "BAMBOO":{"logo":"/logos/bamboologo.png"}}
    chooseSourceBtn=QComboBox()
    ii=0
    for cc in codes.keys():
        
        icn=QIcon(currentdir+codes[cc]['logo'])
        
        chooseSourceBtn.addItem(cc)
        chooseSourceBtn.setItemIcon(ii,icn)
        ii=ii+1
    chooseSourceBtn.setStyleSheet("color: {0};".format(FONT_COLOR_PRIMARY))
    newCodeBtn=QPushButton("GET NEW CODE")
    newCodeBtn.setStyleSheet("border-radius: 7px;border: 2px solid {0}; background-color: {1}; color:{0};".format(FONT_COLOR_PRIMARY,BUTTON_BG_COLOR))
    newCodeBtn.setFixedHeight(40)
    newCodeBtn.clicked.connect(lambda: CODE.set_random_code(chooseSourceBtn))
    buttonLayout=QVBoxLayout()
    buttonLayout.addWidget(chooseSourceBtn)
    buttonLayout.addWidget(newCodeBtn)
    parentLayout.addLayout(buttonLayout)
    window.setLayout(parentLayout)
    window.show()


app = QApplication(sys.argv)
window = QWidget()
window.setStyleSheet("background-color:{0};".format(BG_COLOR))
#window.setGeometry()
window.setFixedHeight(FAC*PINE_SCREEN_HEI)
window.setFixedWidth(FAC*PINE_SCREEN_WID)
run_app(window)
app.exec_()
