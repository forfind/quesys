# -*- coding=utf-8 -*-
import pymysql
import sys


# 读取图片文件
# blob最大只能存65K的文件

def main():
    # fp = open("test.jpg",'rb',encoding='utf-8')
    fp = open(r"D:\Doc\Picture\test.jpg", 'rb')
    img = fp.read()
    fp.close()
    # 创建连接
    conn = pymysql.connect(host='localhost', user="zzmdb", passwd="zzm666", db="exercise")
    # 创建游标
    cursor = conn.cursor()

    # 注意使用Binary()函数来指定存储的是二进制
    # cursor.execute("INSERT INTO demo_pic_repo SET touxiang_data= %s" % pymysql.Binary(img))

    sql = "INSERT INTO exercise_base_info (topic_picture, answer_picture) VALUES (%s,%s)"
    cursor.execute(sql, [img, img])
    # 提交，不然无法保存新建或者修改的数据
    conn.commit()

    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()


if __name__ == '__main__':
    main()
