#coding=utf-8
import configparser
import logging
import time

from Interface_Auto.conf.read_path import Config_path


class MyLogger:
    def __init__(self,logger_name,log_path):
        cf = configparser.RawConfigParser()
        cf.read(Config_path,encoding='utf-8')
        self.logger_name=logger_name
        self.logger_level=cf["LOG"]["logger_level"]
        self.handler_level=cf["LOG"]["handler_level"]
        self.formatter=cf["LOG"]["formatter"]
        self.log_path=log_path

    def mylog(self):
        logger=logging.Logger(self.logger_name,self.logger_level)
        formatter = logging.Formatter(self.formatter)

        sh=logging.StreamHandler()
        sh.setLevel(self.handler_level) #设置过滤输出等级
        sh.setFormatter(formatter)      #设置输出格式

        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        new_log_path = self.log_path + "/Api_Autotest_log_{0}.log".format(now[0:10])
        fh=logging.FileHandler(new_log_path,'a',encoding='utf-8')
        fh.setLevel(self.handler_level) #设置过滤输出等级
        fh.setFormatter(formatter)      #设置输出格式

        logger.addHandler(sh)
        logger.addHandler(fh)

        return logger

if __name__=='__main__':
    mylogger=MyLogger("mylogger","D:\pycharm\study\Interface_Auto\logs\log.txt")
    mylogger.mylog().debug('01级别')
    mylogger.mylog().info('02级别'+'8')
    mylogger.mylog().warning('03级别')
    mylogger.mylog().error('04级别')
    mylogger.mylog().critical('05级别')



