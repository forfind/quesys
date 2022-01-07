import random

import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QPainter

from Ui_main import *
from functools import partial
from database_operate import *
from PyQt5.QtWidgets import *

opr = DatabaseOperate("104.168.172.47", "forfind", "000000", "exercise")
pd.set_option('display.max_columns', None,
              'display.max_rows', None,
              'display.max_colwidth', None,
              'display.width', 100,
              'expand_frame_repr', False)

def test(ui):
    cata = ''
    print("succ")
    cata = "'" + ui.ctt_1.toPlainText() + "'"

    print(cata)


def add(ui):
    chap = int(ui.para1.text())
    sec = int(ui.para2.text())
    category = ''
    diff = ''
    if ui.category_1.isChecked():
        category = "'选择'"
    if ui.category_2.isChecked():
        category = "'判断'"
    if ui.category_3.isChecked():
        category = "'填空'"
    if ui.category_4.isChecked():
        category = "'名词解释'"
    if ui.category_5.isChecked():
        category = "'问答'"
    if ui.category_6.isChecked():
        category = "'算法'"
    if ui.category_7.isChecked():
        category = "'计算'"
    if ui.diff_1.isChecked():
        diff = "'低'"
    if ui.diff_2.isChecked():
        diff = "'高'"
    if ui.diff_3.isChecked():
        diff = "'中'"

    ques = "'" + ui.ctt_1.toPlainText() + "'"
    ans = "'" + ui.ctt_2.toPlainText() + "'"
    print("章：", chap, "节:", sec, "类别:", category, "难度:", diff)
    print("题目", ques, "答案", ans)

    global opr
    opr.add_exercise(ques, "null", ans, "null", category, chap, sec, diff)

    ui.ctt_1.clear()
    ui.ctt_2.clear()


def sreach(ui):
    global opr
    value = ui.inputtxt.toPlainText()
    numls = []
    ui.outputlist.clear()
    if ui.keybtn.isChecked():
        d = opr.query_exercise("all")
        for i in range(d.shape[0]):
            if value  in d.at[i,"topic"]:
                ui.outputlist.addItem(str(d.at[i,"ExerciseCode"])+' '+str(d.at[i,"topic"])+' '+str(d.at[i,"answer"]))
        return
    if ui.codebtn.isChecked():
        d = opr.query_exercise("exercise_base_info.ExerciseCode="+value)
        print(d)

    if ui.catabtn.isChecked():
        cata = "'"+value+"'"
        d = opr.query_exercise("category="+cata)
        print(d)
    print(d[["ExerciseCode","topic","answer"]])

    for i in range(d.shape[0]):
        ui.outputlist.addItem(str(d.at[i,"ExerciseCode"])+' '+str(d.at[i,"topic"])+' '+str(d.at[i,"answer"]))
        #print(str(d.at[i,"ExerciseCode"])+' '+str(d.at[i,"topic"])+' '+str(d.at[i,"answer"]))

def remove_item(list):
    global opr
    if list.count() > 0:
        for i in range(list.count()):
            item = list.item(i)

            if item.isSelected():
                code = int(str(list.item(i).text()).split()[0])

                print("code:",code)

                list.removeItemWidget(list.takeItem(i))
                # 此处+对话框
                global opr
                opr.delete_exercise(code)
                break
def Df2Ls(data):
    datalist = []
    for i in range(len(data)):
        datalist.append([str(data.iat[i,0]),int(data.iat[i,1])])
    return datalist

def statistic_info():
    global opr
    data = opr.statistic_exercise("difficulty")
    print(data)
    datalist = Df2Ls(data)
    print(datalist)
    return datalist

def updata_info(win):
    datalist = statistic_info()
    win.showall(datalist)

def create_paper(ui):
    cate=[]
    if ui.xz.isChecked():
        ca_num = []
        ca_num.append("'选择'")
        ca_num.append(int(ui.xznum.text()))
        cate.append(ca_num)

    if ui.tk.isChecked():
        ca_num = []
        ca_num.append("'填空'")
        ca_num.append(int(ui.tknum.text()))
        cate.append(ca_num)
    if ui.sf.isChecked():
        ca_num = []
        ca_num.append("'算法'")
        ca_num.append(int(ui.sfnum.text()))
        cate.append(ca_num)
    if ui.js.isChecked():
        ca_num = []
        ca_num.append("'计算'")
        ca_num.append(int(ui.jsnum.text()))
        cate.append(ca_num)
    if ui.mc.isChecked():
        ca_num = []
        ca_num.append("'名词解释'")
        ca_num.append(int(ui.mcnum.text()))
        cate.append(ca_num)
    if ui.pd.isChecked():
        ca_num = []
        ca_num.append("'判断'")
        ca_num.append(int(ui.pdnum.text()))
        cate.append(ca_num)
    if ui.wd.isChecked():
        ca_num = []
        ca_num.append("'问答'")
        ca_num.append(int(ui.wdnum.text()))
        cate.append(ca_num)
    chap=[]
    for wid in ui.range.children():
        if isinstance(wid, QCheckBox):
            if wid.isChecked():
                chap.append(int(wid.text()[1:-1]))
    diff=[]
    diff.append(float(int(ui.highpct.text())/100))
    diff.append(float(int(ui.lowpct.text())/100))
    print(cate,chap,diff)
    create_paper_with(cate,chap,diff)

def create_paper_with(cate,chap,diff):
    global opr
    difficulty = ['高','中','低']
    chstr = str(chap)[1:-1]
    final = []
    for i_ca in range(len(cate)):
        ca_diff=[[],[],[]]
        print(ca_diff)
        print("category = "+cate[i_ca][0]+" and chapter in "+"("+chstr+")")
        # 按【类型】查询数据，查询出cate[i_ca]类的可选的所有题目
        data = opr.query_extra_exercise("category = "+cate[i_ca][0]+" and chapter in "+"("+chstr+")")
        print(data)
        # 将查询到的题目按【难度】进行分类，暂存入ca_diff二维列表（存有与高、中、低难度对应的三个列表）
        for i_data in range(data.shape[0]):
            for j in range(3):
                if data.at[i_data,"difficulty"]==difficulty[j]:
                    ca_diff[j].append(data.at[i_data,"ExerciseCode"])
        print(ca_diff)
        # 在分类好的可选题目中随机抽取【指定数目】的题目
        catenum = cate[i_ca][1]
        highnum = int(catenum*diff[0])
        lownum = int(catenum*diff[1])
        final.extend(random.sample(ca_diff[0],highnum))
        final.extend(random.sample(ca_diff[1],catenum-highnum-lownum))
        final.extend(random.sample(ca_diff[2],lownum))
        print(final)
    print(final)
    #def add_paper(self, chapter, difficulty_high, difficulty_middle, difficulty_low)
    #def test_exercise(self, test_id, exercise_id)
    print(chstr,float(diff[0]),float(1-diff[0]-diff[1]),float(diff[1]))
    NewPaperId = opr.add_paper("'"+chstr+"'",float(diff[0]),float(1-diff[0]-diff[1]),float(diff[1]))
    print(NewPaperId)
    for ExcerciseCode in final:
        opr.test_exercise(NewPaperId, ExcerciseCode)

def set_pdctview(win):
    category = opr.statistic_exercise("category")
    category_list = Df2Ls(category)
    chapter = opr.statistic_exercise("chapter")
    chapter_list = Df2Ls(chapter)

    win.set_pdctview(category_list,chapter_list)

def main():
    app = QApplication(sys.argv)
    datalist = statistic_info()
    print(datalist)
    mainwin = mainWindow(datalist)
    mainwin.show()

    mainwin.addui.submit.clicked.connect(partial(add, mainwin.addui))
    mainwin.schui.schbtn.clicked.connect(partial(sreach, mainwin.schui))
    mainwin.schui.delbtn.clicked.connect(partial(remove_item, mainwin.schui.outputlist))
    mainwin.disbtn.clicked.connect(partial(updata_info,mainwin))
    mainwin.pdctbtn.clicked.connect(partial(set_pdctview,mainwin))
    mainwin.pdctui.pushButton.clicked.connect(partial(create_paper,mainwin.pdctui))

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
