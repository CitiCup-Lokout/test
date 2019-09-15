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
driver.get('http://49.232.24.23:9331/')
time.sleep(5)

# 左上角Lokout图标，点击返回主页
# testA_6 ： “返回主页”功能测试函数
lokout_icon = driver.find_element_by_class_name('uk-navbar-left')
def go_homepage():
	ActionChains(driver).click(lokout_icon).perform()
	time.sleep(1)


# ======== testA_1 : “搜索”功能测试 ========
# 获取输入框
inputElement = driver.find_element_by_class_name('uk-search-input')

# testA_1, case1：搜索全称ID
# 输入框输入"老番茄"，并敲击回车
inputElement.send_keys("老番茄") 
time.sleep(1)
inputElement.send_keys(Keys.ENTER)
messagebox.showinfo('testA_1, case1：搜索全称ID','请记录结果是否正确，接下来将返回首页')

go_homepage() # 返回主页
# testA_1, case2：搜索部分ID
# 输入框输入"老番茄"，并敲击回车
inputElement = driver.find_element_by_class_name('uk-search-input')
inputElement.send_keys("老") 
time.sleep(1)
inputElement.send_keys(Keys.ENTER)
messagebox.showinfo('testA_1, case2：搜索部分ID','请记录结果是否正确，接下来将点击“老番茄”进入UP主个人界面')
time.sleep(1)

# 点击老番茄进入个人主页
#wait = ui.WebDriverWait(driver,10)
#wait.until(lambda driver: driver.find_element_by_link_text('老番茄'))
lao_fan_qie = driver.find_element_by_class_name('uk-link-heading');
ActionChains(driver).click(lao_fan_qie).perform()
messagebox.showinfo('testA_1, case2：搜索部分ID','请记录结果是否正确，接下来将返回首页')

go_homepage() # 返回主页


# ======== testA_2 : “排行榜”功能测试 ========
rank = driver.find_element_by_link_text('排名');
ActionChains(driver).click(rank).perform()
messagebox.showinfo('testA_2：“排行榜”功能测试','请记录结果是否正确，接下来将返回首页')
time.sleep(1)
go_homepage() # 返回主页



# ======== testA_3 : "招标发布区"和“任务发布区”测试 ========
# testA_3, case1 : “招标发布区”测试
rank = driver.find_element_by_link_text('招标发布区');
ActionChains(driver).click(rank).perform()
messagebox.showinfo('testA_3, case1：“招标发布区”测试','请记录结果是否正确，接下来将返回首页点击“任务发布区”')
time.sleep(1)
go_homepage() # 返回主页

# testA_3, case2 : “任务发布区”测试
rank = driver.find_element_by_link_text('任务发布区');
ActionChains(driver).click(rank).perform()
messagebox.showinfo('testA_3, case2：“任务发布区”测试','请记录结果是否正确，接下来将返回首页')
time.sleep(1)
go_homepage() # 返回主页


# ======== testA_4 : “视频报告区”功能测试 ========
rank = driver.find_element_by_link_text('报告区');
ActionChains(driver).click(rank).perform()
messagebox.showinfo('testA_4：“报告区”测试','请记录结果是否正确，接下来将返回首页')
time.sleep(1)
go_homepage() # 返回主页


# ======== testA_5 : “登录”功能测试 ========
# 本功能未开发

# ======== testA_6 : “返回主页”功能测试 ========
# 在testA_1, testA_2, testA_3中已经测试

# ======== testA_7 : “基本信息”功能测试 ========
# 人工审核
# 移动到页面底端
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# testA_7, case1 : “网站功能”检查
messagebox.showinfo('testA_7, case1：“基本信息”测试','请记录显示的“网站功能”是否正确')
time.sleep(1)

# testA_7, case2 : “合作伙伴”检查
messagebox.showinfo('testA_7, case2：“合作伙伴”测试','请记录显示的“合作伙伴”是否正确')
time.sleep(1)

# testA_7, case3 : “联系我们”检查
messagebox.showinfo('testA_7, case3：“联系我们”测试','请记录显示的“联系我们”是否正确')
time.sleep(1)


messagebox.showinfo('提示','测试已完成，即将退出测试')
# quit driver
driver.quit()