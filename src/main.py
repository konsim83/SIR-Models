__version__ = "v1.0"
__license__ = "MIT"
 
 
import sys
 
import numpy as np
import scipy as sp
from scipy.integrate import odeint
 
from PyQt5 import QtCore, QtGui, QtWidgets

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from sir import *



class SIR_QCvWidget(object):
    
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
        
        self.graphWidget = pg.PlotWidget(QCvWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphWidget.sizePolicy().hasHeightForWidth())
        self.graphWidget.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphWidget)
                
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
        
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        
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
        self.spinBox_N.setMaximum(100000000)
        self.spinBox_N.setSingleStep(10000)
        self.spinBox_N.setProperty("value", 83000000)
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
        self.spinBox_mu.setDecimals(4)
        self.spinBox_mu.setMaximum(0.1)
        self.spinBox_mu.setSingleStep(0.0001)
        self.spinBox_mu.setProperty("value", 0.000)
        self.spinBox_mu.setObjectName("spinBox_mu")
        self.gridLayout.addWidget(self.spinBox_mu, 6, 2, 1, 1)
        
        self.spinBox_nu = QtWidgets.QDoubleSpinBox(self.groupBox_model_prm)
        self.spinBox_nu.setDecimals(4)
        self.spinBox_nu.setMaximum(0.1)
        self.spinBox_nu.setSingleStep(0.0001)
        self.spinBox_nu.setProperty("value", 0.000)
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
        
        self.spinBox_mu_d = QtWidgets.QDoubleSpinBox(self.groupBox_model_prm)
        self.spinBox_mu_d.setDecimals(3)
        self.spinBox_mu_d.setMinimum(0)
        self.spinBox_mu_d.setMaximum(1.0)
        self.spinBox_mu_d.setSingleStep(0.001)
        self.spinBox_mu_d.setProperty("value", 0.01)
        self.spinBox_mu_d.setObjectName("spinBox_mu_d")
        self.gridLayout.addWidget(self.spinBox_mu_d, 13, 2, 1, 1)
        
        self.spinBox_a = QtWidgets.QDoubleSpinBox(self.groupBox_model_prm)
        self.spinBox_a.setDecimals(2)
        self.spinBox_a.setMinimum(0.01)
        self.spinBox_a.setSingleStep(0.01)
        self.spinBox_a.setProperty("value", 1.0)
        self.spinBox_a.setObjectName("spinBox_a")
        self.gridLayout.addWidget(self.spinBox_a, 14, 2, 1, 1)
        
        self.label_a = QtWidgets.QLabel(self.groupBox_model_prm)
        self.label_a.setObjectName("label_a")
        self.gridLayout.addWidget(self.label_a, 14, 1, 1, 1)
        
        self.label_mu_d = QtWidgets.QLabel(self.groupBox_model_prm)
        self.label_mu_d.setObjectName("label_mu_d")
        self.gridLayout.addWidget(self.label_mu_d, 13, 1, 1, 1)
        
        self.label_i0 = QtWidgets.QLabel(self.groupBox_model_prm)
        self.label_i0.setObjectName("label_i0")
        self.gridLayout.addWidget(self.label_i0, 11, 1, 1, 1)
        
        self.label_r0 = QtWidgets.QLabel(self.groupBox_model_prm)
        self.label_r0.setObjectName("label_r0")
        self.gridLayout.addWidget(self.label_r0, 12, 1, 1, 1)
        
        self.horizontalLayout_2.addWidget(self.groupBox_model_prm)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
                   
        self.retranslateUi(QCvWidget)
        QtCore.QMetaObject.connectSlotsByName(QCvWidget)
        
        #
        # initial values
        #                
        self.i0 = self.spinBox_i0.value()
        self.e0 = 0.0
        self.r0 = self.spinBox_r0.value()
        self.s0 = self.spinBox_N.value() - self.i0 - self.r0
        self.d0 = 0.0
        
        self.y0 = [self.s0, self.i0, self.r0]
        self.tspan  = np.linspace(0, self.spinBox_tmax.value(), self.spinBox_tmax.value()*3)
        
        self.beta = self.spinBox_beta.value()
        self.gamma = self.spinBox_gamma.value()
        self.mu = self.spinBox_mu.value()
        self.nu = self.spinBox_nu.value()
        self.N = self.spinBox_N.value()
        self.mu_d = self.spinBox_mu_d.value()
        self.a = 1/self.spinBox_a.value()

        #
        # Callbacks
        #
        self.spinBox_beta.valueChanged.connect(self.callback_change_generic_parameter)
        self.spinBox_gamma.valueChanged.connect(self.callback_change_generic_parameter)
        self.spinBox_mu.valueChanged.connect(self.callback_change_generic_parameter)
        self.spinBox_nu.valueChanged.connect(self.callback_change_generic_parameter)
        self.spinBox_N.valueChanged.connect(self.callback_change_generic_parameter)
        self.spinBox_mu_d.valueChanged.connect(self.callback_change_generic_parameter)
        self.spinBox_a.valueChanged.connect(self.callback_change_generic_parameter)
        
        self.spinBox_tmax.valueChanged.connect(self.callback_change_tmax)
        self.spinBox_i0.valueChanged.connect(self.callback_change_s0)
        self.spinBox_r0.valueChanged.connect(self.callback_change_s0)
        
        self.comboBox.currentIndexChanged.connect(self.callback_change_model_id)
        
        #
        # Local variables
        #
        self.initial_run = True
        
        self.plot_s_ref = []
        self.plot_e_ref = []
        self.plot_i_ref = []
        self.plot_r_ref = []
        self.plot_d_ref = []
        self.plot_N_ref = []
        
        self.plot_legend = []

        self.solution = []
        
        self.N_of_t = []
        
        self.model_id = 0
        
        #
        # Start
        #
        self.callback_solve()
        self.plot()
    
    def retranslateUi(self, QCvWidget):
        _translate = QtCore.QCoreApplication.translate
        
        QCvWidget.setWindowTitle(_translate("QCvWidget", "SIR Models"))
        
        self.groupBox_solver.setTitle(_translate("QCvWidget", "model info"))        
        self.comboBox.setItemText(0, _translate("QCvWidget", "SIR model"))
        self.comboBox.setItemText(1, _translate("QCvWidget", "SIRD model"))
        self.comboBox.setItemText(2, _translate("QCvWidget", "SEIR model"))
        self.comboBox.setItemText(3, _translate("QCvWidget", "SEIRD model"))
        
        self.groupBox_model_prm.setTitle(_translate("QCvWidget", "model parameters"))
        self.label_mu.setText(_translate("QCvWidget", "natural mortality rate per day (mu)"))
        self.label_N.setText(_translate("QCvWidget", "population size"))
        self.label_beta.setText(_translate("QCvWidget", "infection rate (beta)"))
        self.label_gamma.setText(_translate("QCvWidget", "recovery rate (gamma)"))
        self.label_nu.setText(_translate("QCvWidget", "birth rate per person (nu)"))
        self.label_tmax.setText(_translate("QCvWidget", "time span (time unit)"))
        self.label_i0.setText(_translate("QCvWidget", "initial infections"))
        self.label_r0.setText(_translate("QCvWidget", "initial recoveries"))
        self.label_mu_d.setText(_translate("QCvWidget", "SIRD only: disease mortality rate per day (mu_d)"))
        self.label_a.setText(_translate("QCvWidget", "SEIR only: medium latency time (days)"))
        
    def callback_change_model_id(self, model_index):
        self.model_id = model_index
                
        if self.model_id == 0:
            self.y0 = [self.s0, self.i0, self.r0]
        elif self.model_id == 1:
            self.y0 = [self.s0, self.i0, self.r0, self.d0]
        elif self.model_id == 2:
            self.y0 = [self.s0, self.e0, self.i0, self.r0]
        elif self.model_id == 3:
            self.y0 = [self.s0, self.e0, self.i0, self.r0, self.d0]
        
        self.callback_solve()
        self.plot()
        
    def callback_change_generic_parameter(self, new_value):
        self.beta = self.spinBox_beta.value()
        self.gamma = self.spinBox_gamma.value()
        self.mu = self.spinBox_mu.value()
        self.nu = self.spinBox_nu.value()
        self.N = self.spinBox_N.value()
        self.mu_d = self.spinBox_mu_d.value()
        self.a = 1/self.spinBox_a.value()
        
        self.callback_solve()
        self.plot()
        
    
    def callback_change_tmax(self, new_value):
        self.tspan  = np.linspace(0, self.spinBox_tmax.value(), self.spinBox_tmax.value()*3)
        
        self.callback_solve()
        self.plot()
            
    
    def callback_change_s0(self, new_value):
        self.s0 = self.spinBox_N.value() - self.i0 - self.r0
        if self.model_id == 0:
            self.y0 = [self.s0, self.i0, self.r0]
        elif self.model_id == 1:
            self.y0 = [self.s0, self.i0, self.r0, self.d0]
        elif self.model_id == 2:
            self.y0 = [self.s0, self.e0, self.i0, self.r0]
        elif self.model_id == 3:
            self.y0 = [self.s0, self.e0, self.i0, self.r0, self.d0]
        
        self.callback_solve()
        self.plot()
        
    
    def callback_solve(self):
        if self.initial_run == False:
            self.plot_legend.scene().removeItem(self.plot_legend)
        else:            
            # After first solve we need to set this to false
            self.initial_run = False
        
        if self.model_id == 0:
            self.solution = odeint(SIR_function, 
                                   self.y0, 
                                   self.tspan, 
                                   args=(self.N, self.beta, self.gamma, self.mu, self.nu))
            self.N_of_t = np.sum(self.solution,1)
            print("SIR model solved...")
        elif self.model_id == 1:
            self.solution = odeint(SIRD_function, 
                                   self.y0, 
                                   self.tspan, 
                                   args=(self.N, self.beta, self.gamma, self.mu, self.nu, self.mu_d))
            self.N_of_t = np.sum(self.solution[:,:-1],1)
            print("SIRD model solved...")
        elif self.model_id == 2:
            self.solution = odeint(SEIR_function, 
                                   self.y0, 
                                   self.tspan, 
                                   args=(self.N, self.beta, self.gamma, self.mu, self.nu, self.a))
            self.N_of_t = np.sum(self.solution,1)
            print("SEIR model solved...")
        elif self.model_id == 3:
            self.solution = odeint(SEIRD_function, 
                                   self.y0, 
                                   self.tspan, 
                                   args=(self.N, self.beta, self.gamma, self.mu, self.nu, self.a, self.mu_d))
            self.N_of_t = np.sum(self.solution[:,:-1],1)
            print("SEIRD model solved...")
                
        
    def plot(self):            
        self.graphWidget.setBackground('w')
    
        self.graphWidget.setLabel("left", "number of people", color='red', size=30)
        self.graphWidget.setLabel("bottom", 'time (days)', color='red', size=30)
                
        self.graphWidget.showGrid(x=True, y=True)
        
        self.graphWidget.setXRange(0, self.spinBox_tmax.value()*1.05, padding=0)
        self.graphWidget.setYRange(0, np.max(self.N_of_t)*1.05, padding=0)
                    
        if self.model_id == 0:
            self.plot_s_ref.clear()
            self.plot_e_ref.clear()
            self.plot_i_ref.clear()
            self.plot_r_ref.clear()
            self.plot_d_ref.clear()
            self.plot_N_ref.clear()
                  
            self.graphWidget.addLegend(offset=(-10,10))
            self.plot_legend = self.graphWidget.getPlotItem().legend
            
            
            self.plot_s_ref = self.graphWidget.plot(self.tspan, 
                                  self.solution[:,0], 
                                  name="suspectible", 
                                  pen=pg.mkPen(color="b", width=3, style=QtCore.Qt.SolidLine))
            self.plot_i_ref = self.graphWidget.plot(self.tspan, 
                                  self.solution[:,1], 
                                  name="infected", 
                                  pen=pg.mkPen(color="r", width=3, style=QtCore.Qt.SolidLine))
            self.plot_r_ref = self.graphWidget.plot(self.tspan, 
                                  self.solution[:,2], 
                                  name="removed", 
                                  pen=pg.mkPen(color="g", width=3, style=QtCore.Qt.SolidLine))
            self.plot_N_ref = self.graphWidget.plot(self.tspan, 
                                  self.N_of_t, 
                                  name="population (all)", 
                                  pen=pg.mkPen(color="y", width=3, style=QtCore.Qt.SolidLine))
            
        elif self.model_id == 1:
            self.plot_s_ref.clear()
            self.plot_e_ref.clear()
            self.plot_i_ref.clear()
            self.plot_r_ref.clear()
            self.plot_d_ref.clear()
            self.plot_N_ref.clear()
            
            self.graphWidget.addLegend(offset=(-10,10))
            self.plot_legend = self.graphWidget.getPlotItem().legend
            
            self.plot_s_ref = self.graphWidget.plot(self.tspan, 
                                  self.solution[:,0], 
                                  name="suspectible", 
                                  pen=pg.mkPen(color="b", width=3, style=QtCore.Qt.SolidLine))
            self.plot_i_ref = self.graphWidget.plot(self.tspan, 
                                  self.solution[:,1], 
                                  name="infected", 
                                  pen=pg.mkPen(color="r", width=3, style=QtCore.Qt.SolidLine))
            self.plot_r_ref = self.graphWidget.plot(self.tspan, 
                                  self.solution[:,2], 
                                  name="recovered", 
                                  pen=pg.mkPen(color="g", width=3, style=QtCore.Qt.SolidLine))
            self.plot_d_ref = self.graphWidget.plot(self.tspan, 
                                  self.solution[:,3], 
                                  name="deaths", 
                                  pen=pg.mkPen(color="k", width=3, style=QtCore.Qt.SolidLine))
            self.plot_N_ref = self.graphWidget.plot(self.tspan, 
                                  self.N_of_t, 
                                  name="population (all)", 
                                  pen=pg.mkPen(color="y", width=3, style=QtCore.Qt.SolidLine))
        elif self.model_id == 2:
            self.plot_s_ref.clear()
            self.plot_e_ref.clear()
            self.plot_i_ref.clear()
            self.plot_r_ref.clear()
            self.plot_d_ref.clear()
            self.plot_N_ref.clear()

            self.graphWidget.addLegend(offset=(-10,10))
            self.plot_legend = self.graphWidget.getPlotItem().legend
            
            self.plot_s_ref = self.graphWidget.plot(self.tspan, 
                                  self.solution[:,0], 
                                  name="suspectible", 
                                  pen=pg.mkPen(color="b", width=3, style=QtCore.Qt.SolidLine))
            self.plot_e_ref = self.graphWidget.plot(self.tspan, 
                                  self.solution[:,1], 
                                  name="exposed (not infectious)", 
                                  pen=pg.mkPen(color="c", width=3, style=QtCore.Qt.SolidLine))
            self.plot_i_ref = self.graphWidget.plot(self.tspan, 
                                  self.solution[:,2], 
                                  name="infectious", 
                                  pen=pg.mkPen(color="r", width=3, style=QtCore.Qt.SolidLine))
            self.plot_r_ref = self.graphWidget.plot(self.tspan, 
                                  self.solution[:,3], 
                                  name="removed", 
                                  pen=pg.mkPen(color="g", width=3, style=QtCore.Qt.SolidLine))
            self.plot_N_ref = self.graphWidget.plot(self.tspan, 
                                  self.N_of_t, 
                                  name="population (all)", 
                                  pen=pg.mkPen(color="y", width=3, style=QtCore.Qt.SolidLine))
        elif self.model_id == 3:
            self.plot_s_ref.clear()
            self.plot_e_ref.clear()
            self.plot_i_ref.clear()
            self.plot_r_ref.clear()
            self.plot_d_ref.clear()
            self.plot_N_ref.clear()

            self.graphWidget.addLegend(offset=(-10,10))
            self.plot_legend = self.graphWidget.getPlotItem().legend
            
            self.plot_s_ref = self.graphWidget.plot(self.tspan, 
                                  self.solution[:,0], 
                                  name="suspectible", 
                                  pen=pg.mkPen(color="b", width=3, style=QtCore.Qt.SolidLine))
            self.plot_e_ref = self.graphWidget.plot(self.tspan, 
                                  self.solution[:,1], 
                                  name="exposed (not infectious)", 
                                  pen=pg.mkPen(color="c", width=3, style=QtCore.Qt.SolidLine))
            self.plot_i_ref = self.graphWidget.plot(self.tspan, 
                                  self.solution[:,2], 
                                  name="infectious", 
                                  pen=pg.mkPen(color="r", width=3, style=QtCore.Qt.SolidLine))
            self.plot_r_ref = self.graphWidget.plot(self.tspan, 
                                  self.solution[:,3], 
                                  name="removed", 
                                  pen=pg.mkPen(color="g", width=3, style=QtCore.Qt.SolidLine))
            self.plot_d_ref = self.graphWidget.plot(self.tspan, 
                                  self.solution[:,4], 
                                  name="deaths", 
                                  pen=pg.mkPen(color="k", width=3, style=QtCore.Qt.SolidLine))
            self.plot_N_ref = self.graphWidget.plot(self.tspan, 
                                  self.N_of_t, 
                                  name="population (all)", 
                                  pen=pg.mkPen(color="y", width=3, style=QtCore.Qt.SolidLine))
            

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    QCvWidget = QtWidgets.QWidget()
    
    sir_ui = SIR_QCvWidget()
    sir_ui.setupUi(QCvWidget)
    
    QCvWidget.show()
    sys.exit(app.exec_())

