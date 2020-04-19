from scipy.stats._stats import scipy
__author__      = "Konrad Simon"
__copyright__   = "Copyright 2018, geopde.de"
__version__ = "v0.1"
__license__ = "GPL"
 
 
import sys
 
import numpy as np
import scipy as sp
from scipy.integrate import odeint
 
from PyQt5 import QtCore, QtGui, QtWidgets


from PyQt5 import QtCore, QtGui, QtWidgets

#########################
def SIR(y0,t,N,c,w):
    # -- zunächst die Anfangsdaten - S, I, R:
    S = y0[0]
    I = y0[1]
    R = y0[2]
    # -- jetzt die Modellgleichungen
    r1 = -c*(S/N)*I
    r2 = c*(S/N)*I -w*I
    r3 = w*I
    # Rückgabe der berechneten rechten Seite
    return [r1, r2, r3]
#########################

class Ui_QCvWidget(object):
    def setupUi(self, QCvWidget): 
        QCvWidget.setObjectName("QCvWidget")
        QCvWidget.resize(905, 734)
        
        self.gridLayout_2 = QtWidgets.QGridLayout(QCvWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.graph = QtWidgets.QLabel(QCvWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph.sizePolicy().hasHeightForWidth())
        self.graph.setSizePolicy(sizePolicy)
        self.graph.setStyleSheet("border: 1px solid;")
        self.graph.setText("")
        self.graph.setObjectName("graph")
        self.verticalLayout.addWidget(self.graph)
        
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.pushButtonPlay = QtWidgets.QPushButton(QCvWidget)
        self.pushButtonPlay.setObjectName("pushButtonPlay")
        self.horizontalLayout_2.addWidget(self.pushButtonPlay)
        
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        
        self.groupBox = QtWidgets.QGroupBox(QCvWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 6, 1, 1, 1)
        
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 1, 1, 1)
        
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 8, 1, 1, 1)
        
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1)
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout.addLayout(self.verticalLayout_3, 3, 2, 1, 1)
        
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 1, 1, 1)
        
        self.N = QtWidgets.QSpinBox(self.groupBox)
        self.N.setMaximum(1000000)
        self.N.setSingleStep(1000)
        self.N.setProperty("value", 100000)
        self.N.setObjectName("N")
        self.gridLayout.addWidget(self.N, 9, 2, 1, 1)
        
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 1, 1, 1)
        
        self.gamma = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.gamma.setDecimals(3)
        self.gamma.setSingleStep(0.01)
        self.gamma.setProperty("value", 0.083)
        self.gamma.setObjectName("gamma")
        self.gridLayout.addWidget(self.gamma, 5, 2, 1, 1)
        
        self.mu = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.mu.setSingleStep(0.1)
        self.mu.setObjectName("mu")
        self.gridLayout.addWidget(self.mu, 6, 2, 1, 1)
        
        self.nu = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.nu.setSingleStep(0.1)
        self.nu.setObjectName("nu")
        self.gridLayout.addWidget(self.nu, 7, 2, 1, 1)
        
        self.beta = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.beta.setSingleStep(0.01)
        self.beta.setProperty("value", 0.45)
        self.beta.setObjectName("beta")
        self.gridLayout.addWidget(self.beta, 8, 2, 1, 1)
        
        self.tmax = QtWidgets.QSpinBox(self.groupBox)
        self.tmax.setMinimum(5)
        self.tmax.setMaximum(5000)
        self.tmax.setSingleStep(5)
        self.tmax.setProperty("value", 365)
        self.tmax.setObjectName("tmax")
        self.gridLayout.addWidget(self.tmax, 10, 2, 1, 1)
        
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(QCvWidget)
        QtCore.QMetaObject.connectSlotsByName(QCvWidget)
        
        I0 = 5.83  # Infizierte Fälle zum Anfangszeitpunkt
        R0 = 0.    # Anzahl Genesener zum Anfangszeitpunkt
        S0 = self.N.value() - I0 - R0 # Anzahl noch Gesunder zum Anfangszeitpunkt
        
        cc = self.beta.value()   # Infektionsrate
        ww = self.gamma.value()   # Genesungsrate
        
        # -- definiere die Daten für den Gleichungslöser
        y0 = [S0, I0, R0]
        t  = np.linspace(0, self.tmax.value(), self.tmax.value()*3) # rechne für 365 Tage mit 4 Schritten pro Tag
        
        

    def retranslateUi(self, QCvWidget):
        _translate = QtCore.QCoreApplication.translate
        QCvWidget.setWindowTitle(_translate("QCvWidget", "SIR Models"))
        self.pushButtonPlay.setText(_translate("QCvWidget", "compute"))
        self.groupBox.setTitle(_translate("QCvWidget", "model parameters"))
        self.label_1.setText(_translate("QCvWidget", "mortality per person (mu)"))
        self.label_5.setText(_translate("QCvWidget", "population size"))
        self.label_4.setText(_translate("QCvWidget", "infection rate per time unit (beta)"))
        self.label_2.setText(_translate("QCvWidget", "recovery rate per time unit (gamma)"))
        self.label_3.setText(_translate("QCvWidget", "birth rate per person (nu)"))
        self.label_6.setText(_translate("QCvWidget", "time span (time unit)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QCvWidget = QtWidgets.QWidget()
    ui = Ui_QCvWidget()
    ui.setupUi(QCvWidget)
    QCvWidget.show()
    sys.exit(app.exec_())

