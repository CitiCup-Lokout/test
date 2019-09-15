# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
import time
from tkinter import messagebox

# 登录网页
driver = webdriver.Chrome()
driver.maximize_window()
# 访问“老番茄”的个人信息网页
driver.get('http://49.232.24.23:9331/report/')
time.sleep(5)


# ======== testE_1 : 视频链接正确性测试 ========
center_head = driver.find_element_by_class_name('uk-text-center');
video_links = driver.find_elements_by_class_name('uk-link-heading');
driver.execute_script("arguments[0].scrollIntoView();", center_head)
time.sleep(1)

# 点击第一个视频链接
messagebox.showinfo('testE_1 : 视频链接正确性测试','即将点击第一个视频链接')
time.sleep(1)
ActionChains(driver).click(video_links[0]).perform()
time.sleep(1)
messagebox.showinfo('testE_1 : 视频链接正确性测试','请记录视频链接的正确性')

windows = driver.window_handles
driver.switch_to.window(windows[0])
time.sleep(1)

# 点击第二个视频链接
messagebox.showinfo('testE_1 : 视频链接正确性测试','即将点击第二个视频链接')
time.sleep(1)
ActionChains(driver).click(video_links[1]).perform()
time.sleep(1)
messagebox.showinfo('testE_1 : 视频链接正确性测试','请记录视频链接的正确性')

windows = driver.window_handles
driver.switch_to.window(windows[0])
time.sleep(1)

# 点击第三个视频链接
messagebox.showinfo('testE_1 : 视频链接正确性测试','即将点击第三个视频链接')
time.sleep(1)
ActionChains(driver).click(video_links[2]).perform()
time.sleep(1)
messagebox.showinfo('testE_1 : 视频链接正确性测试','请记录视频链接的正确性')

windows = driver.window_handles
driver.switch_to.window(windows[0])
time.sleep(1)


# ======== testE_2 : 分类正确性测试 ========
classes = driver.find_elements_by_class_name('switcher-large-text');
time.sleep(1)

# 点击行业资讯分类
messagebox.showinfo('testE_2 : 分类正确性测试','即将点击“行业资讯”，请记录显示内容的正确性')
time.sleep(1)
ActionChains(driver).click(classes[1]).perform()
time.sleep(1)

# 点击涨粉月刊分类
messagebox.showinfo('testE_2 : 分类正确性测试','即将点击“点击涨粉月刊分类”，请记录显示内容的正确性')
time.sleep(1)
ActionChains(driver).click(classes[2]).perform()
time.sleep(1)

# 点击吃瓜月刊分类
messagebox.showinfo('testE_2 : 分类正确性测试','即将点击“点击吃瓜月刊分类”，请记录显示内容的正确性')
time.sleep(1)
ActionChains(driver).click(classes[3]).perform()
time.sleep(1)

# 点击播放量月刊分类
messagebox.showinfo('testE_2 : 分类正确性测试','即将点击“点击播放量月刊分类”，请记录显示内容的正确性')
time.sleep(1)
ActionChains(driver).click(classes[4]).perform()
time.sleep(1)


messagebox.showinfo('提示','测试已完成，即将退出测试')
# quit driver
driver.quit()