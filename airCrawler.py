from email.header import Header
from email.mime.text import MIMEText
from time import sleep
from selenium import webdriver
import smtplib


def send_email(text):
    #qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    #用户名
    mail_user="774621331@qq.com"
    # 授权码
    mail_pass = "alphjxhbpiyibcjg"
    sender = '774621331@qq.com'
    receivers = ['774621331@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header("携程机票爬虫", 'utf-8')   # 发送者
    message['To'] = Header("Lynn", 'utf-8')        # 接收者

    subject = '携程机票爬虫结果'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件", str(e))


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=r"D:\产品\爬虫\chromedriver.exe")

    sleep(2)
    start = "2019-08-11"
    end = "2019-08-17"
    adult = 1
    child = 0
    infant = 0
    url = "https://flights.ctrip.com/international/search/round-szx-tyo?depdate=" + start + "_" + end + "&cabin=y_s&adult=" \
          + str(adult) + "&child=" + str(child) + "&infant=" + str(infant)
    print(url)
    driver.get(url)
    sort_button = driver.find_element_by_class_name('sort-item.ticket-price')
    sort_button.click()
    sleep(10)
    flights = driver.find_element_by_class_name("flight-list.root-flights")
    flight_items = flights.find_elements_by_class_name("flight-item")
    flights_info = ""
    for flight in flight_items:
        airline = flight.find_element_by_class_name("airline-name")
        flights_info = flights_info + ("航班: %s" % airline.text) + "\n"
        print("航班: %s" % airline.text)
        planes = flight.find_element_by_class_name("plane")
        print("机型: ")
        print(planes.text)
        flights_info = flights_info + "机型: " + "\n"
        flights_info = flights_info + planes.text + "\n"

        flight_detail = flight.find_element_by_class_name("flight-detail")
        print("航班详情: ")
        flight_detail = flight_detail.text.replace("\n", " ")
        print(flight_detail)
        flights_info = flights_info + "航班详情: " + "\n"
        flights_info = flights_info + flight_detail + "\n"

        flight_time = flight.find_element_by_class_name("flight-consume")
        print("飞行时间: %s" % flight_time.text)
        flights_info = flights_info + ("飞行时间: %s" % flight_time.text) + "\n"

        flight_price = flight.find_element_by_class_name("flight-price")
        print("机票价格: %s" % flight_price.text)
        flights_info = flights_info + ("机票价格: %s" % flight_price.text) + "\n"
        flights_info += "\n"
        print("\n")

    send_email(flights_info)

