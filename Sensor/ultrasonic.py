"""
超声波测距基础实现
"""

import RPi.GPIO as GPIO     # 导入GPIO模块
import time                 # 导入系统time模块


Trig_Pin = 20   # 定义发射超声波引脚20
Echo_Pin = 21   # 定义接受回声的引脚21

GPIO.setmode(GPIO.BCM)                              # 使用BCM编码的引脚图
GPIO.setup(Trig_Pin, GPIO.OUT, initial=GPIO.LOW)    # 初始化引脚信息
GPIO.setup(Echo_Pin, GPIO.IN)                       # 初始化引脚信息

time.sleep(2)   # 延时2秒


def check_distance():                   # 定义检测距离函数
    GPIO.output(Trig_Pin, GPIO.HIGH)    # 发射引脚设置为高电平，此时发射超声波
    time.sleep(0.00015)                 # 持续0.00015秒
    GPIO.output(Trig_Pin, GPIO.LOW)     # 发射引脚设置为低电平，此时停止超声波
    while GPIO.input(Echo_Pin) == 0:    # 捕捉 echo 端输出上升沿
        pass
    t1 = time.time()
    while GPIO.input(Echo_Pin) == 1:    # 捕捉 echo 端输出下降沿
        pass
    t2 = time.time()
    print((t2-t1)*340*100/2)


try:
    while True:
        check_distance()    # 循环调用主函数
        time.sleep(1)       # 延时1.0秒
except KeyboardInterrupt:   # 如果被键盘输入中断
    GPIO.cleanup()          # 释放脚本中使用的资源，避免损坏树莓派
