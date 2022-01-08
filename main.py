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
POINT = 0
TEST_ID = 0

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
    if ui.diffbtn.isChecked():
        diff = "'"+value+"'"
        d = opr.query_exercise("difficulty="+diff)
        print(d)
    #print(d[["ExerciseCode","topic","answer"]])

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
                opr.delete_exercise(code)
                break

def Df2Ls(data):
    datalist = []
    for i in range(len(data)):
        datalist.append([str(data.iat[i,0]),int(data.iat[i,1])])
    return datalist

def statistic_info():
    global opr
    datalist = []
    data = opr.statistic_exercise("difficulty")
    #print(data)
    datalist.append(Df2Ls(data))
    #print(datalist)
    data = opr.statistic_exercise("category")
    #print(data)
    datalist.append(Df2Ls(data))
    #print(datalist)
    data = opr.statistic_exercise("chapter")
    #print(data)
    datalist.append(Df2Ls(data))
    #print(datalist)
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
        ca_num.append(int(ui.xzpoint.text()))
        cate.append(ca_num)

    if ui.tk.isChecked():
        ca_num = []
        ca_num.append("'填空'")
        ca_num.append(int(ui.tknum.text()))
        ca_num.append(int(ui.tkpoint.text()))
        cate.append(ca_num)
    if ui.pd.isChecked():
        ca_num = []
        ca_num.append("'判断'")
        ca_num.append(int(ui.pdnum.text()))
        ca_num.append(int(ui.pdpoint.text()))
        cate.append(ca_num)
    if ui.mc.isChecked():
        ca_num = []
        ca_num.append("'名词解释'")
        ca_num.append(int(ui.mcnum.text()))
        ca_num.append(int(ui.mcpoint.text()))
        cate.append(ca_num)
    if ui.wd.isChecked():
        ca_num = []
        ca_num.append("'问答'")
        ca_num.append(int(ui.wdnum.text()))
        ca_num.append(int(ui.wdpoint.text()))
        cate.append(ca_num)
    if ui.js.isChecked():
        ca_num = []
        ca_num.append("'计算'")
        ca_num.append(int(ui.jsnum.text()))
        ca_num.append(int(ui.jspoint.text()))
        cate.append(ca_num)
    if ui.sf.isChecked():
        ca_num = []
        ca_num.append("'算法'")
        ca_num.append(int(ui.sfnum.text()))
        ca_num.append(int(ui.sfpoint.text()))
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
        onecate = []
        onecate.extend(random.sample(ca_diff[0],highnum))
        onecate.extend(random.sample(ca_diff[1],catenum-highnum-lownum))
        onecate.extend(random.sample(ca_diff[2],lownum))
        final.append(onecate)
        print(final)
    print(final)
    #def add_paper(self, chapter, difficulty_high, difficulty_middle, difficulty_low)
    #def test_exercise(self, test_id, exercise_id)
    print(chstr,float(diff[0]),float(1-diff[0]-diff[1]),float(diff[1]))
    NewPaperId = opr.add_paper("'"+chstr+"'",float(diff[0]),float(1-diff[0]-diff[1]),float(diff[1]))
    print(NewPaperId)
    for i in range(len(final)):
        for ExcerciseCode in final[i]:
            opr.test_exercise(NewPaperId, ExcerciseCode,cate[i][2])

def set_pdctview(win):
    category = opr.statistic_exercise("category")
    category_list = Df2Ls(category)
    chapter = opr.statistic_exercise("chapter")
    chapter_list = Df2Ls(chapter)

    win.set_pdctview(category_list,chapter_list)


def manage_paper(ui):
    global opr

    ui.mngwid.show()
    ui.editwid.hide()
    ui.paperlist.clear()

    paper_data = opr.query_paper("all")
    print(paper_data)

    for i in range(paper_data.shape[0]):
        ui.paperlist.addItem("试卷编号 %s \t高难度题占比:%s\t低难度题占比:%s\t\t范围:%s"%(str(paper_data.at[i,"TestCode"]),str(paper_data.at[i,"difficulty_high"]),str(paper_data.at[i,"difficulty_low"]),str(paper_data.at[i,"chapter"])))


def remove_paper(list):
    global opr
    if list.count() > 0:
        for i in range(list.count()):
            item = list.item(i)
            if item.isSelected():
                code = int(str(list.item(i).text()).split()[1])

                print("code:",code)

                list.removeItemWidget(list.takeItem(i))
                # 此处+对话框
                global opr
                opr.delete_paper(code)
                break

def check_paper(ui):
    global opr,TEST_ID
    list = ui.paperlist
    if list.count() > 0:
        for i in range(list.count()):
            item = list.item(i)
            # 选择被选中的试卷
            if item.isSelected():
                codestr = str(list.item(i).text()).split()[1]
                code = int(codestr)
                TEST_ID = code
                print("code:",code)

                ui.mngwid.hide()
                ui.editwid.show()
                ui.paperlist.clear()
                ques_data = opr.query_exercise_from_paper(code)
                ques_data = ques_data.sort_values(by="number",ascending=True)
                ques_data = ques_data.reset_index(drop = True)
                print(ques_data)
                point = ques_data.at[i,"point"]
                for i in range(ques_data.shape[0]):
                    excercisecode = ques_data.at[i,"ExerciseCode"]
                    detail_data = opr.query_exercise("exercise_base_info.ExerciseCode="+str(excercisecode))
                    print(detail_data)
                    print(str(ques_data.at[i,"ExerciseCode"])+' '+str(ques_data.at[i,"number"])+' '+str(point))
                    ui.paperlist.addItem("编号 "+str(excercisecode)+'\t'+"试卷中序号 "+str(ques_data.at[i,"number"])+'\t'+"分值 "+str(ques_data.at[i,"point"])+'\t'+str(detail_data.at[0,"topic"])+"\t"+str(detail_data.at[0,"answer"]))

                break


def edit_ques(win):
    list = win.mngui.paperlist
    code = 0
    global POINT
    if list.count() > 0:
        for i in range(list.count()):
            item = list.item(i)
            if item.isSelected():
                code = int(str(list.item(i).text()).split()[1])
                POINT = float(str(list.item(i).text()).split()[5])
                break
    print("code",code)
    detail_data = opr.query_exercise("exercise_base_info.ExerciseCode="+str(code))
    print(detail_data)
    win.showchg()
    ui = win.chgui
    ui.codelabel.setText("试题详情-题号："+str(code))
    ui.point.setText(str(POINT))

    cate = detail_data.at[0,"category"]
    diff = detail_data.at[0,"difficulty"]
    
    ui.para1.setValue(detail_data.at[0,"chapter"])
    ui.para2.setValue(detail_data.at[0,"part"])
    ui.ctt_1.setPlainText(detail_data.at[0,"topic"])
    ui.ctt_2.setPlainText(detail_data.at[0,"answer"])
    print(cate)
    if cate == '选择':
        ui.cata_1.setChecked(True)
    elif cate == '判断':
        ui.cata_2.setChecked(True)
    elif cate == '填空':
        ui.cata_3.setChecked(True)
    elif cate == '名词解释':
        ui.cata_4.setChecked(True)
    elif cate == '问答':
        ui.cata_5.setChecked(True)
    elif cate == '算法':
        ui.cata_6.setChecked(True)
    elif cate == '计算':
        ui.cata_7.setChecked(True)

    if diff == "低":
        ui.diff_1.setChecked(True)
    elif diff == "高":
        ui.diff_2.setChecked(True)
    elif diff == "中":
        ui.diff_3.setChecked(True)


def save_edit(ui):

    global opr
    global POINT,TEST_ID

    code = int(ui.codelabel.text()[8:])
    detail_data = opr.query_exercise("exercise_base_info.ExerciseCode="+str(code))
    print(detail_data)
    or_cate = "'"+detail_data.at[0,"category"]+"'"
    or_diff = "'"+detail_data.at[0,"difficulty"]+"'"

    or_chap=detail_data.at[0,"chapter"]
    or_sec=detail_data.at[0,"part"]
    or_ques="'"+detail_data.at[0,"topic"]+"'"
    or_ans="'"+detail_data.at[0,"answer"]+"'"
    or_point = POINT
    point = float(ui.point.text())
    print("test,ques,point",TEST_ID,code,POINT)
    if or_point != point:
        opr.update_point(TEST_ID,code,point)
    print("or_point",or_point)

    chap = int(ui.para1.text())
    sec = int(ui.para2.text())
    cate = ''
    diff = ''
    if ui.cata_1.isChecked():
        cate = "'选择'"
    if ui.cata_2.isChecked():
        cate = "'判断'"
    if ui.cata_3.isChecked():
        cate = "'填空'"
    if ui.cata_4.isChecked():
        cate = "'名词解释'"
    if ui.cata_5.isChecked():
        cate = "'问答'"
    if ui.cata_6.isChecked():
        cate = "'算法'"
    if ui.cata_7.isChecked():
        cate = "'计算'"
    if ui.diff_1.isChecked():
        diff = "'低'"
    if ui.diff_2.isChecked():
        diff = "'高'"
    if ui.diff_3.isChecked():
        diff = "'中'"

    ques = "'" + ui.ctt_1.toPlainText() + "'"
    ans = "'" + ui.ctt_2.toPlainText() + "'"
    print("章：", chap, "节:", sec, "类别:", cate, "难度:", diff)
    print("题目", ques, "答案", ans)
    print("章：", or_chap, "节:", or_sec, "类别:", or_cate, "难度:", or_diff)
    print("题目", or_ques, "答案", or_ans)
    #ques, "null", ans, "null", category, chap, sec, diff
    clms=[]
    val=[]

    if or_chap != chap:
        clms,val =[],[]
        clms.append("chapter")
        val.append(str(chap))
        opr.update_exercise(code,clms,val)
    if or_sec != sec:
        clms,val =[],[]
        clms.append("part")
        val.append(str(sec))
        opr.update_exercise(code,clms,val)
    if or_cate != cate:
        clms,val =[],[]
        clms.append("category")
        val.append(cate)
        opr.update_exercise(code,clms,val)
    if or_diff != diff:
        clms,val =[],[]
        clms.append("difficulty")
        val.append(diff)
        opr.update_exercise(code,clms,val)
    if or_ques != ques:
        clms,val =[],[]
        clms.append("topic")
        val.append(ques)
        opr.update_exercise(code,clms,val)
    if or_ans != ans:
        clms,val =[],[]
        clms.append("answer")
        val.append(ans)
        opr.update_exercise(code,clms,val)


    detail_data = opr.query_exercise("exercise_base_info.ExerciseCode="+str(code))
    print(detail_data)
    '''
    if or_chap != chap:
        clms.append("chapter")
        val.append(str(chap))
    if or_sec != sec:
        clms.append("part")
        val.append(str(sec))
    if or_cate != cate:
        clms.append("category")
        val.append(cate)
    if or_diff != diff:
        clms.append("difficulty")
        val.append(diff)
    if or_ques != ques:
        clms.append("topic")
        val.append(ques)
    if or_ans != ans:
        clms.append("answer")
        val.append(ans)
    print(clms,val)
    opr.update_exercise(code,clms,val)
    detail_data = opr.query_exercise("exercise_base_info.ExerciseCode="+str(code))
    print(detail_data)
    '''

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
    mainwin.pdctui.crtbtn.clicked.connect(partial(create_paper,mainwin.pdctui))
    mainwin.mngbtn.clicked.connect(partial(manage_paper,mainwin.mngui))
    mainwin.mngui.delbtn.clicked.connect(partial(remove_paper,mainwin.mngui.paperlist))
    mainwin.mngui.chkbtn.clicked.connect(partial(check_paper,mainwin.mngui))
    mainwin.mngui.backbtn.clicked.connect(partial(manage_paper,mainwin.mngui))
    mainwin.mngui.chgbtn.clicked.connect(partial(edit_ques,mainwin))
    mainwin.chgui.submit.clicked.connect(partial(save_edit,mainwin.chgui))

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
