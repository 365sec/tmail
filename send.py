# coding:utf8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
# 第三方 SMTP 服务
# mail_host="smtp.163.com" #设置服务器
# mail_user="18962254818@163.com" #用户名
# mail_pass="qwe123456" #口令
# sender = '18962254818@163.com'
# receivers = ["1040641785@qq.com"] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# message = MIMEText('Python SMTP 邮件发送测试', 'plain', 'utf-8')
# message['From'] = Header("From测试",'utf-8')
# message['To'] = Header("To测试", 'utf-8')
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
# try:
#     smtpObj = smtplib.SMTP()
#     smtpObj.connect(mail_host, 25) # 25 为 SMTP 端口号
#     smtpObj.login(mail_user,mail_pass)
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print "邮件发送成功"
# except Exception as e:
#     print str(e)

def send_mail(sub,content):
    mailto_list=['1040641785@qq.com'] #收件人(列表)
    mail_host="smtp.163.com" #使用的邮箱的smtp服务器地址，这里是163的smtp地址
    mail_user="18962254818@163.com" #用户名
    mail_pass="qwe123456" #密码  网易邮箱需要使用授权码
    mail_postfix="163.com" #邮箱的后缀，网易就是163.com
    me="<18962254818@163.com>"
    # 创建一个带附件的实例
    msg = MIMEMultipart()
    # 邮件正文内容
    msg.attach(MIMEText(content,_subtype='plain'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open('report-19-02-13 16_45_1550047554.docx', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="report-19-02-13 16_45_1550047554.docx"'
    msg.attach(att1)

    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(mailto_list) #将收件人列表以‘；’分隔
    try:
        server = smtplib.SMTP()
        server.connect(mail_host) #连接服务器
        server.login(mail_user,mail_pass) #登录操作
        server.sendmail(me, mailto_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print str(e)
        return False

for i in range(1): #发送1封，上面的列表是几个人，这个就填几
    if send_mail("Python SMTP 邮件发送测试","Python SMTP 邮件发送测试"): #邮件主题和邮件内容 #这是最好写点中文，如果随便写，可能会被网易当做垃圾邮件退信
        print( "done!" )
    else:
        print( "failed!" )
