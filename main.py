# coding=utf-8

"""
每天定时给多个女友发给微信暖心话
核心代码。
"""

import time
# import json
import requests
import platform
import os
import myweather
import mycalendar
import words
import mail

def is_online():
    """
    判断是否还在线。
    :return: bool,当返回为 True 时，在线；False 已断开连接。
    """
    try:
        # go-cqhttp 默认host port
        requests.get('http://127.0.0.1:5700')
        return True
    except:
        print('QQ已断开连接!')
        mail.mail('QQ已断开连接!')
        return False

def send_msg(night = False):
    """ 发送定时提醒 """
    print('发送中...')
    if not is_online(): 
        return 
    calendar_info = mycalendar.get_calendar(night)
    weather = myweather.get_today_weather(night)
    sweet_words = words.final_one_words(night)
    send_msg = '\n'.join(
        x for x in [sweet_words, calendar_info, weather] if x)
    qqlist=["your girlfriends' QQid",'10001']
    for qid in qqlist:
        url = "http://127.0.0.1:5700/send_private_msg?user_id="+qid+"&message="+send_msg
        response = requests.get(url)
    print('\n{}\n发送成功...\n\n'.format(send_msg))
    print('消息发送完成...\n')


if __name__ == '__main__':
    night = int(time.strftime('%H'))>21
    send_msg(night)
