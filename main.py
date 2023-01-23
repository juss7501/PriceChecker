import requests
import smtplib
from bs4 import BeautifulSoup
from email.message import EmailMessage
import time

send_mail = True
# function to check price
def check_price():
    target_price = 1000
    url = 'https://www.amazon.de/Samsung-Android-Smartphone-Herstellergarantie-Exklusiv/dp/B09QH2G7BS?ref_=Oct_DLandingS_D_a837534c_60'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    price_element = soup.find_all("span", class_="a-price-whole")
    if price_element:
        price = price_element[0].get_text()
        price = int(price.replace(".", "").replace(",", ""))
        if price < target_price:
            send_notification(price)
            send_mail = False
        print("The current price of the Samsung S22 is: " + str(price))
    else:
        price = 0
        print("Price element not found")
    return price
# function to send notification


def send_notification(x):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("juss7501@gmail.com", "bunbczmapovokzvy")
    message = EmailMessage()
    message.set_content( "Price dropped to " + str(x))
    server.send_message(message,"juss7501@gmail.com","juss7501@gmail.com")
    # server.sendmail("juss7501@gmail.com", "justus.melzer@yahoo.com", message)
    server.quit()
    print("Notification sent")

# main loop

while send_mail:
    check_price()
    time.sleep(60)
