# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pdct.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pdctForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(705, 497)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.sf = QtWidgets.QCheckBox(self.groupBox)
        self.sf.setObjectName("sf")
        self.horizontalLayout_11.addWidget(self.sf)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.sfnum = QtWidgets.QLineEdit(self.groupBox)
        self.sfnum.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sfnum.setObjectName("sfnum")
        self.horizontalLayout_11.addWidget(self.sfnum)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.mc = QtWidgets.QCheckBox(self.groupBox)
        self.mc.setObjectName("mc")
        self.horizontalLayout_8.addWidget(self.mc)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.mcnum = QtWidgets.QLineEdit(self.groupBox)
        self.mcnum.setMaximumSize(QtCore.QSize(60, 16777215))
        self.mcnum.setObjectName("mcnum")
        self.horizontalLayout_8.addWidget(self.mcnum)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pd = QtWidgets.QCheckBox(self.groupBox)
        self.pd.setObjectName("pd")
        self.horizontalLayout_9.addWidget(self.pd)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.pdnum = QtWidgets.QLineEdit(self.groupBox)
        self.pdnum.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pdnum.setObjectName("pdnum")
        self.horizontalLayout_9.addWidget(self.pdnum)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.tk = QtWidgets.QCheckBox(self.groupBox)
        self.tk.setObjectName("tk")
        self.horizontalLayout_23.addWidget(self.tk)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem3)
        self.tknum = QtWidgets.QLineEdit(self.groupBox)
        self.tknum.setMaximumSize(QtCore.QSize(60, 16777215))
        self.tknum.setObjectName("tknum")
        self.horizontalLayout_23.addWidget(self.tknum)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_23.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_23)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.js = QtWidgets.QCheckBox(self.groupBox)
        self.js.setObjectName("js")
        self.horizontalLayout_10.addWidget(self.js)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.jsnum = QtWidgets.QLineEdit(self.groupBox)
        self.jsnum.setMaximumSize(QtCore.QSize(60, 16777215))
        self.jsnum.setObjectName("jsnum")
        self.horizontalLayout_10.addWidget(self.jsnum)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.wd = QtWidgets.QCheckBox(self.groupBox)
        self.wd.setObjectName("wd")
        self.horizontalLayout_7.addWidget(self.wd)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.wdnum = QtWidgets.QLineEdit(self.groupBox)
        self.wdnum.setMaximumSize(QtCore.QSize(60, 16777215))
        self.wdnum.setObjectName("wdnum")
        self.horizontalLayout_7.addWidget(self.wdnum)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.xz = QtWidgets.QCheckBox(self.groupBox)
        self.xz.setObjectName("xz")
        self.horizontalLayout_21.addWidget(self.xz)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem7)
        self.xznum = QtWidgets.QLineEdit(self.groupBox)
        self.xznum.setMaximumSize(QtCore.QSize(60, 16777215))
        self.xznum.setObjectName("xznum")
        self.horizontalLayout_21.addWidget(self.xznum)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_21.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_21)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_28.addWidget(self.label_7)
        self.lowpct = QtWidgets.QLineEdit(self.groupBox_2)
        self.lowpct.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lowpct.setObjectName("lowpct")
        self.horizontalLayout_28.addWidget(self.lowpct)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_28.addWidget(self.label_14)
        self.verticalLayout_3.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_29.addWidget(self.label_6)
        self.highpct = QtWidgets.QLineEdit(self.groupBox_2)
        self.highpct.setMaximumSize(QtCore.QSize(60, 16777215))
        self.highpct.setObjectName("highpct")
        self.horizontalLayout_29.addWidget(self.highpct)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_29.addWidget(self.label_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.range = QtWidgets.QGroupBox(Form)
        self.range.setObjectName("range")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.range)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.c14 = QtWidgets.QVBoxLayout()
        self.c14.setObjectName("c14")
        self.horizontalLayout_3.addLayout(self.c14)
        self.c58 = QtWidgets.QVBoxLayout()
        self.c58.setObjectName("c58")
        self.horizontalLayout_3.addLayout(self.c58)
        self.c912 = QtWidgets.QVBoxLayout()
        self.c912.setObjectName("c912")
        self.horizontalLayout_3.addLayout(self.c912)
        self.verticalLayout_4.addWidget(self.range)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "题型数量"))
        self.sf.setText(_translate("Form", "算法"))
        self.label_13.setText(_translate("Form", "个"))
        self.mc.setText(_translate("Form", "名词解释"))
        self.label_10.setText(_translate("Form", "个"))
        self.pd.setText(_translate("Form", "判断"))
        self.label_11.setText(_translate("Form", "个"))
        self.tk.setText(_translate("Form", "填空"))
        self.label_4.setText(_translate("Form", "个"))
        self.js.setText(_translate("Form", "计算"))
        self.label_12.setText(_translate("Form", "个"))
        self.wd.setText(_translate("Form", "问答"))
        self.label_9.setText(_translate("Form", "个"))
        self.xz.setText(_translate("Form", "选择"))
        self.label_3.setText(_translate("Form", "个"))
        self.groupBox_2.setTitle(_translate("Form", "难度比例"))
        self.label_7.setText(_translate("Form", "低难度"))
        self.label_14.setText(_translate("Form", "%"))
        self.label_6.setText(_translate("Form", "高难度"))
        self.label_8.setText(_translate("Form", "%"))
        self.range.setTitle(_translate("Form", "题目范围"))
        self.pushButton.setText(_translate("Form", "生成题目"))
