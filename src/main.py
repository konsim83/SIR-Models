from scipy.stats._stats import scipy
__author__      = "Konrad Simon"
__copyright__   = "Copyright 2018, geopde.de"
__version__ = "v0.1"
__license__ = "GPL"
 
 
import sys
 
import numpy as np
import scipy as sp
 
from PyQt5 import QtCore, QtGui, QtWidgets


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
        
        self.gamma = QtWidgets.QSpinBox(self.groupBox)
        self.gamma.setObjectName("gamma")
        self.gridLayout.addWidget(self.gamma, 5, 2, 1, 1)
        
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 6, 1, 1, 1)
        
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 1, 1, 1)
        
        self.mu = QtWidgets.QSpinBox(self.groupBox)
        self.mu.setObjectName("mu")
        self.gridLayout.addWidget(self.mu, 6, 2, 1, 1)
        
        self.nu = QtWidgets.QSpinBox(self.groupBox)
        self.nu.setObjectName("nu")
        self.gridLayout.addWidget(self.nu, 7, 2, 1, 1)
        
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 8, 1, 1, 1)
        
        self.beta = QtWidgets.QSpinBox(self.groupBox)
        self.beta.setObjectName("beta")
        self.gridLayout.addWidget(self.beta, 8, 2, 1, 1)
        
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
        self.N.setObjectName("N")
        self.gridLayout.addWidget(self.N, 9, 2, 1, 1)
        self.tmax = QtWidgets.QSpinBox(self.groupBox)
        self.tmax.setObjectName("tmax")
        self.gridLayout.addWidget(self.tmax, 10, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(QCvWidget)
        QtCore.QMetaObject.connectSlotsByName(QCvWidget)

    def retranslateUi(self, QCvWidget):
        _translate = QtCore.QCoreApplication.translate
        QCvWidget.setWindowTitle(_translate("QCvWidget", "QCvWidget"))
        self.pushButtonPlay.setText(_translate("QCvWidget", "compute"))
        self.groupBox.setTitle(_translate("QCvWidget", "model parameters"))
        self.label_1.setText(_translate("QCvWidget", "martality per person (mu)"))
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
