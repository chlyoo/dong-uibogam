import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

from urllib import parse

from instance import *

options = Options()
options.headless = False
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
browser.get("https://lib.jeonnam.go.kr/bbs/login.php")

browser.find_element_by_name('mb_id').send_keys(아이디)
browser.find_element_by_name('mb_password').send_keys(비밀번호)
browser.find_element_by_css_selector(".login form button").click()
browser.get("https://lib.jeonnam.go.kr/bbs/board.php?bo_table=subscription_service#")
browser.execute_script("krpia_open(3516)")
browser.close()
browser.switch_to.window(browser.window_handles[-1])
browser.implicitly_wait(3)
browser.get("https://www.krpia.co.kr/product/main?plctId=PLCT00004558#none")
browser.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[1]/div/div/div[3]/div[2]/a").click()

#browser.get("https://www.krpia.co.kr/viewer?plctId=PLCT00004558&tabNodeId=NODE03923082")

#browser.implicitly_wait(3)



# 게시판 글 읽기

#browser.get(f"https://hisnet.handong.edu/cis/write.php?Board=KYOM_EXTRA&CateCode=2959&dflag=")
#browser#browser.get(f"https://hisnet.handong.edu/cis/list.php?Board=KYOM_EXTRA&CateCode=2959")


#WebElement formElement = driver.findElement(By.name("form_w"));
#List<WebElement> allFormChildElements = formElement.findElements(By.xpath("*"));
#browser.find_element_by_class_name('content')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#element = browser.find_element_by_name('content')
#WebDriverWait(browser, 5).until(
#    EC.presence_of_element_located((By.ID, "content"))
#)  # Wait until the `text_to_score` element appear (up to 5 seconds)
#browser.execute_script('oEditors.getById["content"].setIR("11")')
#browser.find_element_by_name('form_w').submit()
#browser.implicitly_wait(3)
#browser.switch_to_frame('MyIFrame').switch_to_alert().accept();

