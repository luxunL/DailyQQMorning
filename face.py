# coding=utf-8
"""
表情生成器
表情 CQ 码 ID 表
https://github.com/kyubotics/coolq-http-api/wiki/%E8%A1%A8%E6%83%85-CQ-%E7%A0%81-ID-%E8%A1%A8
 """
import requests
import random

def randomText(textArr,n=1):
    length = len(textArr)
    if n in [0,1]:
        return str(textArr[random.randint(0,length-1)])
    if length < 1:
        print('textArr is None!')
        return ''
    l=[randomText(textArr,0) for i in range(n)]
    return l

def face(textArr,n=1):
    args = randomText(textArr,n)
    # print(args.__class__.__name__)
    if not args.__class__.__name__ == 'list':
        args = [args]
    re = ('[CQ:face,id={}]'*n).format(*args)
    return re

if __name__ == '__main__':
    facelist=[66,42,63,85,49,109]
    fc = face([12],2)
    print(fc)
    pass
