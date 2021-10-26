# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import urllib.request

src = 'https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/s1080x1080/177586869_518332985999757_7907282525816274859_n.jpg?tp=1&_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=RCBDLIXz8RQAX_S8UV9&edm=AP_V10EAAAAA&ccb=7-4&oh=403e2596bb631878555fccca577af202&oe=60AC9BDC&_nc_sid=4f375e'
urllib.request.urlretrieve(src, "captcha.png")
print('save')


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

if os.path.isfile("./chromedriver.exe"):

	driver = webdriver.Chrome("chromedriver.exe", chrome_options=options)
	driver.implicitly_wait(3)
	driver.get("https://www.instagram.com/")
	time.sleep(2)

	assert "Instagram" in driver.title

	driver.find_element_by_name('username').send_keys('hanjuhee9@naver.com')
	elem = driver.find_element_by_name('password')
	elem.send_keys('100tktlqtkqlalf') #Test용 계정
	elem.submit()

	time.sleep(5)

	excep = driver.find_element_by_class_name('cmbtv')
	print(excep)
	if excep is not None:
		excep.click()

	excep = driver.find_element_by_class_name('_1XyCr')
	if excep is not None:
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

	search_input = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
	search_input.send_keys(u'#고양이')
	time.sleep(2)
	search_input.send_keys(Keys.ENTER)
	time.sleep(2)
	search_input.send_keys(Keys.ENTER)

	time.sleep(5)


# 이미지의 src 이용하여 Local 에 다운로드 동작 추가 필요
