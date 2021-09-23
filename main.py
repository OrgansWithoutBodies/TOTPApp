import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QIcon
import random 
import os
import subprocess

PINE_SCREEN_WID = 720
PINE_SCREEN_HEI = 1440

FAC = 0.5

BG_COLOR= "#222222"
BUTTON_BG_COLOR= "#333333"
FONT_COLOR_PRIMARY= "#cccccc"
MFACODES={"OKT":{"logo":"/logos/oktalogo.png"},
          "AWS":{"logo":"/logos/awslogo.png"},
          "BHR":{"logo":"/logos/bamboologo.png"}}
    
def getCodeForMFA(mfacode):
    command='oathtool --base32 --totp {0}'.format(mfacode)
    test=subprocess.Popen(command.split(),stdout=subprocess.PIPE)    
    out,error=test.communicate()
    if error is None:
        code=out.decode('utf-8').strip("'").split('\n')[0]
        return [*code]
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
        code=[random.randint(0,9) for cc in range(6)]
    def get_code_then_set(self,source,mfa):
        selected=source.currentText()
        code=getCodeForMFA(mfa[selected])
        self.set_code(code)    
        
class CodeDial():
    def __init__(self):
        self.widget=QPushButton('*')
        self.widget.setFixedHeight(200)
        self.widget.setFixedWidth(50)
        self.widget.setFont(QFont('Arial', 30))
        self.widget.setStyleSheet("border-radius: 10px;border: 2px solid {0}; background-color: {1}; color:{0};".format(FONT_COLOR_PRIMARY,BUTTON_BG_COLOR))
    def setText(self,code):
        self.widget.setText(code)
def get_code():
    pass
def run_get_code():
    pass

def run_app(window,mfa):
    
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
    chooseSourceBtn=QComboBox()
    ii=0
    for cc in mfa.keys():
        chooseSourceBtn.addItem(cc)
        if cc in MFACODES.keys():
            icn=QIcon(currentdir+MFACODES[cc]['logo'])        
            chooseSourceBtn.setItemIcon(ii,icn)
        ii=ii+1
    btnHei=60
    chooseSourceBtn.setStyleSheet("color: {0};".format(FONT_COLOR_PRIMARY))
    chooseSourceBtn.setFixedHeight(btnHei)
    chooseSourceBtn.setFixedWidth(int(0.25*FAC*PINE_SCREEN_WID))
    newCodeBtn=QPushButton("GET NEW CODE")
    newCodeBtn.setFont(QFont('Arial', 19,QFont.Bold))
    newCodeBtn.setStyleSheet("border-radius: 7px;border: 2px solid {0}; background-color: {1}; color:{0};".format(FONT_COLOR_PRIMARY,BUTTON_BG_COLOR))
    newCodeBtn.setFixedHeight(btnHei)
    newCodeBtn.clicked.connect(lambda: CODE.get_code_then_set(chooseSourceBtn,mfa))
    buttonLayout=QHBoxLayout()
    buttonLayout.addWidget(chooseSourceBtn)
    buttonLayout.addWidget(newCodeBtn)
    parentLayout.addLayout(buttonLayout)
    window.setLayout(parentLayout)
    window.show()

def STARTAPP(mfa):  
    app = QApplication(sys.argv)
    window = QWidget()
    window.setStyleSheet("background-color:{0};".format(BG_COLOR))
    #window.setGeometry()
    window.setFixedHeight(FAC*PINE_SCREEN_HEI)
    window.setFixedWidth(FAC*PINE_SCREEN_WID)
    run_app(window,mfa)
    app.exec_()


if __name__ == "__main__":
    mfarc=sys.argv[1]
    print(mfarc)
    mfa=dict()
    with open(mfarc,'r') as file:
        for ll in file:
            vals=ll.split(" ")[1].strip('\n').strip('"').split('=')
            mfa[vals[0].split('MFA')[0]]=vals[1]
            
    
    STARTAPP(mfa)
#    for line in mfarc:
#        print(line)
#        if line in known:
#            assign icon
# TODO add mfarc file as args