import requests
import time
import smtplib
from email.mime.text import MIMEText

def visit_url():
    url = "http://www.aikys.top/ys/temp/index.php"
    url_1 = "http://www.aikys.top/ys/temp/update_m3u.php"
    try:
        response = requests.get(url)
        response.raise_for_status()
        time.sleep(15)  # 停留15秒钟
        return f"Visited URL successfully, Status Code: {response.status_code}"
        response_1 = requests.get(url)
        response_1.raise_for_status()
        time.sleep(15)  # 停留15秒钟
        return f"Visited URL successfully, Status Code: {response_1.status_code}"
    except requests.RequestException as e:
        return f"Failed to visit URL: {str(e)}"

def send_email():
    # 邮件服务器地址和端口号
    smtp_server = 'smtp.qq.com'
    smtp_port = 465

    # 发件人邮箱和密码
    sender_email = '1574412465@qq.com'
    sender_password = 'ptblprejncuxfjia'

    # 收件人邮箱
    receiver_email = '3409056090@qq.com'

    # 邮件内容
    text = text
    message = MIMEText('text', 'plain', 'utf-8')
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = '每天9:30定时推送'

    try:
        # 创建SMTP对象并连接到服务器
        smtp_obj = smtplib.SMTP_SSL(smtp_server, smtp_port)
        smtp_obj.login(sender_email, sender_password)

        # 发送邮件
        smtp_obj.sendmail(sender_email, receiver_email, message.as_string())
        print('邮件发送成功')

    except Exception as e:
        print('邮件发送失败:', str(e))

    finally:
        # 关闭SMTP对象的连接
        smtp_obj.quit()
   
if __name__ == "__main__":
    result = visit_url()
    print(result)
    text = "推送更新成功\n" + response.status_code + "(如果为200则表示txt更新成功)\n" + response_1.status_code + "(如果为200则表示m3u更新成功)"
    send_email(text)
    print(f"推送成功!")
