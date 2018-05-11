#/usr/
#coding=utf-8

import mysql.connector
import configparser
from Interface_Auto.conf.read_path import Db_path

class Mysql_Read:
    def mysql_read(self,sql):
        #读取mysql配置信息
        cf=configparser.ConfigParser()
        cf.read(Db_path)
        mysql_config=eval(cf.get("MYSQL_CONFIG","mysql_config"))
        #登录数据库
        connection=mysql.connector.connect(**mysql_config)
        #设置游标
        cursor=connection.cursor()
        #写sql语句
        #sql="select * from member m where m.MobilePhone='18612340055' "
        #执行sql
        cursor.execute(sql)
        #提交
        #cursor.execute("commit")
        result=cursor.fetchone()
        #result=cursor.fetchall()
        #print(result)
        #关闭游标
        cursor.close()
        #关闭连接
        connection.close()
        return result

#Mysql_Read().mysql_read("select * from member m where m.MobilePhone='186123400'")