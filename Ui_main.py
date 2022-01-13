import sys
from functools import partial

import PyQt5

from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QApplication, QVBoxLayout, QCheckBox, QGroupBox, \
    QFileDialog, QLabel, QHBoxLayout
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtCore import Qt

from database_operate import DatabaseOperate

from ui_crt import *
from ui_pdct import *
from ui_sch import *
from ui_change import *
from ui_mng import *


class mainWindow(QMainWindow):

    def __init__(self,data):
        super().__init__()
        self.init_ui(data)

    def init_ui(self,data):

        self.resize(1200, 800)

        self.main_widget = QWidget()  # 创建窗口主部件
        self.main_widget.setObjectName('main_widget')  # 对象命名
        self.main_layout = QGridLayout()  # 创建网格布局的对象
        self.main_widget.setLayout(self.main_layout)  # 将主部件设置为网格布局

        self.init_left()
        self.init_right(data)
        # 将初始化完成的左侧、右侧空间加入整体空间的网格布局
        self.main_layout.addWidget(self.lwidget, 0, 0, 1, 1)
        self.main_layout.addWidget(self.schwidget, 0, 1, 1, 6)
        self.main_layout.addWidget(self.chgwidget, 0, 1, 1, 6)
        self.main_layout.addWidget(self.addwidget, 0, 1, 1, 6)
        self.main_layout.addWidget(self.mngwidget, 0, 1, 1, 6)
        self.main_layout.addWidget(self.allwidget, 0, 1, 1, 6)
        self.main_layout.addWidget(self.pdctwidget, 0, 1, 1, 6)
        # 将右侧窗口隐藏，避免重叠
        self.addwidget.hide()
        self.schwidget.hide()
        self.chgwidget.hide()
        self.mngwidget.hide()
        self.pdctwidget.hide()

        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

    def init_left(self):
        self.font = QtGui.QFont()
        self.font.setFamily('微软雅黑')
        self.font.setBold(True)
        self.font.setPointSize(15)
        self.font.setWeight(10)

        self.lwidget = QWidget()
        self.lwidget.setObjectName('lwidget')

        self.llayout = QVBoxLayout()
        self.lwidget.setLayout(self.llayout)

        self.addbtn = QtWidgets.QPushButton(self.lwidget)
        self.addbtn.setObjectName("addbtn")
        self.addbtn.setFont(self.font)  #载入字体设置
        self.addbtn.setFixedHeight(140)
        self.addbtn.setCheckable(True)
        self.addbtn.setFlat(True)  # 透明背景

        self.schbtn = QtWidgets.QPushButton(self.lwidget)
        self.schbtn.setObjectName("findbtn")
        self.schbtn.setFont(self.font)  #载入字体设置
        self.schbtn.setFixedHeight(140)
        self.schbtn.setCheckable(True)
        self.schbtn.setFlat(True)  # 透明背景

        self.chgbtn = QtWidgets.QPushButton(self.lwidget)
        self.chgbtn.setObjectName("editbtn")
        self.chgbtn.hide()

        self.mngbtn = QtWidgets.QPushButton(self.lwidget)
        self.mngbtn.setObjectName("mngbtn")
        self.mngbtn.setFont(self.font)  #载入字体设置
        self.mngbtn.setFixedHeight(140)
        self.mngbtn.setCheckable(True)
        self.mngbtn.setFlat(True)  # 透明背景

        self.pdctbtn = QtWidgets.QPushButton(self.lwidget)
        self.pdctbtn.setObjectName("probtn")
        self.pdctbtn.setFont(self.font)  #载入字体设置
        self.pdctbtn.setFixedHeight(140)
        self.pdctbtn.setCheckable(True)
        self.pdctbtn.setFlat(True)  # 透明背景

        self.disbtn = QtWidgets.QPushButton(self.lwidget)
        self.disbtn.setObjectName("disbtn")
        self.disbtn.setFont(self.font)  #载入字体设置
        self.disbtn.setFixedHeight(140)
        self.disbtn.setCheckable(True)
        self.disbtn.setFlat(True)  # 透明背景

        _translate = QtCore.QCoreApplication.translate
        self.addbtn.setText(_translate("MainWindow", "添加题目"))
        self.schbtn.setText(_translate("MainWindow", "检索题目"))
        self.chgbtn.setText(_translate("MainWindow", "修改题目"))
        self.mngbtn.setText(_translate("MainWindow", "试卷管理"))
        self.pdctbtn.setText(_translate("MainWindow", "生成试卷"))
        self.disbtn.setText(_translate("MainWindow", "试题统计"))
        self.llayout.addWidget(self.addbtn)
        self.llayout.addWidget(self.schbtn)
        self.llayout.addWidget(self.chgbtn)
        self.llayout.addWidget(self.mngbtn)
        self.llayout.addWidget(self.pdctbtn)
        self.llayout.addWidget(self.disbtn)

        self.addbtn.clicked.connect(self.showadd)
        self.schbtn.clicked.connect(self.showsch)
        self.chgbtn.clicked.connect(self.showchg)
        self.mngbtn.clicked.connect(self.showmng)
        self.pdctbtn.clicked.connect(self.showpdct)

    def init_right(self,data):
        self.addwidget = QWidget()
        self.addwidget.setObjectName('addwidget')
        self.addui = Ui_QeditForm()
        self.addui.setupUi(self.addwidget)
        self.addui.picslc1.clicked.connect(self.openfile1)
        self.addui.picslc2.clicked.connect(self.openfile2)

        self.schwidget = QWidget()
        self.schwidget.setObjectName('schwidget')
        self.schui = Ui_schForm()
        self.schui.setupUi(self.schwidget)
        self.schui.difficulty.stateChanged.connect(self.change_state)
        self.schui.category.stateChanged.connect(self.change_state)
        self.schui.chapter.stateChanged.connect(self.change_state)

        self.chgwidget = QWidget()
        self.chgwidget.setObjectName('chgwidget')
        self.chgui = Ui_chgForm()
        self.chgui.setupUi(self.chgwidget)


        self.mngwidget = QWidget()
        self.mngwidget.setObjectName('mngwidget')
        self.mngui = Ui_mngForm()
        self.mngui.setupUi(self.mngwidget)
        self.mngui.editwid.hide()

        self.allwidget = self.getview(data)
        self.allwidget.setObjectName('allwidget')

        self.pdctwidget = QWidget()
        self.pdctwidget.setObjectName('pdctwidget')
        self.pdctui = Ui_pdctForm()
        self.pdctui.setupUi(self.pdctwidget)
        self.chaplist = []

    def openfile1(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            print(fname[0])
            self.pic1data = open(fname[0], 'rb').read()
            self.addui.picpath1.setText(fname[0])

            pixmap = QPixmap(fname[0])
            self.lbl1 = QLabel(self)
            self.lbl1.setPixmap(pixmap)
            self.addui.grid1.addWidget(self.lbl1,0,2,1,1)
            self.lbl1.setScaledContents(True)

    def openfile2(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            print(fname[0])
            self.pic2data = open(fname[0], 'rb').read()
            print("picdata",self.pic2data)
            self.addui.picpath2.setText(fname[0])
            pixmap = QPixmap(fname[0])
            self.lbl2 = QLabel(self)
            self.lbl2.setPixmap(pixmap)
            self.addui.grid2.addWidget(self.lbl2,0,2,1,1)
            self.lbl2.setScaledContents(True)

    def change_state(self):
        ui = self.schui
        if ui.difficulty == self.sender():
            state = ui.difficulty.checkState()
            ui.h.setChecked(state)
            ui.l.setChecked(state)
            ui.m.setChecked(state)
        elif ui.category == self.sender():
            state = ui.category.checkState()
            ui.xz.setChecked(state)
            ui.tk.setChecked(state)
            ui.mc.setChecked(state)
            ui.pd.setChecked(state)
            ui.wd.setChecked(state)
            ui.js.setChecked(state)
            ui.sf.setChecked(state)
        else:
            state = ui.chapter.checkState()
            ui.ch0.setChecked(state)
            ui.ch1.setChecked(state)
            ui.ch2.setChecked(state)
            ui.ch3.setChecked(state)
            ui.ch4.setChecked(state)
            ui.ch5.setChecked(state)
            ui.ch6.setChecked(state)
            ui.ch7.setChecked(state)
            ui.ch8.setChecked(state)
            ui.ch9.setChecked(state)
            ui.ch10.setChecked(state)
            ui.ch11.setChecked(state)

    def create_piechart(self,ls):
        # 创建QPieSeries对象，它用来存放饼图的数据
        series = PyQt5.QtChart.QPieSeries()
        # append方法中的数字，代表的是权重，完成可以改成其它，如80,70,60等等
        for i in range(len(ls)):
            series.append(str(ls[i][0])+":"+str(ls[i][1]), ls[i][1])

        # 单独处理某个扇区
        slice = PyQt5.QtChart.QPieSlice()

        # 这里要处理的是python项，是依据前面append的顺序，如果是处理C++项的话，那索引就是3
        slice = series.slices()[0]

        # 突出显示，设置颜色
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.red, 2))
        slice.setBrush(Qt.red)

        # 创建QChart实例，它是PyQt5中的类
        chart = PyQt5.QtChart.QChart()
        # QLegend类是显示图表的图例，先隐藏掉
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()

        # 设置动画效果
        chart.setAnimationOptions(PyQt5.QtChart.QChart.SeriesAnimations)

        # 设置标题
        chart.setTitle("题库试题分布")

        chart.legend().setVisible(True)

        # 对齐方式
        chart.legend().setAlignment(Qt.AlignBottom)

        # 创建ChartView，它是显示图表的控件
        chartview = PyQt5.QtChart.QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        return chartview

    def getview(self,data):
        re_wid = QWidget()
        re_layout = QGridLayout()
        for i in range(len(data)):
            chartview = self.create_piechart(data[i])
            if i == 0:
                re_layout.addWidget(chartview,0,0,1,1)
            elif i == 1:
                re_layout.addWidget(chartview,1,0,1,2)
            else:
                re_layout.addWidget(chartview,0,1,1,1)

        re_wid.setLayout(re_layout)
        return re_wid

    def showadd(self):
        self.addwidget.show()
        self.schwidget.hide()
        self.chgwidget.hide()
        self.mngwidget.hide()
        self.allwidget.hide()
        self.pdctwidget.hide()
        self.addbtn.setChecked(True)
        self.schbtn.setChecked(False)
        self.mngbtn.setChecked(False)
        self.pdctbtn.setChecked(False)
        self.disbtn.setChecked(False)

    def showsch(self):
        self.addwidget.hide()
        self.schwidget.show()
        self.chgwidget.hide()
        self.mngwidget.hide()
        self.allwidget.hide()
        self.pdctwidget.hide()
        self.addbtn.setChecked(False)
        self.schbtn.setChecked(True)
        self.mngbtn.setChecked(False)
        self.pdctbtn.setChecked(False)
        self.disbtn.setChecked(False)

    def showchg(self):
        self.addwidget.hide()
        self.schwidget.hide()
        self.chgwidget.show()
        self.mngwidget.hide()
        self.allwidget.hide()
        self.pdctwidget.hide()
        self.addbtn.setChecked(False)
        self.schbtn.setChecked(False)
        self.mngbtn.setChecked(False)
        self.pdctbtn.setChecked(False)
        self.disbtn.setChecked(False)

    def showmng(self):
        self.addwidget.hide()
        self.schwidget.hide()
        self.chgwidget.hide()
        self.mngwidget.show()
        self.allwidget.hide()
        self.pdctwidget.hide()
        self.addbtn.setChecked(False)
        self.schbtn.setChecked(False)
        self.mngbtn.setChecked(True)
        self.pdctbtn.setChecked(False)
        self.disbtn.setChecked(False)

    def showpdct(self):
        self.addwidget.hide()
        self.schwidget.hide()
        self.chgwidget.hide()
        self.mngwidget.hide()
        self.allwidget.hide()
        self.pdctwidget.show()
        self.addbtn.setChecked(False)
        self.schbtn.setChecked(False)
        self.mngbtn.setChecked(False)
        self.pdctbtn.setChecked(True)
        self.disbtn.setChecked(False)

    def showall(self,data):

        self.allwidget.hide()
        self.addwidget.hide()
        self.schwidget.hide()
        self.chgwidget.hide()
        self.mngwidget.hide()
        self.pdctwidget.hide()


        self.allwidget = self.getview(data)
        self.main_layout.addWidget(self.allwidget, 0, 1, 1, 6)
        self.allwidget.show()
        self.addbtn.setChecked(False)
        self.schbtn.setChecked(False)
        self.mngbtn.setChecked(False)
        self.pdctbtn.setChecked(False)
        self.disbtn.setChecked(True)

    def set_pdctview(self, category_list, chapter_list):
        ui = self.pdctui

        ui.sfwid.hide()
        ui.pdwid.hide()
        ui.xzwid.hide()
        ui.wdwid.hide()
        ui.mcwid.hide()
        ui.jswid.hide()
        ui.tkwid.hide()

        ui.xz.setChecked(False)
        ui.mc.setChecked(False)
        ui.tk.setChecked(False)
        ui.sf.setChecked(False)
        ui.js.setChecked(False)
        ui.wd.setChecked(False)
        ui.pd.setChecked(False)

        for i in range(ui.chaplayout.count()):
            print(ui.chaplayout.count())
            ui.chaplayout.itemAt(i).widget().deleteLater()

        for i in range(len(category_list)):
            if category_list[i][0] == "判断":
                ui.pdwid.show()
            if category_list[i][0] == "填空":
                ui.tkwid.show()
            if category_list[i][0] == "名词解释":
                ui.mcwid.show()
            if category_list[i][0] == "计算":
                ui.jswid.show()
            if category_list[i][0] == "算法":
                ui.sfwid.show()
            if category_list[i][0] == "问答":
                ui.wdwid.show()
            if category_list[i][0] == "选择":
                ui.xzwid.show()
        for i in range(len(chapter_list)):
            chap = chapter_list[i][0]
            Chbox = QCheckBox("第"+chap+"章",parent=ui.range)
            ui.chaplayout.addWidget(Chbox)
# TEST:
def check_paper(ui):
    list = ui.paperlist
    print(list)
    if list.count() > 0:
        for i in range(list.count()):
            item = list.item(i)
            # 选择被选中的试卷
            if item.isSelected():
                codestr = str(list.item(i).text()).split()[1]
                code = int(codestr)
                print("code:",code)

                ui.mngwid.hide()
                ui.editwid.show()
                ui.paperlist.clear()
                opr = DatabaseOperate("104.168.172.47", "forfind", "000000", "exercise")
                ques_data = opr.query_exercise_from_paper(code)
                print(ques_data)
                for i in range(ques_data.shape[0]):
                    print(str(ques_data.at[i,"ExerciseCode"])+' '+str(ques_data.at[i,"number"])+' '+str(ques_data.at[i,"point"]))
                    ui.paperlist.addItem("编号 "+str(ques_data.at[i,"ExerciseCode"])+'\t'+"试卷中序号 "+str(ques_data.at[i,"number"])+'\t'+"分值 "+str(ques_data.at[i,"point"]))
                break
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("3.png")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        lbl.setScaledContents(True)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()
def main():
    app = QApplication(sys.argv)
    mainwin = mainWindow([[['低', 402], ['高', 392], ['中', 396]], [['选择', 225], ['判断', 180], ['填空', 181], ['名词解释', 153], ['问答', 150], ['算法', 151], ['计算', 150]], [['1', 219], ['2', 217], ['3', 216], ['7', 96], ['4', 217], ['5', 216], ['6', 4], ['8', 3], ['9', 2]]])



    ex = Example()
    mainwin.mngui.paperlist.addItem("1 8 3")
    mainwin.mngui.chkbtn.clicked.connect(partial(check_paper,mainwin.mngui))
    mainwin.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
