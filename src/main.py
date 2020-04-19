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

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg


def SIR_function(y, t, N, beta, gamma, mu, nu):
        # -- zunächst die Anfangsdaten - S, I, R:
        S = y[0]
        I = y[1]
        R = y[2]
        # -- jetzt die Modellgleichungen
        r1 = nu*N - beta*(S/N)*I - mu*S
        r2 = beta*(S/N)*I -gamma*I - mu*I
        r3 = gamma*I - mu*R
        # Rückgabe der berechneten rechten Seite
        return [r1, r2, r3]


class Ui_QCvWidget(object):
    def setupUi(self, QCvWidget):
        QCvWidget.setObjectName("QCvWidget")
        QCvWidget.resize(905, 749)
        self.gridLayout_2 = QtWidgets.QGridLayout(QCvWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelGraph = QtWidgets.QLabel(QCvWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelGraph.sizePolicy().hasHeightForWidth())
        self.labelGraph.setSizePolicy(sizePolicy)
        self.labelGraph.setStyleSheet("border: 1px solid;")
        self.labelGraph.setText("")
        self.labelGraph.setObjectName("labelGraph")
        self.verticalLayout.addWidget(self.labelGraph)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_solver = QtWidgets.QGroupBox(QCvWidget)
        self.groupBox_solver.setObjectName("groupBox_solver")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_solver)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 110, 168, 103))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButtonSolve = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSolve.sizePolicy().hasHeightForWidth())
        self.pushButtonSolve.setSizePolicy(sizePolicy)
        self.pushButtonSolve.setObjectName("pushButtonSolve")
        self.verticalLayout_2.addWidget(self.pushButtonSolve)
        self.horizontalLayout_2.addWidget(self.groupBox_solver)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.groupBox_model_prm = QtWidgets.QGroupBox(QCvWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_model_prm.sizePolicy().hasHeightForWidth())
        self.groupBox_model_prm.setSizePolicy(sizePolicy)
        self.groupBox_model_prm.setObjectName("groupBox_model_prm")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_model_prm)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_mu = QtWidgets.QLabel(self.groupBox_model_prm)
        self.label_mu.setObjectName("label_mu")
        self.gridLayout.addWidget(self.label_mu, 6, 1, 1, 1)
        self.label_N = QtWidgets.QLabel(self.groupBox_model_prm)
        self.label_N.setObjectName("label_N")
        self.gridLayout.addWidget(self.label_N, 9, 1, 1, 1)
        self.label_beta = QtWidgets.QLabel(self.groupBox_model_prm)
        self.label_beta.setObjectName("label_beta")
        self.gridLayout.addWidget(self.label_beta, 8, 1, 1, 1)
        self.label_gamma = QtWidgets.QLabel(self.groupBox_model_prm)
        self.label_gamma.setObjectName("label_gamma")
        self.gridLayout.addWidget(self.label_gamma, 5, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout.addLayout(self.verticalLayout_3, 3, 2, 1, 1)
        self.label_nu = QtWidgets.QLabel(self.groupBox_model_prm)
        self.label_nu.setObjectName("label_nu")
        self.gridLayout.addWidget(self.label_nu, 7, 1, 1, 1)
        self.spinBox_N = QtWidgets.QSpinBox(self.groupBox_model_prm)
        self.spinBox_N.setMaximum(1000000)
        self.spinBox_N.setSingleStep(1000)
        self.spinBox_N.setProperty("value", 100000)
        self.spinBox_N.setObjectName("spinBox_N")
        self.gridLayout.addWidget(self.spinBox_N, 9, 2, 1, 1)
        self.label_tmax = QtWidgets.QLabel(self.groupBox_model_prm)
        self.label_tmax.setObjectName("label_tmax")
        self.gridLayout.addWidget(self.label_tmax, 10, 1, 1, 1)
        self.spinBox_gamma = QtWidgets.QDoubleSpinBox(self.groupBox_model_prm)
        self.spinBox_gamma.setDecimals(3)
        self.spinBox_gamma.setSingleStep(0.01)
        self.spinBox_gamma.setProperty("value", 0.083)
        self.spinBox_gamma.setObjectName("spinBox_gamma")
        self.gridLayout.addWidget(self.spinBox_gamma, 5, 2, 1, 1)
        self.spinBox_mu = QtWidgets.QDoubleSpinBox(self.groupBox_model_prm)
        self.spinBox_mu.setSingleStep(0.1)
        self.spinBox_mu.setObjectName("spinBox_mu")
        self.gridLayout.addWidget(self.spinBox_mu, 6, 2, 1, 1)
        self.spinBox_nu = QtWidgets.QDoubleSpinBox(self.groupBox_model_prm)
        self.spinBox_nu.setSingleStep(0.1)
        self.spinBox_nu.setObjectName("spinBox_nu")
        self.gridLayout.addWidget(self.spinBox_nu, 7, 2, 1, 1)
        self.spinBox_beta = QtWidgets.QDoubleSpinBox(self.groupBox_model_prm)
        self.spinBox_beta.setSingleStep(0.01)
        self.spinBox_beta.setProperty("value", 0.45)
        self.spinBox_beta.setObjectName("spinBox_beta")
        self.gridLayout.addWidget(self.spinBox_beta, 8, 2, 1, 1)
        self.spinBox_tmax = QtWidgets.QSpinBox(self.groupBox_model_prm)
        self.spinBox_tmax.setMinimum(5)
        self.spinBox_tmax.setMaximum(5000)
        self.spinBox_tmax.setSingleStep(5)
        self.spinBox_tmax.setProperty("value", 365)
        self.spinBox_tmax.setObjectName("spinBox_tmax")
        self.gridLayout.addWidget(self.spinBox_tmax, 10, 2, 1, 1)
        self.spinBox_i0 = QtWidgets.QDoubleSpinBox(self.groupBox_model_prm)
        self.spinBox_i0.setMaximum(9999.99)
        self.spinBox_i0.setProperty("value", 5.83)
        self.spinBox_i0.setObjectName("spinBox_i0")
        self.gridLayout.addWidget(self.spinBox_i0, 11, 2, 1, 1)
        self.spinBox_r0 = QtWidgets.QDoubleSpinBox(self.groupBox_model_prm)
        self.spinBox_r0.setMaximum(99999.99)
        self.spinBox_r0.setSingleStep(0.01)
        self.spinBox_r0.setObjectName("spinBox_r0")
        self.gridLayout.addWidget(self.spinBox_r0, 12, 2, 1, 1)
        self.label_i0 = QtWidgets.QLabel(self.groupBox_model_prm)
        self.label_i0.setObjectName("label_i0")
        self.gridLayout.addWidget(self.label_i0, 11, 1, 1, 1)
        self.label_r0 = QtWidgets.QLabel(self.groupBox_model_prm)
        self.label_r0.setObjectName("label_r0")
        self.gridLayout.addWidget(self.label_r0, 12, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_model_prm)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        
        def callback_change_value(new_value):
            print("new beta = ", self.spinBox_beta.value())
            print("new N = ", self.spinBox_N.value())
            
        self.spinBox_beta.valueChanged.connect(callback_change_value)
        self.spinBox_N.valueChanged.connect(callback_change_value)
           
        self.retranslateUi(QCvWidget)
        QtCore.QMetaObject.connectSlotsByName(QCvWidget)
        
        self.i0 = self.spinBox_i0.value()
        self.r0 = self.spinBox_r0.value()
        self.s0 = self.spinBox_N.value() - self.i0 - self.r0
        
        self.y0 = [self.s0, self.i0, self.r0]
        self.tspan  = np.linspace(0, self.spinBox_tmax.value(), self.spinBox_tmax.value()*3)
        
        self.beta = self.spinBox_beta.value()
        self.gamma = self.spinBox_gamma.value()
        self.mu = self.spinBox_mu.value()
        self.nu = self.spinBox_nu.value()
        self.N = self.spinBox_N.value()
                
        self.solution = []

        #
        # Callbacks
        #
        self.spinBox_beta.valueChanged.connect(self.callback_change_generic_parameter)
        self.spinBox_gamma.valueChanged.connect(self.callback_change_generic_parameter)
        self.spinBox_mu.valueChanged.connect(self.callback_change_generic_parameter)
        self.spinBox_nu.valueChanged.connect(self.callback_change_generic_parameter)
        self.spinBox_N.valueChanged.connect(self.callback_change_generic_parameter)
        
        self.spinBox_tmax.valueChanged.connect(self.callback_change_tmax)
        self.spinBox_i0.valueChanged.connect(self.callback_change_s0)
        self.spinBox_r0.valueChanged.connect(self.callback_change_s0)
        
        self.pushButtonSolve.clicked.connect(self.callback_solve)
        
    def retranslateUi(self, QCvWidget):
        _translate = QtCore.QCoreApplication.translate
        QCvWidget.setWindowTitle(_translate("QCvWidget", "QCvWidget"))
        self.groupBox_solver.setTitle(_translate("QCvWidget", "solver"))
        self.pushButtonSolve.setText(_translate("QCvWidget", "compute"))
        self.groupBox_model_prm.setTitle(_translate("QCvWidget", "model parameters"))
        self.label_mu.setText(_translate("QCvWidget", "mortality per person (mu)"))
        self.label_N.setText(_translate("QCvWidget", "population size"))
        self.label_beta.setText(_translate("QCvWidget", "infection rate per time unit (beta)"))
        self.label_gamma.setText(_translate("QCvWidget", "recovery rate per time unit (gamma)"))
        self.label_nu.setText(_translate("QCvWidget", "birth rate per person (nu)"))
        self.label_tmax.setText(_translate("QCvWidget", "time span (time unit)"))
        self.label_i0.setText(_translate("QCvWidget", "initial infections"))
        self.label_r0.setText(_translate("QCvWidget", "initial recoveries"))
        
    def callback_change_generic_parameter(self, new_value):
        self.beta = self.spinBox_beta.value()
        self.gamma = self.spinBox_gamma.value()
        self.mu = self.spinBox_mu.value()
        self.nu = self.spinBox_nu.value()
        self.N = self.spinBox_N.value()
        
    def callback_change_tmax(self, new_value):
        self.tspan  = np.linspace(0, self.spinBox_tmax.value(), self.spinBox_tmax.value()*3)
            
    def callback_change_s0(self, new_value):
        self.s0 = self.spinBox_N.value() - self.i0 - self.r0
        
    def callback_solve(self):
        self.solution = odeint(SIR_function, 
                               self.y0, 
                               self.tspan, 
                               args=(self.N, self.beta, self.gamma, self.mu, self.nu))
        print("Model solved.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QCvWidget = QtWidgets.QWidget()
    ui = Ui_QCvWidget()
    ui.setupUi(QCvWidget)
    QCvWidget.show()
    sys.exit(app.exec_())

