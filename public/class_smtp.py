#coding=utf-8

'''
参数说明： 
    1. subject：邮件主题
    2. content：邮件正文
    3. filepath：附件的地址
    4. sender:发件人
    5. receivers：收件人地址, 输入格式为"收件人1,收件人2" 如："xxxx@qq.com,xxxx@163.com"
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication




class Send_Email:
    def __init__(self, subject, content,sender,pwd,receivers,smtp_server,port_no):
        self.sender = sender
        self.receivers =  receivers.split(",")
        self.pwd =  pwd
        self.subject = subject
        self.content = content
        self.smtp_server=smtp_server
        self.port_no=port_no
        self.files_path=[]

    def Add_Attach(self,filepath):
        self.files_path.append(filepath)

    def send_email(self):
        msgRoot = MIMEMultipart()
        msgRoot['Subject'] = self.subject
        msgRoot['From'] = self.sender
        msgRoot['To'] = ','.join(self.receivers) #群发邮件

        file_msg = MIMEText(self.content)
        msgRoot.attach(file_msg)

        ##添加附件部分，将filepath列表中的文件循环处理
        for path in self.files_path:
            file_name = path.split("\\")[-1] #取文件名
            file_msg = MIMEApplication(open(path,'rb').read(), 'utf-8')
            file_msg.add_header('Content-Disposition', 'attachment', filename=('gb2312','',file_name))
            msgRoot.attach(file_msg)
        #发送邮件
        try:
            s = smtplib.SMTP()
            s.connect(self.smtp_server,self.port_no)
            s.login(self.sender, self.pwd)
            s.sendmail(self.sender, self.receivers, msgRoot.as_string())
            print ("邮件发送成功")
        except smtplib.SMTPException as e:
            print("Error, 发送失败")
            raise e
        finally:
            s.quit()

if __name__=="__main__":
    subject="SMTP封装邮件"
    content="SMTP封装模块发送测试"
    Send_email=Send_Email(subject,content,'15757177080@163.com',"wy123456","451786285@qq.com,387954307@qq.com","smtp.163.com","25")
    Send_email.Add_Attach('D:\pycharm\study\class_smtp\class_smtp.py')
    Send_email.send_email()
