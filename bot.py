import PyOfficeRobot
from PyOfficeRobot.core.WeChatType import *
from PyOfficeRobot.api import chat
from PyOfficeRobot.api import file
from PyOfficeRobot.lib.decorator_utils.instruction_url import instruction
#将PyOfficeRobot模块导入
import random
import requests
from lxml import etree
import papermill as pmdef
import time
from threading import Timer
import re
#引用部分

def get_weather(url):
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
    }

    # 请求Weather API并拿到服务器返回的数据
    rep = requests.get(url, headers = header)
    rep.encoding = "utf-8"
    result = ''
    weather = rep.text

    # 解析服务器返回的数据，具体可参考weather.json文件
    index_cityInfo = weather.find("cityInfo")
    index_cityId = weather.find("cityId")
    index_shidu = weather.find("shidu")
    index_pm25 = weather.find("pm25")
    index_pm10 = weather.find("pm10")
    index_quality = weather.find("quality")
    index_wendu = weather.find("wendu")
    index_ganmao = weather.find("ganmao")
    index_forecast = weather.find("forecast")
    index_ymd = weather.find("ymd", index_forecast)
    index_week = weather.find("week", index_forecast)
    index_sunset = weather.find("sunset", index_forecast)
    index_high = weather.find("high", index_forecast)
    index_low = weather.find("low", index_forecast)
    index_fx = weather.find("fx", index_forecast)
    index_fl = weather.find("fl", index_forecast)
    index_aqi = weather.find("aqi", index_forecast)
    index_type = weather.find("type", index_forecast)
    index_notice = weather.find("notice", index_forecast)

    #bug时尝试输出测试
    # print(index_cityInfo)
    # print(index_cityId)
    # print(index_shidu)
    # print(index_pm25)
    # print(index_pm10)
    # print(index_quality)
    # print(index_wendu)
    # print(index_ganmao)
    # print(index_forecast)
    # print(index_ymd)
    # print(index_week)
    # print(index_sunset)
    # print(index_high)
    # print(index_low)
    # print(index_fx)
    # print(index_fl)
    # print(index_aqi)
    # print(index_type)
    # print(index_notice)

    # 将解析好的数据组装成想要的格式做为函数的返回值
    '''
    # 今日天气预报
    # 年月日 + 星期 + 所在地城市
    # 天气类型 + 风向 + 风力
    # 温度范围（最低温度~最高温度）
    # 污染指数：PM2.5/PM10/AQI
    # 空气质量
    # 当前温度 + 空气湿度
    # Notice信息
    '''
    result = '今日天气预报' + '{ctrl}{ENTER}'\
             + "天气: " + weather[index_type + 7:index_notice - 3] + "{ctrl}{ENTER}" \
             + "污染指数: PM2.5:" + weather[index_pm25 + 6:index_pm10 - 1] + "" \
             + "PM10:" + weather[index_pm10 + 6:index_quality - 1] + "{ctrl}{ENTER}" \
             + "空气质量:" + weather[index_quality + 10:index_wendu - 3] + '{ctrl}{ENTER}' \
             + "当前温度:" + weather[index_wendu + 8:index_ganmao - 3] + " " \
             + "空气湿度:" + weather[index_shidu + 8:index_pm25 - 3] + '{ctrl}{ENTER}' \
             + weather[index_notice + 9:weather.find('}', index_notice) - 1]
    return result
#天气信息部分

def get_news():
	url = "http://open.iciba.com/dsapi/"
	r = requests.get(url)
	content = r.json()['content']
	note = r.json()['note']
	return content, note
#一言部分


def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "平局"
    elif (player_choice == "石头" and computer_choice == "剪刀") or \
         (player_choice == "剪刀" and computer_choice == "布") or \
         (player_choice == "布" and computer_choice == "石头"):
        return "玩家胜利"
    else:
        return "电脑胜利"
    
#石头剪刀布游戏部分

url = 'http://t.weather.sojson.com/api/weather/city/101230506'
# 调用get_weather函数
GW = get_weather(url)
print(GW)
test = get_news()
print(test[0])
print(test[1])


np = random.randint(1,99)
file = str(np) + ".jpg"
#随机照片
mytime = time.localtime()
if mytime.tm_hour < 9:
    payload = '早上好Y(^o^)Y'
else:
    if mytime.tm_hour < 12:
        payload = '上午好Y(^o^)Y'
    else:
        if mytime.tm_hour == 12:
            payload = '中午好Y(^o^)Y'
        else:
            if mytime.tm_hour > 12:
                payload = '下午好Y(^o^)Y'
            else:
                pass

time = time.strftime("%X")
ds = payload + '，这里是今日份每日一言请查收!' + "{ctrl}{ENTER}" + test[0] + '{ctrl}{ENTER}' + test[1]
txt = GW + "{ctrl}{ENTER}" + "现在的时间是:" + '{ctrl}{ENTER}' + time
menu = '机器人菜单' + "{ctrl}{ENTER}" + "1.天气（获取今日天气）" + "{ctrl}{ENTER}" + "2.一言（获取一句鸡汤）" + "{ctrl}{ENTER}" + "3.一图（获取一张风景图）" + "{ctrl}{ENTER}" + "4.开始游戏（打开游戏菜单）"
game = '游戏菜单' + "{ctrl}{ENTER}" + "1.猜数字（猜一个数字）" + "{ctrl}{ENTER}" + "2.石头剪刀布（石头剪刀布）[维修中]"
stjdb = '石头剪刀布游戏开始！' + "{ctrl}{ENTER}" + "请选择：" + "{ctrl}{ENTER}" + "1. 石头" + "{ctrl}{ENTER}" + "2. 剪刀" + "{ctrl}{ENTER}" + "3. 布"

#信息变量

wx = WeChat()
wx.GetSessionList()

# who = '有福同享，有难退群'
who = '妈妈'
wx.ChatWith(who)
#打开微信聊天界面

PyOfficeRobot.chat.send_message(who,ds)
#PyOfficeRobot.chat.send_message(text)
PyOfficeRobot.chat.send_message(who,txt)
PyOfficeRobot.file.send_file(who,file)
#PyOfficeRobot.chat.chat_robot(who)
while True:
        try:
            friend_name, receive_msg = wx.GetAllMessage[-1][0], wx.GetAllMessage[-1][1]  # 获取朋友的名字、发送的信息
            clean_text = re.sub(r'[^\w\s]','',receive_msg)

            if (friend_name == friend_name) & (clean_text == '菜单' or clean_text == '机器人菜单' or clean_text == '打开菜单' or clean_text == '启动机器人') :
                print(f'【{friend_name}】发送：【{receive_msg}】')
                PyOfficeRobot.chat.send_message(who,menu) # 向`who`发送消息

            if (friend_name == friend_name) & (clean_text == '服务检测') :
                print(f'【{friend_name}】发送：【{receive_msg}】')
                PyOfficeRobot.chat.chat_robot(who) # 向`who`发送消息

            if (friend_name == friend_name) & (clean_text == '开始游戏' or clean_text == '游戏' or clean_text == '打开游戏' or clean_text == '启动游戏' or clean_text == '启动' or clean_text == '游戏菜单') :
                print(f'【{friend_name}】发送：【{receive_msg}】')
                PyOfficeRobot.chat.send_message(who,game) # 向`who`发送消息    

            if (friend_name == friend_name) & (clean_text == '天气' or clean_text == '今天天气' or clean_text == '今天天气怎么样' or clean_text == '今天天气') :
                print(f'【{friend_name}】发送：【{receive_msg}】')
                PyOfficeRobot.chat.send_message(who,txt) # 向`who`发送消息

            if (friend_name == friend_name) & (clean_text == '一言' or clean_text == '鸡汤' or clean_text == '来个鸡汤' or clean_text == '没人说话') :
                print(f'【{friend_name}】发送：【{receive_msg}】')
                get_request = requests.get(url='https://v.api.aa1.cn/api/yiyan/index.php')  # 向api接口发送请求
                html = etree.HTML(get_request.text)  # html：爬取得到的网页html内容
                yyyy = html.xpath('/html/body/p/text()')[0]  # xpath路径下提取text文本,取得列表中的第0项，就是一个字符串
                PyOfficeRobot.chat.send_message(who,yyyy) # 向`who`发送消息

            if (friend_name == friend_name) and (clean_text == '一图' or clean_text == '来个图片' or clean_text == '风景') :
                print(f'【{friend_name}】发送：【{receive_msg}】')
                np = random.randint(1,99)
                file = str(np) + ".jpg"
                PyOfficeRobot.file.send_file(who,file) # 向`who`发送消息

            if (friend_name == friend_name) and (clean_text == '猜数字' or clean_text == '猜数' or clean_text == '猜字') :
                print(f'【{friend_name}】发送：【{receive_msg}】')
                target_number = random.randint(1, 100)
                attempts = 0
                last_msg = ""
                handled = False
                while not handled :
                    try:
                        name, msg = wx.GetAllMessage[-1][0], wx.GetAllMessage[-1][1]  # 获取朋友的名字、发送的信息
                        clean_msg = re.sub(r'[^\w\s]','',msg)
                        print(f'【{name}】发送：【{msg}】')
                        if msg == last_msg:
                            continue
                        last_msg = msg
                        if clean_msg == "猜数字" or clean_text == '猜数' or clean_text == '猜字':
                            PyOfficeRobot.chat.send_message(who, "猜一个数字（1-100）：")
                            sent_prompt = True
                            continue

                        if not clean_msg.isdigit():
                            if not sent_prompt:
                                PyOfficeRobot.chat.send_message(who, "请输入一个有效的数字！")
                                sent_prompt = True
                                continue

                        guess = int(clean_msg)
                        attempts += 1

                        if guess < target_number:
                            PyOfficeRobot.chat.send_message(who,"猜小了！")
                        elif guess > target_number:
                            PyOfficeRobot.chat.send_message(who,"猜大了！")
                        else:
                            PyOfficeRobot.chat.send_message(who,f"{friend_name}猜对了！你用了{attempts}次猜中了数字{target_number}。")
                            handled = True
                    except:
                        pass
            # if (friend_name == friend_name) and (receive_msg == '石头剪刀布') :
            #     print(f'【{friend_name}】发送：【{receive_msg}】')
            #     PyOfficeRobot.chat.send_message(who,stjdb)
            #     player_score = 0
            #     computer_score = 0
            #     game_over = False

            #     while not game_over:
            #         name, msg = wx.GetAllMessage[-1][0], wx.GetAllMessage[-1][1]  # 获取朋友的名字、发送的信息
            #         print(f'【{name}】发送：【{msg}】')

            #         if name != "zh_mc"and (msg == "石头" or msg == "剪刀" or msg == "布") :
            #             player_choice = msg
            #             computer_choice = random.choice(["石头", "剪刀", "布"])

            #             result = get_winner(player_choice, computer_choice)
            #             PyOfficeRobot.chat.send_message(who, f"你选择了【{player_choice}】，电脑选择了【{computer_choice}】")
            #             PyOfficeRobot.chat.send_message(who, f"结果：{result}")

            #             if result == "玩家胜利":
            #                 player_score += 1
            #             elif result == "电脑胜利":
            #                 computer_score += 1
            #             if player_score >= 2 or computer_score >= 2:
            #                 game_over = True
            #         else:
            #             PyOfficeRobot.chat.send_message(who, "请输入有效的选择（石头、剪刀、布）！")
            #             continue

            #     if player_score > computer_score:
            #         PyOfficeRobot.chat.send_message(who, "恭喜你，你赢得了比赛！")
            #     else:
            #         PyOfficeRobot.chat.send_message(who, "很遗憾，你输掉了比赛。")

                
        except:
            pass

#信息发送区域
