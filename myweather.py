# coding=utf-8

import requests
import json
import os
from datetime import datetime
from datetime import timedelta
from face import face 

__all__ = ['get_today_weather']

MSG_ORI = '天津{low_temp}~{high_temp}{tempface}\n{_type}【{wind}】\n{notice}{noticeFace}'

def get_today_weather(night=False):
    """
     获取天气信息。网址：https://www.sojson.com/blog/305.html .
    :param city_name: str,城市名
    :return: str ,例如：2019-06-12 星期三 晴 南风 3-4级 高温 22.0℃ 低温 18.0℃ 愿你拥有比阳光明媚的心情
    """
    # 天津
    key_ = '101030100'
    weather_url = 'http://t.weather.itboy.net/api/weather/city/'+key_
    
    try:
        resp = requests.get(url=weather_url)
        if resp.status_code == 200:
            # print(resp.text)
            weather_dict = resp.json()
            # 今日天气
            # {
            # "sunrise": "04:45",
            # "high": "高温 34.0℃",
            # "low": "低温 25.0℃",
            # "sunset": "19:37",
            # "aqi": 145,
            # "ymd": "2019-06-12",
            # "week": "星期三",
            # "fx": "西南风",
            # "fl": "3-4级",
            # "type": "多云",
            # "notice": "阴晴之间谨防紫外线侵扰，"
            # }
            if weather_dict.get('status') == 200:
                if night:
                    MSG='明天'+MSG_ORI
                    forecastIndex = 1
                    today_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
                    # 这个天气的接口更新不及时，有时候当天1点的时候，还是昨天的天气信息，如果天气不一致，则取下一天(今天)的数据
                else:
                    MSG='今天'+MSG_ORI
                    forecastIndex = 0
                    today_date = datetime.now().strftime('%Y-%m-%d')
                today_weather = weather_dict.get('data').get('forecast')[forecastIndex]
                weather_today = today_weather['ymd']
                _type=today_weather['type']
                if '雨' in _type:
                    noticeFace=face([90],2)+'☔'+'\n'+'🌂'*6
                elif '阴' in _type:
                    noticeFace=face([91],2)
                elif '晴' in _type:
                    noticeFace=face([74,301],3)
                else:
                    noticeFace=face([202],2)
                if today_date != weather_today:
                    today_weather = weather_dict.get('data').get('forecast')[forecastIndex+1]
                if int(today_weather['low'][3:-1])>25:
                    tempface = '\n好热啊，注意避暑！'+face([301,312],2)
                elif int(today_weather['high'][3:-1])<21:
                    tempface = '\n有些冷，注意保暖哦！'+face([211,60],2)
                else:
                    tempface = face([219],2)
                weather_info = MSG.format(
                    date=today_date,
                    week=today_weather['week'],
                    _type=today_weather['type'],
                    low_temp=today_weather['low'][3:-1],
                    high_temp=today_weather['high'][3:],
                    wind=today_weather['fx'] + today_weather['fl'],
                    notice=today_weather['notice'],
                    tempface=tempface,
                    noticeFace=noticeFace
                )
                return weather_info
            else:
                print('天气请求出错:{}'.format(weather_dict.get('message')))
    except Exception as exception:
        print(str(exception))
        return None

if __name__ == '__main__':
    night = False
    we = get_today_weather(night)
    print(we)