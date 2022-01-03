from Ui_main import *
from functools import partial
from database_operate import *
def test(ui):
    cata = ''
    print("succ")
    cata = "'" + ui.ctt_1.toPlainText() + "'"

    print(cata)


def add(ui):
    chap = int(ui.para1.text())
    sec = int(ui.para2.text())
    cata = ''
    diff = ''
    if ui.cata_1.isChecked():
        cata = "'选择'"
    if ui.cata_2.isChecked():
        cata = "'判断'"
    if ui.cata_3.isChecked():
        cata = "'填空'"
    if ui.cata_4.isChecked():
        cata = "'名词解释'"
    if ui.cata_5.isChecked():
        cata = "'问答'"
    if ui.cata_6.isChecked():
        cata = "'算法'"
    if ui.cata_7.isChecked():
        cata = "'计算'"
    if ui.diff_1.isChecked():
        diff = "'低'"
    if ui.diff_2.isChecked():
        diff = "'高'"
    if ui.diff_3.isChecked():
        diff = "'中'"

    ques = "'" + ui.ctt_1.toPlainText() + "'"
    ans = "'" + ui.ctt_2.toPlainText() + "'"
    ui.ctt_1.clear()
    ui.ctt_2.clear()
    print("章：", chap, "节:", sec, "类别:", cata, "难度:", diff)
    print("题目", ques, "答案", ans)

    opr = DatabaseOperate("104.168.172.47", "forfind", "000000", "exercise")
    pd.set_option('display.max_columns', None,
                  'display.max_rows', None,
                  'display.max_colwidth', None,
                  'display.width', 100,
                  'expand_frame_repr', False)
    print(cata)
    opr.add(ques, "null", ans, "null", cata, chap, sec, diff)
    d = opr.inquire("category="+cata)
    print(d)


def sreach(ui):
    opr = DatabaseOperate("104.168.172.47", "forfind", "000000", "exercise")
    pd.set_option('display.max_columns', None,
              'display.max_rows', None,
              'display.max_colwidth', None,
              'display.width', 100,
              'expand_frame_repr', False)
    value = ui.inputtxt.toPlainText()
    if ui.keybtn.isChecked():
        by = 0
    if ui.codebtn.isChecked():
        d = opr.inquire("exercise_base_info.ExerciseCode="+value)
        print(d)
    if ui.catabtn.isChecked():
        cata = "'"+value+"'"
        d = opr.inquire("category="+cata)
        print(d)
        ui.outputtxt.set


def main():
    app = QApplication(sys.argv)
    mainwin = mainWindow()
    mainwin.show()
    mainwin.addui.submit.clicked.connect(partial(add, mainwin.addui))
    mainwin.schui.schbtn.clicked.connect(partial(sreach, mainwin.schui))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
