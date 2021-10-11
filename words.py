# coding=utf-8
"""
https://chp.shadiao.app/?from_nmsl
彩虹屁生成器
 """
import requests
import random
from face import face
from face import randomText

__all__ = ['get_caihongpi_info']


def get_one_words():
    """
    彩虹屁生成器
    :return: str,彩虹屁
    """
    try:
        #return loveWord()
        resp = requests.get('https://chp.shadiao.app/api.php')
        if resp.status_code == 200:
            if '访问太频繁' in resp.text:
                return loveWord()
            return resp.text
        print('彩虹屁获取失败。')
    except requests.exceptions.RequestException as exception:
        print(exception)
        return loveWord()
    return loveWord()
    
def goodnight():
    words = []
    with open('goodnight',encoding='utf8') as f:
        words = f.readlines()
    return randomText(words).replace("\t", "\n")

def loveWord():
    words = []
    with open('lovewords',encoding='utf8') as f:
        words = f.readlines()
    return randomText(words)
    
def loveyou():
    loveyou_word=randomText(['爱你哟','爱你 爱你 爱你','超~~~~爱你','今天也是爱你的一天！'])
    facelist=[66,42,63,85,49,109]
    return face(facelist)+loveyou_word+face(facelist)+'\n'
    
def final_one_words(night=False):
    """
    彩虹屁生成器
    :return: str,彩虹屁
    """
    if night:
        return '晚安[CQ:face,id=75]，臭宝！\n'+loveyou()+goodnight()+face([66,277,60])
    return '早安[CQ:face,id=74]，宝宝！\n'+loveyou()+'[CQ:face,id=277]今日份土味情话[CQ:face,id=277]\n'+get_one_words()+'\n'+face([192])*6

if __name__ == '__main__':
    ow = final_one_words()
    print(ow)
    pass
