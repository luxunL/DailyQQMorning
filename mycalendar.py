# coding=utf-8
"""
https://www.juhe.cn/docs/api/id/606
指定日期的节假日及万年历信息
"""
from datetime import datetime
from datetime import timedelta
import requests
import json
import random
from face import face 

def get_calendar(night):
    """
    获取指定日期的节假日及万年历信息
    https://apis.juhe.cn/fapig/calendar/day.php?date=2021-05-09&detail=1&key=*****
    :param data: str 日期 格式 %Y-%m-%d
    :rtype str
    """
    if night:
        date_ = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    else:
        date_ = datetime.now().strftime('%Y-%m-%d')
    # print('获取 {} 的日历...'.format(date_))
    try:
        key_ = '此处填写你的key值'
        resp = requests.get('https://apis.juhe.cn/fapig/calendar/day.php?detail=1&key='+key_+'&date='+date_)
        # resp = {"reason":"success","result":{"date":"2021-05-09","week":"星期日","statusDesc":"周末","status":'',"animal":"牛","avoid":"订婚.上梁.纳采.盖屋.开仓","cnDay":"日","day":"9","desc":"母亲节","gzDate":"丁巳","gzMonth":"癸巳","gzYear":"辛丑","isBigMonth":"1","lDate":"廿八","lMonth":"三","lunarDate":"28","lunarMonth":"3","lunarYear":"2021","month":"5","suit":"搬家.装修.开业.结婚.入宅.领证.开工.动土.安床.出行.安葬.开张.作灶.旅游.求嗣.赴任.修造.祈福.祭祀.解除.开市.牧养.纳财.纳畜.开光.嫁娶.移徙.经络.立券.求医.竖柱.栽种.斋醮.求财","term":"","value":"母亲节","year":"2021"},"error_code":0}
        if resp.status_code == 200:
            """
            {"reason":"success","result":{"date":"2021-05-09","week":"星期日","statusDesc":"周末","status":null,"animal":"牛","avoid":"订婚.上梁.纳采.盖屋.开仓","cnDay":"日","day":"9","desc":"母亲节","gzDate":"丁巳","gzMonth":"癸巳","gzYear":"辛丑","isBigMonth":"1","lDate":"廿八","lMonth":"三","lunarDate":"28","lunarMonth":"3","lunarYear":"2021","month":"5","suit":"搬家.装修.开业.结婚.入宅.领证.开工.动土.安床.出行.安葬.开张.作灶.旅游.求嗣.赴任.修造.祈福.祭祀.解除.开市.牧养.纳财.纳畜.开光.嫁娶.移徙.经络.立券.求医.竖柱.栽种.斋醮.求财","term":"","value":"母亲节","year":"2021"},"error_code":0}
            """
            # print(resp.text)
            content_dict = resp.json()
            if content_dict['reason'] == 'success':
                data_dict = content_dict['result']
                statusDesc =data_dict['statusDesc']
                # 农历
                lunar_calendar = '{}月{}日'.format(data_dict['lunarMonth'], data_dict['lunarDate'])
                # 节日
                desc=''
                if 'desc' in data_dict.keys():
                    desc = '['+data_dict['desc']+']'
                # 节气
                solarTerms=''
                if data_dict['term']:
                    solarTerms = '['+data_dict['term']+']'
                # 祝福语
                if data_dict['status']==1:
                    blessing = '假期愉快！'+'\n'+face([320,113],2)
                elif data_dict['status']==2:
                    blessing = '工作顺利！'+'\n'+face([158,30,285],3)
                else:
                    if len(statusDesc)>2:
                        blessing = '工作顺利！'+'\n'+face([158,30,285],3)
                    else:
                        blessing = '周末愉快！'+'\n'+face([320,113],2)
                # 纪念日
                commemoration=''
                commDic = json.load(open('commemoration.json',encoding='utf8'))
                commDic['lunar'].keys()
                lunardate = '0'+str(int(data_dict['lunarMonth'])*100+int(data_dict['lunarDate']))
                lunardate = lunardate[-4:]
                solardate = date_.replace('-','')[-4:]
                if lunardate in commDic['lunar'].keys():
                    print(commDic['lunar'][lunardate]) 
                    for x in commDic['lunar'][lunardate]:
                        commemoration+= '\n【'+ x +'】'
                if solardate in commDic['solar'].keys():
                    print(commDic['solar'][solardate])
                    for x in commDic['solar'][solardate]:
                        commemoration+= '\n【'+ x +'】'
                if commemoration:
                    commemoration+='\n别忘了给他(们)送上祝福哦！'
                # suit = data_dict['suit']
                # suit = suit if suit else '无'
                # taboo = data_dict['taboo']
                # taboo = taboo if taboo else '无'

                return_text = '{date} {week}{desc}{commemoration}\n农历{lunarCalendar}{solarTerms}，{blessing}\n'.format(
                    blessing=blessing,
                    commemoration=commemoration,
                    date=date_,
                    desc=desc,
                    solarTerms=solarTerms,
                    week=data_dict['week'],
                    lunarCalendar=lunar_calendar,
                )
                if night:
                    return '明天是 '+return_text
                return '今天是 '+return_text
            else:
                print('获取日历失败:{}'.format(content_dict['message']))
        print('获取日历失败。')
    except Exception as exception:
        print(str(exception))
        return None


if __name__ == '__main__':
    date = datetime.now().strftime('%Y-%m-%d')
    content = get_calendar(False)
    print(content)
