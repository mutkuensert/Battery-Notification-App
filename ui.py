# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(459, 255)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(459, 255))
        MainWindow.setMaximumSize(QtCore.QSize(459, 255))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 431, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(75, 0))
        self.label_4.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.sliderLowerLimit = QtWidgets.QSlider(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderLowerLimit.sizePolicy().hasHeightForWidth())
        self.sliderLowerLimit.setSizePolicy(sizePolicy)
        self.sliderLowerLimit.setMaximum(95)
        self.sliderLowerLimit.setOrientation(QtCore.Qt.Horizontal)
        self.sliderLowerLimit.setObjectName("sliderLowerLimit")
        self.horizontalLayout_4.addWidget(self.sliderLowerLimit)
        self.lowerLimitValue = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lowerLimitValue.setObjectName("lowerLimitValue")
        self.horizontalLayout_4.addWidget(self.lowerLimitValue)
        self.horizontalLayout_4.setStretch(0, 10)
        self.horizontalLayout_4.setStretch(1, 80)
        self.horizontalLayout_4.setStretch(2, 20)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(75, 0))
        self.label_3.setMaximumSize(QtCore.QSize(757, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.sliderUpperLimit = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.sliderUpperLimit.setMinimum(5)
        self.sliderUpperLimit.setMaximum(100)
        self.sliderUpperLimit.setOrientation(QtCore.Qt.Horizontal)
        self.sliderUpperLimit.setObjectName("sliderUpperLimit")
        self.horizontalLayout_3.addWidget(self.sliderUpperLimit)
        self.upperLimitValue = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.upperLimitValue.setObjectName("upperLimitValue")
        self.horizontalLayout_3.addWidget(self.upperLimitValue)
        self.horizontalLayout_3.setStretch(0, 10)
        self.horizontalLayout_3.setStretch(1, 80)
        self.horizontalLayout_3.setStretch(2, 20)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.latencyTime = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.latencyTime.setMinimumSize(QtCore.QSize(70, 0))
        self.latencyTime.setMinimum(5)
        self.latencyTime.setMaximum(60)
        self.latencyTime.setObjectName("latencyTime")
        self.horizontalLayout.addWidget(self.latencyTime)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.numberOfNotifications = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.numberOfNotifications.setMinimumSize(QtCore.QSize(70, 0))
        self.numberOfNotifications.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.numberOfNotifications.setMinimum(1)
        self.numberOfNotifications.setMaximum(100)
        self.numberOfNotifications.setObjectName("numberOfNotifications")
        self.horizontalLayout_2.addWidget(self.numberOfNotifications)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Battery Notification"))
        self.label_4.setText(_translate("MainWindow", "Lower Limit:"))
        self.lowerLimitValue.setText(_translate("MainWindow", "Value: "))
        self.label_3.setText(_translate("MainWindow", "Upper Limit:"))
        self.upperLimitValue.setText(_translate("MainWindow", "Value: "))
        self.label.setText(_translate("MainWindow", "Duration between notifications(sec):"))
        self.label_2.setText(_translate("MainWindow", "Number of notifications:"))