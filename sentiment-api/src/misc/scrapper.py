from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import uuid
from unidecode import unidecode
import time

driver = webdriver.Firefox()
driver.get("https://www.emag.ro/televizor-led-smart-samsung-100-cm-40j5200-full-hd-ue40j5200awxxh/pd/DYLF4YBBM/?path=televizor-led-smart-samsung-100-cm-40j5200-full-hd-ue40j5200awxxh/pd/DYLF4YBBM")
i=0
while(True):
    a = driver.find_elements_by_class_name("product-review-body")
    for rev in a:
        try:
            rev.find_element_by_class_name("rated-5")
            print(len(rev.text.split()))
            if len(rev.text.split())<150:
              f=open("/home/katakonst/disertatie/sent-proj/sentiment-api/src/misc/pos/"+str(uuid.uuid4())+".txt", "w")
              f.write(unidecode(rev.text.lower()))
              f.close()
        except Exception:
           print("err")
        try:
            rev.find_element_by_class_name("rated-1")
            if len(rev.text.split())<150:
              f=open("/home/katakonst/disertatie/sent-proj/sentiment-api/src/misc/neg/"+str(uuid.uuid4())+".txt","w")
              f.write(unidecode(rev.text.lower()))
              f.close()
        except Exception:
            print("err")

        try:
            rev.find_element_by_class_name("rated-2")
            if len(rev.text.split())<150:
              f=open("/home/katakonst/disertatie/sent-proj/sentiment-api/src/misc/neg/"+str(uuid.uuid4())+".txt","w")
              f.write(unidecode(rev.text.lower()))
              f.close()
        except Exception:
            print("err")

        try:
            rev.find_element_by_class_name("rated-3")
            if len(rev.text.split())<150:
              f=open("/home/katakonst/disertatie/sent-proj/sentiment-api/src/misc/neg/"+str(uuid.uuid4())+".txt","w")
              f.write(unidecode(rev.text.lower()))
              f.close()
        except Exception:
            print("err")
    i=i+1
    time.sleep(1)
    but=driver.find_element_by_xpath('//a[@href="'+"#page-"+str(i)+'"]')
    driver.execute_script("arguments[0].click();", but)
