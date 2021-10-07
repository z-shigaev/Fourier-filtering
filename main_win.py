# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1226, 884)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_1.sizePolicy().hasHeightForWidth())
        self.frame_1.setSizePolicy(sizePolicy)
        self.frame_1.setMinimumSize(QtCore.QSize(630, 250))
        self.frame_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.horizontalLayout_7.addWidget(self.frame_1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_x_1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_x_1.sizePolicy().hasHeightForWidth())
        self.label_x_1.setSizePolicy(sizePolicy)
        self.label_x_1.setMinimumSize(QtCore.QSize(60, 20))
        self.label_x_1.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_x_1.setFont(font)
        self.label_x_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_x_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_x_1.setObjectName("label_x_1")
        self.verticalLayout.addWidget(self.label_x_1)
        self.lineEdit_graph_1 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_graph_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_graph_1.setSizePolicy(sizePolicy)
        self.lineEdit_graph_1.setMinimumSize(QtCore.QSize(60, 20))
        self.lineEdit_graph_1.setMaximumSize(QtCore.QSize(60, 20))
        self.lineEdit_graph_1.setObjectName("lineEdit_graph_1")
        self.verticalLayout.addWidget(self.lineEdit_graph_1)
        self.verticalSlider_1 = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalSlider_1.sizePolicy().hasHeightForWidth())
        self.verticalSlider_1.setSizePolicy(sizePolicy)
        self.verticalSlider_1.setMinimumSize(QtCore.QSize(60, 0))
        self.verticalSlider_1.setMaximumSize(QtCore.QSize(60, 16777215))
        self.verticalSlider_1.setMinimum(1)
        self.verticalSlider_1.setMaximum(100)
        self.verticalSlider_1.setProperty("value", 100)
        self.verticalSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_1.setInvertedAppearance(False)
        self.verticalSlider_1.setInvertedControls(True)
        self.verticalSlider_1.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.verticalSlider_1.setObjectName("verticalSlider_1")
        self.verticalLayout.addWidget(self.verticalSlider_1)
        self.lineEdit_per_1 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_per_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_per_1.setSizePolicy(sizePolicy)
        self.lineEdit_per_1.setMinimumSize(QtCore.QSize(60, 20))
        self.lineEdit_per_1.setMaximumSize(QtCore.QSize(60, 20))
        self.lineEdit_per_1.setObjectName("lineEdit_per_1")
        self.verticalLayout.addWidget(self.lineEdit_per_1)
        self.btn_OK_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_OK_1.setMinimumSize(QtCore.QSize(60, 20))
        self.btn_OK_1.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn_OK_1.setFont(font)
        self.btn_OK_1.setObjectName("btn_OK_1")
        self.verticalLayout.addWidget(self.btn_OK_1)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(630, 250))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6.addWidget(self.frame_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_x_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_x_2.sizePolicy().hasHeightForWidth())
        self.label_x_2.setSizePolicy(sizePolicy)
        self.label_x_2.setMinimumSize(QtCore.QSize(60, 20))
        self.label_x_2.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_x_2.setFont(font)
        self.label_x_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_x_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_x_2.setObjectName("label_x_2")
        self.verticalLayout_3.addWidget(self.label_x_2)
        self.lineEdit_graph_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_graph_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_graph_2.setSizePolicy(sizePolicy)
        self.lineEdit_graph_2.setMinimumSize(QtCore.QSize(60, 20))
        self.lineEdit_graph_2.setMaximumSize(QtCore.QSize(60, 20))
        self.lineEdit_graph_2.setObjectName("lineEdit_graph_2")
        self.verticalLayout_3.addWidget(self.lineEdit_graph_2)
        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalSlider_2.sizePolicy().hasHeightForWidth())
        self.verticalSlider_2.setSizePolicy(sizePolicy)
        self.verticalSlider_2.setMinimumSize(QtCore.QSize(60, 0))
        self.verticalSlider_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.verticalSlider_2.setMinimum(1)
        self.verticalSlider_2.setMaximum(100)
        self.verticalSlider_2.setProperty("value", 100)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setInvertedAppearance(False)
        self.verticalSlider_2.setInvertedControls(True)
        self.verticalSlider_2.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalLayout_3.addWidget(self.verticalSlider_2)
        self.lineEdit_per_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_per_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_per_2.setSizePolicy(sizePolicy)
        self.lineEdit_per_2.setMinimumSize(QtCore.QSize(60, 20))
        self.lineEdit_per_2.setMaximumSize(QtCore.QSize(60, 20))
        self.lineEdit_per_2.setObjectName("lineEdit_per_2")
        self.verticalLayout_3.addWidget(self.lineEdit_per_2)
        self.btn_OK_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_OK_2.setMinimumSize(QtCore.QSize(60, 20))
        self.btn_OK_2.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn_OK_2.setFont(font)
        self.btn_OK_2.setObjectName("btn_OK_2")
        self.verticalLayout_3.addWidget(self.btn_OK_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(630, 250))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5.addWidget(self.frame_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_x_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_x_3.sizePolicy().hasHeightForWidth())
        self.label_x_3.setSizePolicy(sizePolicy)
        self.label_x_3.setMinimumSize(QtCore.QSize(60, 20))
        self.label_x_3.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_x_3.setFont(font)
        self.label_x_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_x_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_x_3.setObjectName("label_x_3")
        self.verticalLayout_4.addWidget(self.label_x_3)
        self.lineEdit_graph_3 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_graph_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_graph_3.setSizePolicy(sizePolicy)
        self.lineEdit_graph_3.setMinimumSize(QtCore.QSize(60, 20))
        self.lineEdit_graph_3.setMaximumSize(QtCore.QSize(60, 20))
        self.lineEdit_graph_3.setObjectName("lineEdit_graph_3")
        self.verticalLayout_4.addWidget(self.lineEdit_graph_3)
        self.verticalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalSlider_3.sizePolicy().hasHeightForWidth())
        self.verticalSlider_3.setSizePolicy(sizePolicy)
        self.verticalSlider_3.setMinimumSize(QtCore.QSize(60, 0))
        self.verticalSlider_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.verticalSlider_3.setMinimum(1)
        self.verticalSlider_3.setMaximum(100)
        self.verticalSlider_3.setProperty("value", 100)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setInvertedAppearance(False)
        self.verticalSlider_3.setInvertedControls(True)
        self.verticalSlider_3.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.verticalLayout_4.addWidget(self.verticalSlider_3)
        self.lineEdit_per_3 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_per_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_per_3.setSizePolicy(sizePolicy)
        self.lineEdit_per_3.setMinimumSize(QtCore.QSize(60, 20))
        self.lineEdit_per_3.setMaximumSize(QtCore.QSize(60, 20))
        self.lineEdit_per_3.setObjectName("lineEdit_per_3")
        self.verticalLayout_4.addWidget(self.lineEdit_per_3)
        self.btn_OK_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_OK_3.setMinimumSize(QtCore.QSize(60, 20))
        self.btn_OK_3.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn_OK_3.setFont(font)
        self.btn_OK_3.setObjectName("btn_OK_3")
        self.verticalLayout_4.addWidget(self.btn_OK_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_time.sizePolicy().hasHeightForWidth())
        self.label_time.setSizePolicy(sizePolicy)
        self.label_time.setMinimumSize(QtCore.QSize(140, 0))
        self.label_time.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_time.setFont(font)
        self.label_time.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.gridLayout.addWidget(self.label_time, 1, 0, 1, 1)
        self.lineEdit_FD = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_FD.sizePolicy().hasHeightForWidth())
        self.lineEdit_FD.setSizePolicy(sizePolicy)
        self.lineEdit_FD.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_FD.setObjectName("lineEdit_FD")
        self.gridLayout.addWidget(self.lineEdit_FD, 1, 1, 1, 1)
        self.lineEdit_points = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_points.sizePolicy().hasHeightForWidth())
        self.lineEdit_points.setSizePolicy(sizePolicy)
        self.lineEdit_points.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_points.setObjectName("lineEdit_points")
        self.gridLayout.addWidget(self.lineEdit_points, 1, 2, 1, 1)
        self.label_config_1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_1.sizePolicy().hasHeightForWidth())
        self.label_config_1.setSizePolicy(sizePolicy)
        self.label_config_1.setMaximumSize(QtCore.QSize(1000, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_config_1.setFont(font)
        self.label_config_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_config_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_config_1.setWordWrap(False)
        self.label_config_1.setObjectName("label_config_1")
        self.gridLayout.addWidget(self.label_config_1, 0, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_slct_func = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_slct_func.sizePolicy().hasHeightForWidth())
        self.label_slct_func.setSizePolicy(sizePolicy)
        self.label_slct_func.setMaximumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_slct_func.setFont(font)
        self.label_slct_func.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_slct_func.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slct_func.setObjectName("label_slct_func")
        self.horizontalLayout_3.addWidget(self.label_slct_func)
        self.comboBox_func = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_func.sizePolicy().hasHeightForWidth())
        self.comboBox_func.setSizePolicy(sizePolicy)
        self.comboBox_func.setMinimumSize(QtCore.QSize(60, 60))
        self.comboBox_func.setMaximumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_func.setFont(font)
        self.comboBox_func.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_func.setIconSize(QtCore.QSize(16, 16))
        self.comboBox_func.setFrame(True)
        self.comboBox_func.setModelColumn(0)
        self.comboBox_func.setObjectName("comboBox_func")
        self.comboBox_func.addItem("")
        self.comboBox_func.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_func)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_coeff_A = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_coeff_A.sizePolicy().hasHeightForWidth())
        self.label_coeff_A.setSizePolicy(sizePolicy)
        self.label_coeff_A.setMaximumSize(QtCore.QSize(30, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_coeff_A.setFont(font)
        self.label_coeff_A.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_coeff_A.setObjectName("label_coeff_A")
        self.horizontalLayout_4.addWidget(self.label_coeff_A)
        self.lineEdit_coeff_A = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_coeff_A.sizePolicy().hasHeightForWidth())
        self.lineEdit_coeff_A.setSizePolicy(sizePolicy)
        self.lineEdit_coeff_A.setMinimumSize(QtCore.QSize(80, 40))
        self.lineEdit_coeff_A.setMaximumSize(QtCore.QSize(80, 40))
        self.lineEdit_coeff_A.setObjectName("lineEdit_coeff_A")
        self.horizontalLayout_4.addWidget(self.lineEdit_coeff_A)
        self.label_coeff_B = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_coeff_B.sizePolicy().hasHeightForWidth())
        self.label_coeff_B.setSizePolicy(sizePolicy)
        self.label_coeff_B.setMaximumSize(QtCore.QSize(30, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_coeff_B.setFont(font)
        self.label_coeff_B.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_coeff_B.setObjectName("label_coeff_B")
        self.horizontalLayout_4.addWidget(self.label_coeff_B)
        self.lineEdit_coeff_B = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_coeff_B.sizePolicy().hasHeightForWidth())
        self.lineEdit_coeff_B.setSizePolicy(sizePolicy)
        self.lineEdit_coeff_B.setMinimumSize(QtCore.QSize(80, 40))
        self.lineEdit_coeff_B.setMaximumSize(QtCore.QSize(80, 40))
        self.lineEdit_coeff_B.setObjectName("lineEdit_coeff_B")
        self.horizontalLayout_4.addWidget(self.lineEdit_coeff_B)
        self.btn_Add_func = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Add_func.setMinimumSize(QtCore.QSize(93, 40))
        self.btn_Add_func.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_Add_func.setFont(font)
        self.btn_Add_func.setMouseTracking(False)
        self.btn_Add_func.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_Add_func.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.btn_Add_func.setAcceptDrops(True)
        self.btn_Add_func.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_Add_func.setObjectName("btn_Add_func")
        self.horizontalLayout_4.addWidget(self.btn_Add_func)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.btn_Reset_signal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Reset_signal.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_Reset_signal.setFont(font)
        self.btn_Reset_signal.setObjectName("btn_Reset_signal")
        self.verticalLayout_2.addWidget(self.btn_Reset_signal)
        self.pTE_list_func = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pTE_list_func.sizePolicy().hasHeightForWidth())
        self.pTE_list_func.setSizePolicy(sizePolicy)
        self.pTE_list_func.setMaximumSize(QtCore.QSize(1000, 80))
        self.pTE_list_func.setReadOnly(True)
        self.pTE_list_func.setObjectName("pTE_list_func")
        self.verticalLayout_2.addWidget(self.pTE_list_func)
        self.label_config_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_2.sizePolicy().hasHeightForWidth())
        self.label_config_2.setSizePolicy(sizePolicy)
        self.label_config_2.setMaximumSize(QtCore.QSize(1000, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_config_2.setFont(font)
        self.label_config_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_config_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_config_2.setScaledContents(False)
        self.label_config_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_config_2.setWordWrap(False)
        self.label_config_2.setObjectName("label_config_2")
        self.verticalLayout_2.addWidget(self.label_config_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_noise_min = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_noise_min.sizePolicy().hasHeightForWidth())
        self.label_noise_min.setSizePolicy(sizePolicy)
        self.label_noise_min.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_noise_min.setFont(font)
        self.label_noise_min.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_noise_min.setObjectName("label_noise_min")
        self.horizontalLayout.addWidget(self.label_noise_min)
        self.lineEdit_min = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_min.sizePolicy().hasHeightForWidth())
        self.lineEdit_min.setSizePolicy(sizePolicy)
        self.lineEdit_min.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_min.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_min.setObjectName("lineEdit_min")
        self.horizontalLayout.addWidget(self.lineEdit_min)
        self.comboBox_min = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_min.sizePolicy().hasHeightForWidth())
        self.comboBox_min.setSizePolicy(sizePolicy)
        self.comboBox_min.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_min.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_min.setFont(font)
        self.comboBox_min.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.comboBox_min.setObjectName("comboBox_min")
        self.comboBox_min.addItem("")
        self.comboBox_min.addItem("")
        self.comboBox_min.addItem("")
        self.comboBox_min.addItem("")
        self.comboBox_min.addItem("")
        self.comboBox_min.addItem("")
        self.comboBox_min.addItem("")
        self.comboBox_min.addItem("")
        self.comboBox_min.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_min)
        self.label_noise_max = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_noise_max.sizePolicy().hasHeightForWidth())
        self.label_noise_max.setSizePolicy(sizePolicy)
        self.label_noise_max.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_noise_max.setFont(font)
        self.label_noise_max.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_noise_max.setObjectName("label_noise_max")
        self.horizontalLayout.addWidget(self.label_noise_max)
        self.lineEdit_max = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_max.sizePolicy().hasHeightForWidth())
        self.lineEdit_max.setSizePolicy(sizePolicy)
        self.lineEdit_max.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_max.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_max.setObjectName("lineEdit_max")
        self.horizontalLayout.addWidget(self.lineEdit_max)
        self.comboBox_max = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_max.sizePolicy().hasHeightForWidth())
        self.comboBox_max.setSizePolicy(sizePolicy)
        self.comboBox_max.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_max.setMaximumSize(QtCore.QSize(80, 16777215))
        self.comboBox_max.setObjectName("comboBox_max")
        self.comboBox_max.addItem("")
        self.comboBox_max.addItem("")
        self.comboBox_max.addItem("")
        self.comboBox_max.addItem("")
        self.comboBox_max.addItem("")
        self.comboBox_max.addItem("")
        self.comboBox_max.addItem("")
        self.comboBox_max.addItem("")
        self.comboBox_max.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_max)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_numb_noise = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_numb_noise.sizePolicy().hasHeightForWidth())
        self.label_numb_noise.setSizePolicy(sizePolicy)
        self.label_numb_noise.setMinimumSize(QtCore.QSize(0, 40))
        self.label_numb_noise.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_numb_noise.setFont(font)
        self.label_numb_noise.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_numb_noise.setObjectName("label_numb_noise")
        self.horizontalLayout_2.addWidget(self.label_numb_noise)
        self.lineEdit_numb_noise = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_numb_noise.sizePolicy().hasHeightForWidth())
        self.lineEdit_numb_noise.setSizePolicy(sizePolicy)
        self.lineEdit_numb_noise.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_numb_noise.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_numb_noise.setObjectName("lineEdit_numb_noise")
        self.horizontalLayout_2.addWidget(self.lineEdit_numb_noise)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.btn_Add_noise = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Add_noise.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_Add_noise.setFont(font)
        self.btn_Add_noise.setObjectName("btn_Add_noise")
        self.verticalLayout_2.addWidget(self.btn_Add_noise)
        self.btn_Filter = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Filter.setMinimumSize(QtCore.QSize(0, 90))
        self.btn_Filter.setMaximumSize(QtCore.QSize(1000, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_Filter.setFont(font)
        self.btn_Filter.setObjectName("btn_Filter")
        self.verticalLayout_2.addWidget(self.btn_Filter)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1226, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.comboBox_min.setCurrentIndex(4)
        self.comboBox_max.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fourier_filtering"))
        self.label_x_1.setText(_translate("MainWindow", "x"))
        self.lineEdit_per_1.setText(_translate("MainWindow", "100"))
        self.btn_OK_1.setText(_translate("MainWindow", "OK"))
        self.label_x_2.setText(_translate("MainWindow", "x"))
        self.lineEdit_per_2.setText(_translate("MainWindow", "100"))
        self.btn_OK_2.setText(_translate("MainWindow", "OK"))
        self.label_x_3.setText(_translate("MainWindow", "x"))
        self.lineEdit_per_3.setText(_translate("MainWindow", "100"))
        self.btn_OK_3.setText(_translate("MainWindow", "OK"))
        self.label_time.setText(_translate("MainWindow", "FD(p/sec), POINTS"))
        self.lineEdit_FD.setText(_translate("MainWindow", "25000"))
        self.lineEdit_points.setText(_translate("MainWindow", "10000"))
        self.label_config_1.setText(_translate("MainWindow", " Configuration of source signal"))
        self.label_slct_func.setText(_translate("MainWindow", " Select function:"))
        self.comboBox_func.setCurrentText(_translate("MainWindow", "Asin(2*pi*Bx)"))
        self.comboBox_func.setItemText(0, _translate("MainWindow", "Asin(2*pi*Bx)"))
        self.comboBox_func.setItemText(1, _translate("MainWindow", "Acos(2*pi*Bx)"))
        self.label_coeff_A.setText(_translate("MainWindow", " A:"))
        self.lineEdit_coeff_A.setText(_translate("MainWindow", "1"))
        self.label_coeff_B.setText(_translate("MainWindow", " B:"))
        self.lineEdit_coeff_B.setText(_translate("MainWindow", "1"))
        self.btn_Add_func.setText(_translate("MainWindow", " Add function"))
        self.btn_Reset_signal.setText(_translate("MainWindow", "RESET THE SIGNAL"))
        self.label_config_2.setText(_translate("MainWindow", " Configuration of noise"))
        self.label_noise_min.setText(_translate("MainWindow", " Min:"))
        self.lineEdit_min.setText(_translate("MainWindow", "-1"))
        self.comboBox_min.setCurrentText(_translate("MainWindow", "0"))
        self.comboBox_min.setItemText(0, _translate("MainWindow", "-4"))
        self.comboBox_min.setItemText(1, _translate("MainWindow", "-3"))
        self.comboBox_min.setItemText(2, _translate("MainWindow", "-2"))
        self.comboBox_min.setItemText(3, _translate("MainWindow", "-1"))
        self.comboBox_min.setItemText(4, _translate("MainWindow", "0"))
        self.comboBox_min.setItemText(5, _translate("MainWindow", "1"))
        self.comboBox_min.setItemText(6, _translate("MainWindow", "2"))
        self.comboBox_min.setItemText(7, _translate("MainWindow", "3"))
        self.comboBox_min.setItemText(8, _translate("MainWindow", "4"))
        self.label_noise_max.setText(_translate("MainWindow", " Max:"))
        self.lineEdit_max.setText(_translate("MainWindow", "1"))
        self.comboBox_max.setCurrentText(_translate("MainWindow", "0"))
        self.comboBox_max.setItemText(0, _translate("MainWindow", "-4"))
        self.comboBox_max.setItemText(1, _translate("MainWindow", "-3"))
        self.comboBox_max.setItemText(2, _translate("MainWindow", "-2"))
        self.comboBox_max.setItemText(3, _translate("MainWindow", "-1"))
        self.comboBox_max.setItemText(4, _translate("MainWindow", "0"))
        self.comboBox_max.setItemText(5, _translate("MainWindow", "1"))
        self.comboBox_max.setItemText(6, _translate("MainWindow", "2"))
        self.comboBox_max.setItemText(7, _translate("MainWindow", "3"))
        self.comboBox_max.setItemText(8, _translate("MainWindow", "4"))
        self.label_numb_noise.setText(_translate("MainWindow", " Number of points:  "))
        self.btn_Add_noise.setText(_translate("MainWindow", "ADD NOISE"))
        self.btn_Filter.setText(_translate("MainWindow", "Filter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
