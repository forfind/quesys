# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_crt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QeditForm(object):
    def setupUi(self, QeditForm):
        QeditForm.setObjectName("QeditForm")
        QeditForm.resize(817, 779)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(QeditForm)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox = QtWidgets.QGroupBox(QeditForm)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setMaximumSize(QtCore.QSize(34, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setIndent(12)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.para1 = QtWidgets.QSpinBox(self.groupBox)
        self.para1.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.para1.setFont(font)
        self.para1.setObjectName("para1")
        self.horizontalLayout_2.addWidget(self.para1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setIndent(12)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setMaximumSize(QtCore.QSize(34, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setIndent(12)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.para2 = QtWidgets.QSpinBox(self.groupBox)
        self.para2.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.para2.setFont(font)
        self.para2.setObjectName("para2")
        self.horizontalLayout_6.addWidget(self.para2)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setIndent(12)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(QeditForm)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.diff_2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.diff_2.setMaximumSize(QtCore.QSize(103, 50))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.diff_2.setFont(font)
        self.diff_2.setObjectName("diff_2")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(QeditForm)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.diff_2)
        self.horizontalLayout_5.addWidget(self.diff_2)
        self.diff_3 = QtWidgets.QRadioButton(self.groupBox_3)
        self.diff_3.setMaximumSize(QtCore.QSize(103, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.diff_3.setFont(font)
        self.diff_3.setObjectName("diff_3")
        self.buttonGroup_2.addButton(self.diff_3)
        self.horizontalLayout_5.addWidget(self.diff_3)
        self.diff_1 = QtWidgets.QRadioButton(self.groupBox_3)
        self.diff_1.setMaximumSize(QtCore.QSize(103, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.diff_1.setFont(font)
        self.diff_1.setObjectName("diff_1")
        self.buttonGroup_2.addButton(self.diff_1)
        self.horizontalLayout_5.addWidget(self.diff_1)
        self.horizontalLayout_8.addWidget(self.groupBox_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.groupBox_2 = QtWidgets.QGroupBox(QeditForm)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cata_1 = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.cata_1.setFont(font)
        self.cata_1.setObjectName("cata_1")
        self.buttonGroup = QtWidgets.QButtonGroup(QeditForm)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.cata_1)
        self.horizontalLayout_4.addWidget(self.cata_1)
        self.cata_2 = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.cata_2.setFont(font)
        self.cata_2.setObjectName("cata_2")
        self.buttonGroup.addButton(self.cata_2)
        self.horizontalLayout_4.addWidget(self.cata_2)
        self.cata_3 = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.cata_3.setFont(font)
        self.cata_3.setObjectName("cata_3")
        self.buttonGroup.addButton(self.cata_3)
        self.horizontalLayout_4.addWidget(self.cata_3)
        self.cata_5 = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.cata_5.setFont(font)
        self.cata_5.setObjectName("cata_5")
        self.buttonGroup.addButton(self.cata_5)
        self.horizontalLayout_4.addWidget(self.cata_5)
        self.cata_6 = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.cata_6.setFont(font)
        self.cata_6.setObjectName("cata_6")
        self.buttonGroup.addButton(self.cata_6)
        self.horizontalLayout_4.addWidget(self.cata_6)
        self.cata_7 = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.cata_7.setFont(font)
        self.cata_7.setObjectName("cata_7")
        self.buttonGroup.addButton(self.cata_7)
        self.horizontalLayout_4.addWidget(self.cata_7)
        self.cata_4 = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.cata_4.setFont(font)
        self.cata_4.setObjectName("cata_4")
        self.buttonGroup.addButton(self.cata_4)
        self.horizontalLayout_4.addWidget(self.cata_4)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(QeditForm)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.grid1 = QtWidgets.QGridLayout()
        self.grid1.setObjectName("grid1")
        self.ctt_1 = QtWidgets.QTextEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.ctt_1.setFont(font)
        self.ctt_1.setObjectName("ctt_1")
        self.grid1.addWidget(self.ctt_1, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.grid1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.picpath1 = QtWidgets.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.picpath1.setFont(font)
        self.picpath1.setObjectName("picpath1")
        self.horizontalLayout_9.addWidget(self.picpath1)
        self.picslc1 = QtWidgets.QPushButton(self.groupBox_4)
        self.picslc1.setMinimumSize(QtCore.QSize(160, 28))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.picslc1.setFont(font)
        self.picslc1.setObjectName("picslc1")
        self.horizontalLayout_9.addWidget(self.picslc1)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(QeditForm)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.grid2 = QtWidgets.QGridLayout()
        self.grid2.setObjectName("grid2")
        self.ctt_2 = QtWidgets.QTextEdit(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.ctt_2.setFont(font)
        self.ctt_2.setObjectName("ctt_2")
        self.grid2.addWidget(self.ctt_2, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.grid2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.picpath2 = QtWidgets.QLineEdit(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.picpath2.setFont(font)
        self.picpath2.setObjectName("picpath2")
        self.horizontalLayout_10.addWidget(self.picpath2)
        self.picslc2 = QtWidgets.QPushButton(self.groupBox_5)
        self.picslc2.setMinimumSize(QtCore.QSize(160, 28))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.picslc2.setFont(font)
        self.picslc2.setObjectName("picslc2")
        self.horizontalLayout_10.addWidget(self.picslc2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.submit = QtWidgets.QPushButton(QeditForm)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.verticalLayout_3.addWidget(self.submit)

        self.retranslateUi(QeditForm)
        QtCore.QMetaObject.connectSlotsByName(QeditForm)

    def retranslateUi(self, QeditForm):
        _translate = QtCore.QCoreApplication.translate
        QeditForm.setWindowTitle(_translate("QeditForm", "Form"))
        self.groupBox.setTitle(_translate("QeditForm", "章节"))
        self.label_10.setText(_translate("QeditForm", "第"))
        self.label_7.setText(_translate("QeditForm", "章"))
        self.label_9.setText(_translate("QeditForm", "第"))
        self.label_8.setText(_translate("QeditForm", "节"))
        self.groupBox_3.setTitle(_translate("QeditForm", "难度"))
        self.diff_2.setText(_translate("QeditForm", "高"))
        self.diff_3.setText(_translate("QeditForm", "中"))
        self.diff_1.setText(_translate("QeditForm", "低"))
        self.groupBox_2.setTitle(_translate("QeditForm", "类别"))
        self.cata_1.setText(_translate("QeditForm", "选择"))
        self.cata_2.setText(_translate("QeditForm", "判断"))
        self.cata_3.setText(_translate("QeditForm", "填空"))
        self.cata_5.setText(_translate("QeditForm", "问答"))
        self.cata_6.setText(_translate("QeditForm", "算法"))
        self.cata_7.setText(_translate("QeditForm", "计算"))
        self.cata_4.setText(_translate("QeditForm", "名词解释"))
        self.groupBox_4.setTitle(_translate("QeditForm", "题目"))
        self.picslc1.setText(_translate("QeditForm", "选择图片"))
        self.groupBox_5.setTitle(_translate("QeditForm", "答案"))
        self.picslc2.setText(_translate("QeditForm", "选择图片"))
        self.submit.setText(_translate("QeditForm", "提交"))