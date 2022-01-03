import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QApplication, QVBoxLayout


from ui_Qedit import *
from ui_pdct import *
from ui_sch import *
from ui_change import *

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):

        self.resize(1000, 800)

        self.main_widget = QWidget()  # 创建窗口主部件
        self.main_widget.setObjectName('main_widget')  # 对象命名
        self.main_layout = QGridLayout()  # 创建网格布局的对象
        self.main_widget.setLayout(self.main_layout)  # 将主部件设置为网格布局

        self.init_left()
        self.init_right()
        # 将初始化完成的左侧、右侧空间加入整体空间的网格布局
        self.main_layout.addWidget(self.lwidget, 0, 0, 1, 1)
        self.main_layout.addWidget(self.schwidget, 0, 1, 1, 6)
        self.main_layout.addWidget(self.chgwidget, 0, 1, 1, 6)
        self.main_layout.addWidget(self.addwidget, 0, 1, 1, 6)
        self.main_layout.addWidget(self.mngwidget, 0, 1, 1, 6)
        # 将右侧窗口隐藏，避免重叠
        self.addwidget.hide()
        self.schwidget.hide()
        self.chgwidget.hide()
        self.mngwidget.hide()

        self.setCentralWidget(self.main_widget)  # 设置窗口主部件


    def init_left(self):
        self.lwidget = QWidget()
        self.lwidget.setObjectName('lwidget')

        self.llayout = QVBoxLayout()
        self.lwidget.setLayout(self.llayout)

        self.addbtm = QtWidgets.QPushButton(self.lwidget)
        self.addbtm.setObjectName("addbtm")
        self.schbtm = QtWidgets.QPushButton(self.lwidget)
        self.schbtm.setObjectName("findbtm")
        self.chgbtm = QtWidgets.QPushButton(self.lwidget)
        self.chgbtm.setObjectName("editbtm")
        self.mngbtm = QtWidgets.QPushButton(self.lwidget)
        self.mngbtm.setObjectName("mngbtm")
        self.pdctbtm = QtWidgets.QPushButton(self.lwidget)
        self.pdctbtm.setObjectName("probtm")
        self.disbtm = QtWidgets.QPushButton(self.lwidget)
        self.disbtm.setObjectName("disbtm")

        _translate = QtCore.QCoreApplication.translate
        self.addbtm.setText(_translate("MainWindow", "添加题目"))
        self.schbtm.setText(_translate("MainWindow", "检索题目"))
        self.chgbtm.setText(_translate("MainWindow", "修改题目"))
        self.mngbtm.setText(_translate("MainWindow", "试卷管理"))
        self.pdctbtm.setText(_translate("MainWindow", "生成试卷"))
        self.disbtm.setText(_translate("MainWindow", "试题统计"))
        self.llayout.addWidget(self.addbtm)
        self.llayout.addWidget(self.schbtm)
        self.llayout.addWidget(self.chgbtm)
        self.llayout.addWidget(self.mngbtm)
        self.llayout.addWidget(self.pdctbtm)
        self.llayout.addWidget(self.disbtm)

        self.addbtm.clicked.connect(self.showadd)
        self.schbtm.clicked.connect(self.showsch)
        self.chgbtm.clicked.connect(self.showchg)
        self.mngbtm.clicked.connect(self.showmng)



    def init_right(self):
        self.addwidget = QWidget()
        self.addwidget.setObjectName('addwidget')
        self.addui = Ui_QeditForm()
        self.addui.setupUi(self.addwidget)

        self.schwidget = QWidget()
        self.schwidget.setObjectName('schwidget')
        self.schui = Ui_schForm()
        self.schui.setupUi(self.schwidget)

        self.chgwidget = QWidget()
        self.chgwidget.setObjectName('chgwidget')
        self.chgui = Ui_chgForm()
        self.chgui.setupUi(self.chgwidget)

        self.mngwidget = QWidget()
        self.mngwidget.setObjectName('mngwidget')
        #self.mngui = Ui_mngForm()
        #self.mngui.setupUi(self.mngwidget)

    def showadd(self):
        self.addwidget.show()
        self.schwidget.hide()
        self.chgwidget.hide()
        self.mngwidget.hide()

    def showsch(self):
        self.addwidget.hide()
        self.schwidget.show()
        self.chgwidget.hide()
        self.mngwidget.hide()

    def showchg(self):
        self.addwidget.hide()
        self.schwidget.hide()
        self.chgwidget.show()
        self.mngwidget.hide()

    def showmng(self):
        self.addwidget.hide()
        self.schwidget.hide()
        self.chgwidget.hide()
        self.mngwidget.show()




def main():
    app = QApplication(sys.argv)
    manuwin = mainWindow()
    manuwin.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
