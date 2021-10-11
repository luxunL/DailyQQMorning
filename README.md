# DailyQQMorning

QQ每天定时给女朋友(们)发早安晚安

1.基于[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)实现

2.在[EverydayWechat](https://github.com/sfyc23/EverydayWechat)的基础上简单改改的

## 使用方法：
1.在linux系统中通过cron命令实现定时运行（其他系统我也不了解，自己动手实现吧

2.go-cqhttp选择云函数服务，（其他服务没了解

### 需要修改的参数/文件
1.main.py  qqlist

2.myweather.py   key_,MSG_ORI

3.mycalendar.py   key_

4.commemoration.json

5.mail.py  username,password，rcptto   (qq掉线，则发送掉线提醒

## 后续可能增加的服务
1.若qq掉线则把早安发给QQ邮箱

2.增加配置文件，不需要修改.py文件

3.在代码中实现定时运行

4.掉线实现自动登录

5.将获取的每日情话自动添加到本地文件中

6.暂时想不出来了= = 欢迎[Issue](https://github.com/luxunL/DailyQQMorning/issues)

  
