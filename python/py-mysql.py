#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","001325","company",charset="utf8" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL 查询
cursor.execute("SELECT 企业名称 from 企业联系表 where 联系人 = 'None' ")

# 使用 fetchone() 方法获取单条数据
data1 = cursor.fetchall()

# print (data1)
# print ("公司名字：%s" % data1)'
for i in range(len(data1)):
    print (data1[i]) 
    sql1 = "select 联系人 from 企业信息表 where 企业名称 = '%s'" % data1[i]
    print (sql1)
    cursor.execute(sql1)
    data2 = cursor.fetchone()
    # print ("联系人：%s" % data2)
    sql2 = "update 企业联系表 set 联系人 = '%s'" % data2 
    sql2 += " where 企业名称 = '%s'" % data1[i]
    print (sql2)
    cursor.execute(sql2)
    db.commit()

# 关闭数据库连接
db.close()

