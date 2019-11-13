#!/usr/local/python3
import smtplib

from smtplib import SMTP
HOST="smtp.163.com"  #定义smtp主机
SUBJECT="test email form python"  #定义邮件主题
TO = "younglovesara@gmail.com"   #定义邮件收件人
FROM="eryoung2@163.com"  #定义邮件发件人
text="python is test smtp"   #邮件内容,编码为ASCII范围内的字符或字节字符串，所以不能写中文
BODY = '\r\n'.join((      #组合sendmail方法的邮件主体内容，各段以"\r\n"进行分离
    "From: %s" %"admin",
    "TO: %s" %TO,
    "subject: %s" %SUBJECT,
    "",
    text
))

server = SMTP()   #创建一个smtp对象
server.connect(HOST,'25')  #链接smtp主机
server.login(FROM,"950102WTHDK")  #邮箱账号登陆
server.sendmail(FROM,TO,BODY) #发送邮件
server.quit()  #端口smtp链接