import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import random 

PINE_SCREEN_WID = 720
PINE_SCREEN_HEI = 1440

FAC = 0.5

BG_COLOR= "#222222"
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
    def set_random_code(self):
        btns=self.buttons

        code=[random.randint(0,9) for cc in range(6)]
        self.set_code(code)    
class CodeDial():
    def __init__(self):
        self.widget=QPushButton('*')
        self.widget.setFixedHeight(200)
        self.widget.setFixedWidth(50)
        self.widget.setFont(QFont('Arial', 20))
        self.widget.setStyleSheet("border-radius: 10px;border: 2px solid {0}; background-color: {1}; color:{0};".format(FONT_COLOR_PRIMARY,BG_COLOR))
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
    mfarcBtn=QPushButton("SET MFARC")
    newCodeBtn=QPushButton("GET NEW CODE")
    newCodeBtn.clicked.connect(lambda: CODE.set_random_code())
    parentLayout.addWidget(newCodeBtn)
    window.setLayout(parentLayout)
    window.show()


app = QApplication(sys.argv)
window = QWidget()
#window.setGeometry()
window.setFixedHeight(FAC*PINE_SCREEN_HEI)
window.setFixedWidth(FAC*PINE_SCREEN_WID)
run_app(window)
app.exec_()
