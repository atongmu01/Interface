#coding=utf-8
import unittest
import time
import os
import configparser
from Interface_Auto.public.class_smtp import Send_Email
from Interface_Auto.conf.read_path import Config_path
from Interface_Auto.Interface_register.Register_Request_Test import Register_Request_test
from Interface_Auto.Interface_recharge.Recharge_Request_Test import Recharge_Request_test
from Interface_Auto.public import HTMLTestRunnerNew


suite=unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Register_Request_test))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Recharge_Request_test))
#suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Http_Request_test))
#取当前时间
now=time.strftime('%Y-%m-%d_%H_%M_%S')
path=os.getcwd()
f= open(path+"\\result\\"+'Http_Request_report'+now+'.html','wb')
runner=HTMLTestRunnerNew.HTMLTestRunner(
    stream=f,
    title='接口测试报告',
    description='用例执行情况',
    verbosity = 2,
    tester='小白'
)


if __name__=='__main__':
    runner.run(suite)
    f.close()
    cf=configparser.ConfigParser()
    cf.read(Config_path,encoding="utf-8")
    smtp_server = cf.get("EMAIL", "smtp_server")
    port = cf.get("EMAIL", "port")
    sender = cf.get("EMAIL", "sender")
    pwd = cf.get("EMAIL", "pwd")
    receiver = cf.get("EMAIL", "receiver")
    subject = cf.get("EMAIL", "subject")
    content = cf.get("EMAIL", "content")
    Send_email = Send_Email(subject, content, sender, pwd,receiver,smtp_server,port)
    Send_email.Add_Attach(path+"\\result\\"+'Http_Request_report'+now+'.html')
    Send_email.send_email()
