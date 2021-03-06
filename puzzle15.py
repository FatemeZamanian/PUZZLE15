# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'puzzle15.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from functools import partial
from PySide2.QtWidgets import QMessageBox

import sys
import os
import random
class main(QWidget):
       global txt,empt_x,empt_y,hd,arbtn
       def __init__(self):
              super(main,self).__init__()
              loader = QUiLoader()
              self.ui = loader.load('puzzle15.ui', None)
              self.ui.show()


              
              global arbtn
              self.arbtn=[[self.ui.pushButton_1,self.ui.pushButton_2,self.ui.pushButton_3,self.ui.pushButton_4],
              [self.ui.pushButton_5,self.ui.pushButton_6,self.ui.pushButton_7,self.ui.pushButton_8],
              [self.ui.pushButton_9,self.ui.pushButton_10,self.ui.pushButton_11,self.ui.pushButton_12],
              [self.ui.pushButton_13,self.ui.pushButton_14,self.ui.pushButton_15,self.ui.pushButton_16]
              ]
              self.ui.pushButton.clicked.connect(self.method_start)
              self.ui.pushButton_1.clicked.connect(partial(self.method_btn,0,0,0,0))
              self.ui.pushButton_2.clicked.connect(partial(self.method_btn,0,1,0,60))
              self.ui.pushButton_3.clicked.connect(partial(self.method_btn,0,2,0,120))
              self.ui.pushButton_4.clicked.connect(partial(self.method_btn,0,3,0,180))
              self.ui.pushButton_5.clicked.connect(partial(self.method_btn,1,0,60,0))
              self.ui.pushButton_6.clicked.connect(partial(self.method_btn,1,1,60,60))
              self.ui.pushButton_7.clicked.connect(partial(self.method_btn,1,2,60,120))
              self.ui.pushButton_8.clicked.connect(partial(self.method_btn,1,3,60,180))
              self.ui.pushButton_9.clicked.connect(partial(self.method_btn,2,0,120,0))
              self.ui.pushButton_10.clicked.connect(partial(self.method_btn,2,1,120,60))
              self.ui.pushButton_11.clicked.connect(partial(self.method_btn,2,2,120,120))
              self.ui.pushButton_12.clicked.connect(partial(self.method_btn,2,3,120,180))
              self.ui.pushButton_13.clicked.connect(partial(self.method_btn,3,0,180,0))
              self.ui.pushButton_14.clicked.connect(partial(self.method_btn,3,1,180,60))
              self.ui.pushButton_15.clicked.connect(partial(self.method_btn,3,2,180,120))
              self.ui.pushButton_16.clicked.connect(partial(self.method_btn,3,3,180,180))
              self.method_start()

              

              
              

       def method_start(self):
              global txt,empt_x,empt_y,hd
              self.empt_x=180
              self.empt_y=180
              txt=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
              random.shuffle(txt)
              self.ui.pushButton_1.setText(txt[0])
              self.ui.pushButton_2.setText(txt[1])
              self.ui.pushButton_3.setText(txt[2])
              self.ui.pushButton_4.setText(txt[3])
              self.ui.pushButton_5.setText(txt[4])
              self.ui.pushButton_6.setText(txt[5])
              self.ui.pushButton_7.setText(txt[6])
              self.ui.pushButton_8.setText(txt[7])
              self.ui.pushButton_9.setText(txt[8])
              self.ui.pushButton_10.setText(txt[9])
              self.ui.pushButton_11.setText(txt[10])
              self.ui.pushButton_12.setText(txt[11])
              self.ui.pushButton_13.setText(txt[12])
              self.ui.pushButton_14.setText(txt[13])
              self.ui.pushButton_15.setText(txt[14])

              for i in range(4):
                     for j in range(4):
                            self.arbtn[i][j].show()
              self.ui.pushButton_16.hide()
              self.hd=self.ui.pushButton_16
              
       def method_win(self):
              if self.arbtn[0][0]=='1' and self.arbtn[0][1]=='2' and self.arbtn[0][2]=='3' and self.arbtn[0][3]=='4' and self.arbtn[1][0]=='5' and self.arbtn[1][1]=='6' and self.arbtn[1][2]=='7' and self.arbtn[1][3]=='8' and self.arbtn[2][0]=='9' and self.arbtn[2][1]=='10' and self.arbtn[2][2]=='11' and self.arbtn[2][3]=='12' and self.arbtn[3][0]=='13' and self.arbtn[3][1]=='14' and self.arbtn[3][2]=='15':
                     if self.arbtn[3][3].hide()==True:
                            self.ui.pushButton.disable()
                            QMessageBox.about(self,"","you win!!!")




       def method_btn(self,n,m,x,y):
              if x==self.empt_x+60 and y==self.empt_y:
                     self.empt_x=x
                     self.empt_y=y
                     text=self.arbtn[n][m].text()
                     self.hd.setText(text)
                     self.hd.show()
                     self.arbtn[n][m].hide()
                     self.hd=self.arbtn[n][m]
                     self.method_win()
                            
              elif  x==self.empt_x-60 and y==self.empt_y:
                     self.empt_x=x
                     self.empt_y=y
                     text=self.arbtn[n][m].text()
                     self.hd.setText(text)
                     self.hd.show()
                     self.arbtn[n][m].hide()
                     self.hd=self.arbtn[n][m]
                     self.method_win()
                            
              elif y==self.empt_y+60 and x==self.empt_x:
                     self.empt_x=x
                     self.empt_y=y
                     text=self.arbtn[n][m].text()
                     self.hd.setText(text)
                     self.hd.show()
                     self.arbtn[n][m].hide()
                     self.hd=self.arbtn[n][m]
                     self.method_win()
              elif y==self.empt_y-60 and x==self.empt_x:
                     self.empt_x=x
                     self.empt_y=y
                     text=self.arbtn[n][m].text()
                     self.hd.setText(text)
                     self.hd.show()
                     self.arbtn[n][m].hide()
                     self.hd=self.arbtn[n][m]
                     self.method_win()




if __name__ == "__main__":
       app = QApplication([])
       widget = main()
       sys.exit(app.exec_())
