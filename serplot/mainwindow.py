# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Feb 17 04:39:51 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1024, 700)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.w_box_source = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_box_source.sizePolicy().hasHeightForWidth())
        self.w_box_source.setSizePolicy(sizePolicy)
        self.w_box_source.setObjectName(_fromUtf8("w_box_source"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.w_box_source)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.w_port = QtGui.QComboBox(self.w_box_source)
        self.w_port.setObjectName(_fromUtf8("w_port"))
        self.horizontalLayout_3.addWidget(self.w_port)
        self.w_protocol = QtGui.QComboBox(self.w_box_source)
        self.w_protocol.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_protocol.sizePolicy().hasHeightForWidth())
        self.w_protocol.setSizePolicy(sizePolicy)
        self.w_protocol.setFrame(True)
        self.w_protocol.setObjectName(_fromUtf8("w_protocol"))
        self.w_protocol.addItem(_fromUtf8(""))
        self.w_protocol.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.w_protocol)
        self.w_channels = QtGui.QSpinBox(self.w_box_source)
        self.w_channels.setPrefix(_fromUtf8(""))
        self.w_channels.setMinimum(1)
        self.w_channels.setMaximum(6)
        self.w_channels.setObjectName(_fromUtf8("w_channels"))
        self.horizontalLayout_3.addWidget(self.w_channels)
        self.w_connect = QtGui.QPushButton(self.w_box_source)
        self.w_connect.setObjectName(_fromUtf8("w_connect"))
        self.horizontalLayout_3.addWidget(self.w_connect)
        self.gridLayout.addWidget(self.w_box_source, 0, 0, 1, 1)
        self.w_box_filtering = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_box_filtering.sizePolicy().hasHeightForWidth())
        self.w_box_filtering.setSizePolicy(sizePolicy)
        self.w_box_filtering.setObjectName(_fromUtf8("w_box_filtering"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.w_box_filtering)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.w_filter_none = QtGui.QRadioButton(self.w_box_filtering)
        self.w_filter_none.setChecked(True)
        self.w_filter_none.setObjectName(_fromUtf8("w_filter_none"))
        self.horizontalLayout.addWidget(self.w_filter_none)
        self.w_filter_sma = QtGui.QRadioButton(self.w_box_filtering)
        self.w_filter_sma.setObjectName(_fromUtf8("w_filter_sma"))
        self.horizontalLayout.addWidget(self.w_filter_sma)
        self.w_filter_window = QtGui.QSpinBox(self.w_box_filtering)
        self.w_filter_window.setEnabled(False)
        self.w_filter_window.setSuffix(_fromUtf8(""))
        self.w_filter_window.setMinimum(1)
        self.w_filter_window.setObjectName(_fromUtf8("w_filter_window"))
        self.horizontalLayout.addWidget(self.w_filter_window)
        self.gridLayout.addWidget(self.w_box_filtering, 0, 2, 1, 1)
        self.w_box_plot = QtGui.QGroupBox(self.centralwidget)
        self.w_box_plot.setTitle(_fromUtf8(""))
        self.w_box_plot.setObjectName(_fromUtf8("w_box_plot"))
        self.gridLayout.addWidget(self.w_box_plot, 1, 0, 1, 4)
        self.w_box_plotting_control = QtGui.QGroupBox(self.centralwidget)
        self.w_box_plotting_control.setEnabled(True)
        self.w_box_plotting_control.setObjectName(_fromUtf8("w_box_plotting_control"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.w_box_plotting_control)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.w_button_autozoom = QtGui.QPushButton(self.w_box_plotting_control)
        self.w_button_autozoom.setCheckable(True)
        self.w_button_autozoom.setChecked(True)
        self.w_button_autozoom.setObjectName(_fromUtf8("w_button_autozoom"))
        self.horizontalLayout_2.addWidget(self.w_button_autozoom)
        self.w_button_pause = QtGui.QPushButton(self.w_box_plotting_control)
        self.w_button_pause.setEnabled(True)
        self.w_button_pause.setCheckable(True)
        self.w_button_pause.setAutoDefault(False)
        self.w_button_pause.setObjectName(_fromUtf8("w_button_pause"))
        self.horizontalLayout_2.addWidget(self.w_button_pause)
        self.gridLayout.addWidget(self.w_box_plotting_control, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(513, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.w_protocol.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial Plotting", None))
        self.w_box_source.setTitle(_translate("MainWindow", "Source", None))
        self.w_protocol.setItemText(0, _translate("MainWindow", "Serial Protocol 1", None))
        self.w_protocol.setItemText(1, _translate("MainWindow", "Serial Protocol 2", None))
        self.w_channels.setSuffix(_translate("MainWindow", " channel(s)", None))
        self.w_connect.setText(_translate("MainWindow", "Connect", None))
        self.w_box_filtering.setTitle(_translate("MainWindow", "Filtering", None))
        self.w_filter_none.setText(_translate("MainWindow", "None", None))
        self.w_filter_sma.setText(_translate("MainWindow", "SMA", None))
        self.w_filter_window.setPrefix(_translate("MainWindow", "n=", None))
        self.w_box_plotting_control.setTitle(_translate("MainWindow", "Plotting", None))
        self.w_button_autozoom.setText(_translate("MainWindow", "Auto zoom", None))
        self.w_button_pause.setText(_translate("MainWindow", "Pause", None))

