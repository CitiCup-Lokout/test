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
driver.get('http://49.232.24.23:9331/up/546195')
time.sleep(5)


# ======== testD_1 : “固定信息板块”功能测试 ========
# testD_1, case1 ： 基本信息显示是否正确
messagebox.showinfo('testD_1, case1 ： 基本信息显示是否正确','请核实并记录显示的UP主ID、简介是否正确')
time.sleep(1)
messagebox.showinfo('testD_1, case1 ： 基本信息显示是否正确','请核实并记录显示的UP主粉丝数、播放量、本月充电量是否正确')
time.sleep(1)
messagebox.showinfo('testD_1, case1 ： 基本信息显示是否正确','请核实并记录显示的UP主粉丝增长指数、作品指数、总指数是否正确')
time.sleep(1)
messagebox.showinfo('testD_1, case1 ： 基本信息显示是否正确','请核实并记录显示的UP主能力图是否正确')
time.sleep(1)


# testD_1, case2 ： 确认Bilibili链接是否正确
B_channel = driver.find_element_by_link_text('TA的频道');
# 滑动滚轮使得“TA的频道”出现在页面中（顶部）
driver.execute_script("arguments[0].scrollIntoView();", B_channel)
messagebox.showinfo('testD_1, case2 ： 确认Bilibili链接是否正确','接下来将自动点击当前页面顶端UP主个人空间链接')
time.sleep(1)
ActionChains(driver).click(B_channel).perform()
time.sleep(1)
messagebox.showinfo('testD_1, case2 ： 确认Bilibili链接是否正确','请记录打开的链接是否相符')
# 切换到项目网页
windows = driver.window_handles
driver.switch_to.window(windows[0])
time.sleep(1)


# ======== testD_2 :  "基本数据板块"功能测试 ========
# 播放量
view_counts = driver.find_elements_by_link_text('播放量');
# 充电量
battery_counts = driver.find_elements_by_link_text('充电量');

# testD_2, case1 ： 新增量测试
# 滑动滚轮使得“新增数据”出现在页面中（顶部）
# basic = driver.find_element_by_link_text('新增');
# driver.execute_script("arguments[0].scrollIntoView();", basic)
driver.execute_script("arguments[0].scrollIntoView();", view_counts[0])
# 粉丝量
messagebox.showinfo('testD_2, case1 ： 新增量测试','请检查并记录新增粉丝量是否正确')
time.sleep(1)

# 播放量
ActionChains(driver).click(view_counts[0]).perform()
messagebox.showinfo('testD_2, case1 ： 新增量测试','请检查并记录新增播放量是否正确')
time.sleep(1)

# 充电量
ActionChains(driver).click(battery_counts[0]).perform()
messagebox.showinfo('testD_2, case1 ： 新增量测试','请检查并记录新增充电量是否正确')
time.sleep(1)


# testD_2, case2 ： 累计量测试
# 滑动滚轮使得“累计数据”出现在页面中（顶部）
# basic = driver.find_element_by_link_text('累计');
# driver.execute_script("arguments[0].scrollIntoView();", basic)
driver.execute_script("arguments[0].scrollIntoView();", view_counts[1])
# 粉丝量
messagebox.showinfo('testD_2, case2 ： 累计量测试','请检查并记录累计粉丝量是否正确')
time.sleep(1)

# 播放量
ActionChains(driver).click(view_counts[1]).perform()
messagebox.showinfo('testD_2, case2 ： 累计量测试','请检查并记录累计播放量是否正确')
time.sleep(1)

# 充电量
ActionChains(driver).click(battery_counts[1]).perform()
messagebox.showinfo('testD_2, case2 ： 累计量测试','请检查并记录累计充电量是否正确')
time.sleep(1)


# testD_2, case3 ： 预测趋势测试
# 滑动滚轮使得“预测数据”出现在页面中（顶部）
# basic = driver.find_element_by_link_text('预测');
# driver.execute_script("arguments[0].scrollIntoView();", basic)
driver.execute_script("arguments[0].scrollIntoView();", view_counts[2])
# 粉丝量
messagebox.showinfo('testD_2, case2 ： 预测量测试','请检查并记录预测粉丝量是否正确')
time.sleep(1)

# 播放量
ActionChains(driver).click(view_counts[2]).perform()
messagebox.showinfo('testD_2, case2 ： 预测量测试','请检查并记录预测播放量是否正确')
time.sleep(1)



# ======== testD_3 : “视频数据板块”功能测试 ========
# testD_3, case1 : 视频信息测试
video_data = driver.find_element_by_link_text('视频数据');
driver.execute_script("arguments[0].scrollIntoView();", video_data)
time.sleep(1)
ActionChains(driver).click(video_data).perform()
time.sleep(1)
messagebox.showinfo('testD_3, case1 : 视频信息测试','请检查并记录视频信息显示是否正确')
time.sleep(1)

# testD_3, case2 : 视频质量测试
# video_quality = driver.find_element_by_link_text('视频质量');
# driver.execute_script("arguments[0].scrollIntoView();", video_quality)
messagebox.showinfo('testD_3, case2 : 视频质量测试','请检查并记录视频质量显示是否正确')
time.sleep(1)

# testD_3, case3 : 视频追踪测试
video_ch = driver.find_element_by_link_text('视频数据');
driver.execute_script("arguments[0].scrollIntoView();", video_ch)
messagebox.showinfo('testD_3, case3 : 视频追踪测试','请检查并记录视频追踪显示是否正确')
time.sleep(1)


# ======== testD_4 : “估值数据板”功能测试 ========
predict_data = driver.find_element_by_link_text('估值数据');
driver.execute_script("arguments[0].scrollIntoView();", predict_data)
time.sleep(1)
ActionChains(driver).click(predict_data).perform()
time.sleep(1)
messagebox.showinfo('testD_4 :  “估值数据板”功能测试','请检查并记录估值数据板块显示是否正确')
time.sleep(1)

# ======== testD_5 : “粉丝画像板块”功能测试 ========
fans_portrait = driver.find_element_by_link_text('粉丝画像');
driver.execute_script("arguments[0].scrollIntoView();", fans_portrait)
time.sleep(1)
ActionChains(driver).click(fans_portrait).perform()
time.sleep(1)
messagebox.showinfo('testD_5 : “粉丝画像板块”功能测试 ','请检查并记录粉丝画像板块显示是否正确')
time.sleep(1)


messagebox.showinfo('提示','测试已完成，即将退出测试')
# quit driver
driver.quit()