from scipy.stats._stats import scipy
__author__      = "Konrad Simon"
__copyright__   = "Copyright 2018, geopde.de"
__version__ = "v0.1"
__license__ = "GPL"
 
 
import sys
 
import numpy as np
import scipy as sp

 
from PyQt5 import QtCore 
from PyQt5 import QtGui 
from PyQt5.QtWidgets import (QAction, 
                                QMenu,
                                QFrame,
                                QApplication, 
                                QWidget,
                                QGridLayout,
                                QMenuBar,
                                QPushButton)
 
 
# -------------------------------------------------
# begin class MainWindow(QWidget)        
# -------------------------------------------------    
class MainWindow(QWidget):
 
    def __init__(self):
        QWidget.__init__(self)
         
        # Set up an empty layout
        self.layout = QGridLayout()
        self.initLayout()
         
        # Add a menu bar to the layout
        self.menubar = QMenuBar()
        self.initMenuBar()
         
        # Add a camera frame to the layout
        self.cameraframe =  QFrame()
        self.initCameraFrame()
         
        # Add a control frame to the layout
        self.controlframe =  QFrame()
        self.initControlFrame()
         
        self.initGeometry()
        # end __init__(self)
             
 
    def initLayout(self):        
        self.setLayout(self.layout)
 
 
    def initMenuBar(self):
        self.layout.addWidget(self.menubar, 0, 0)
         
        # Menu bar        
        fileMenu = self.menubar.addMenu('File')
        helpMenu = self.menubar.addMenu('Help')
         
        # -------------
        # File->New
        newAct = QAction('New', fileMenu)
         
        # File->Import menu
        impMenu = QMenu('Import', fileMenu)
        # File->Import menu -> ...
        impAct01 = QAction('something', fileMenu) 
        impAct02 = QAction('something else' , fileMenu)
        # Add everything to File->Import 
        impMenu.addAction(impAct01)
        impMenu.addAction(impAct02)
         
        # File->Quit
        quitAct = QAction('Quit', fileMenu)
         
        # Add everything to File
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(quitAct)
        # -------------
         
        # -------------
        # Help->About
        newAct = QAction('About', self.menubar)
         
        # Add everything to Help
        helpMenu.addAction(newAct)
        # -------------
        # end initMenuBar(self)
 
    def initCameraFrame(self):
        self.layout.addWidget(self.cameraframe, 0, 0, 8,8)
         
        self.cameraframe.setObjectName('Camera Frame')
         
        shadow = QFrame.Plain
        self.cameraframe.setFrameShadow(shadow)
         
        shape = QFrame.Box
        self.cameraframe.setFrameShape(shape)
        self.cameraframe.setLineWidth(2.0)
         
        #         self.cameraframe.show()
        # end initFrameCamera(self)
 
    def initControlFrame(self):
        self.layout.addWidget(self.controlframe, 0, 9, 8,4)
        self.controlframe.setObjectName('Control Frame')
                         
        shadow = QFrame.Plain
        self.controlframe.setFrameShadow(shadow)
         
        shape = QFrame.Box
        self.controlframe.setFrameShape(shape)
        self.controlframe.setLineWidth(2.0)
        # end controlFrame(self) 
 
    def initGeometry(self):
        self.setGeometry(300, 100, 1200, 800)
        self.setWindowTitle('Drone Controls')    
        self.show()
        # end initGeometry(self)
# -------------------------------------------------
# end class MainWindow(QWidget)        
# -------------------------------------------------
 
 
# -------------------------------------------------------
# -------------------------------------------------------       
app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec_())
