import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.header import Header     

def mail(html_str,rcptto=None):
    # 发件人地址，通过控制台创建的发件人地址
    username = 'YourServerMailAddr'
    # 发件人密码，通过控制台创建的发件人密码
    password = 'ABCDEFGHIJK'
    # 自定义的回复地址
    replyto = username
    # 收件人地址或是地址列表，支持多个收件人，最多60个
    if rcptto is None:
        rcptto = ['YourReceiveMailAddr']
        
    # 构建alternative结构
    msg = MIMEMultipart('alternative')
    
    msg['Subject'] = Header(html_str)
    msg['From'] = '%s <%s>' % (Header(''), username)
    msg['To'] = Header(','.join(rcptto))
    msg['Reply-to'] = replyto
    msg['Message-id'] = email.utils.make_msgid()
    msg['Date'] = email.utils.formatdate()
    texthtml = MIMEText(html_str, _subtype='html', _charset='UTF-8')
    msg.attach(texthtml)
    
    s = time.strftime('%m-%d %H:%M ')
    try:
        client = smtplib.SMTP_SSL('smtp.163.com',465)
        #python 2.7以上版本，若需要使用SSL，可以这样创建client
        #client = smtplib.SMTP_SSL()
        #SMTP普通端口为25或80
        #client.connect('smtp.163.com')
        #client.ehlo()
        #client.starttls()
        #开启DEBUG模式
        client.set_debuglevel(0)
        client.login(username, password)
        #发件人和认证地址必须一致
        #备注：若想取到DATA命令返回值,可参考smtplib的sendmaili封装方法:
        #使用SMTP.mail/SMTP.rcpt/SMTP.data方法
        client.sendmail(username, rcptto, msg.as_string())
        client.quit()
        print(s+'邮件发送成功！')
    except smtplib.SMTPConnectError as e:
        print(s+'邮件发送失败，连接失败:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPAuthenticationError as e:
        print(s+'邮件发送失败，认证错误:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPSenderRefused as e:
        print(s+'邮件发送失败，发件人被拒绝:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPRecipientsRefused as e:
        print(s+'邮件发送失败，收件人被拒绝:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPDataError as e:
        print(s+'邮件发送失败，数据接收拒绝:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPException as e:
        print(s+'邮件发送失败, ', str(e))
    except Exception as e:
        print(s+'邮件发送异常, ', str(e))
