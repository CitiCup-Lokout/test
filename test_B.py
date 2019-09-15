# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
import time
from tkinter import messagebox

# 登录网页
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://49.232.24.23:9331/')
time.sleep(5)


# ======== testB_1 : “招标发布区”功能测试 ========
bid = driver.find_element_by_link_text('招标发布区');
ActionChains(driver).click(bid).perform()
time.sleep(1)
messagebox.showinfo('testB_1 : “招标发布区”功能测试','请记录招标发布区内容是否正确')
time.sleep(1)

# ======== testB_2 : “任务发布区”功能测试 ========
task = driver.find_element_by_link_text('任务发布区');
ActionChains(driver).click(task).perform()
time.sleep(1)
messagebox.showinfo('testB_2 : “任务发布区”功能测试','请记录任务发布区内容是否正确')
time.sleep(1)


messagebox.showinfo('提示','测试已完成，即将退出测试')
# quit driver
driver.quit()