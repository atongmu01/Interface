#Author: Xqq
import os
import configparser


conf_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
#cf=configparser.RawConfigParser()
#cf.read(os.path.join(conf_path,"file_path.conf"),encoding='utf-8')
#project_path=cf.get("PROJECT_PATH","project_path")
project_path=conf_path


Config_path=os.path.join(project_path,"conf","config.conf") #配置文件路径


Log_path=os.path.join(project_path,"logs") #日志文件路径


Excel_path=os.path.join(project_path,"Test_data","接口测试用例.xlsx") #excel文件路径


Db_path=os.path.join(project_path,"conf","dbconfig.conf") #数据库配置路径