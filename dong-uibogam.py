from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

from urllib import parse

from instance import *
import json
import os

#hwp module
import win32com.client as win32

hwp = win32.Dispatch("HWPFrame.HwpObject")
hwp.RegisterModule("FilePathCheckDLL", "SecurityModule")
hwp.Open('C:\\dong-uibogam\\bogam.hwp', "HWP", None)

#field_list =[i for i in hwp.GetFieldList(0,0).split('\x02')]
field_list=['title','content']


startnode=3923083 
endnode=3928498
"""
#hwp initialize
hwp.Run('SelectAll')
hwp.Run('Copy')
hwp.MovePos(3,None,None)
for i in range(startnode,endnode):
	hwp.Run('Paste')
	hwp.MovePos(3,None,None)
"""

options = Options()
options.headless = True #False
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
browser.get("https://lib.jeonnam.go.kr/bbs/login.php")

browser.find_element_by_name('mb_id').send_keys(아이디)
browser.find_element_by_name('mb_password').send_keys(비밀번호)
browser.find_element_by_css_selector(".login form button").click()
browser.get("https://lib.jeonnam.go.kr/bbs/board.php?bo_table=subscription_service#")
browser.execute_script("krpia_open(3516)")
browser.close()
browser.switch_to.window(browser.window_handles[-1])
browser.get("https://www.krpia.co.kr/product/main?plctId=PLCT00004558#none")
browser.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[1]/div/div/div[3]/div[2]/a").click()
browser.switch_to.window(browser.window_handles[-1])


#browser.window_handles
#browser.get("https://www.krpia.co.kr/viewer?plctId=PLCT00004558&tabNodeId=NODE03923082")

#field_list =[i for i in hwp.GetFieldList(0,0).split('\x02')]
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
for i in range(startnode,endnode+1):
    
    translist={}
    WebDriverWait(browser, 15).until(
    	EC.presence_of_element_located((By.CLASS_NAME, "content"))
    	)
    translist['content']=browser.find_element_by_class_name("content").text 
    translist['title']=browser.find_element_by_css_selector("a#titleNow.on").text
    
    for field in field_list:
    	hwp.PutFieldText(f'{field}{{{{{i-startnode}}}}}',translist[str(field)]) 

    WebDriverWait(browser, 30).until(
    	EC.presence_of_element_located((By.ID, "titleNext"))
    	)
    browser.find_element_by_id("titleNext").click()
    hwp.Save(False)



"""
import http

import urllib.request

from urllib.parse import quote

import json
browser.switch_to.window(browser.window_handles[0])
for i in range(startnode,endnode+1):
	url="https://www.krpia.co.kr/viewer/medaBody?viewModeType=185002%2C&node-id=NODE0" + str(i)+"&plctId=PLCT00004558"
	browser.get(url)
	request=urllib.request.Request(url)
	response=urllib.request.urlopen(request)
	rescode = response.getcode()
	response_body= response.read()
	parse = json.loads(response_body)
	transList=parse['transList'][0]
	translist={}
	translist['content']=transList['body']
	translist['title']=transList['filePath']
	for field in field_list:
		hwp.PutFieldText(f'{field}{{{{{i-startnode}}}}}',translist[str(field)]) 
	hwp.Save(False)

	 #기존 json
    #
    