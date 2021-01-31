import RPi.GPIO as GPIO
import time

Trig_Pin = 20   # 定义发射超声波引脚20
Echo_Pin = 21   # 定义接受回声的引脚21
LedPin = 17     # 定义激光模块BCM编码引脚17

GPIO.setmode(GPIO.BCM)                              # 使用BCM编码的引脚图
GPIO.setup(Trig_Pin, GPIO.OUT, initial=GPIO.LOW)    # 初始化引脚信息
GPIO.setup(Echo_Pin, GPIO.IN)                       # 初始化引脚信息
GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.LOW)      # 初始化引脚信息

time.sleep(2)   # 延时2秒


def loop(speed):
    print("...Laser off...")
    GPIO.output(LedPin, GPIO.LOW)   # 输出引脚设置为低电平，此时停止激光
    time.sleep(speed * 0.005)
    print("...Laser on...")
    GPIO.output(LedPin, GPIO.HIGH)  # 输出引脚设置为高电平，此时开始激光
    time.sleep(speed * 0.005)


def check_distance():                       # 定义检测距离函数
    while True:
        GPIO.output(Trig_Pin, GPIO.HIGH)    # 发射引脚设置为高电平，此时发射超声波
        time.sleep(0.00015)                 # 持续0.00015秒
        GPIO.output(Trig_Pin, GPIO.LOW)     # 发射引脚设置为低电平，此时停止超声波
        while GPIO.input(Echo_Pin) == 0:    # 捕捉 echo 端输出上升沿
            pass
        t1 = time.time()
        while GPIO.input(Echo_Pin) == 1:    # 捕捉 echo 端输出下降沿
            pass
        t2 = time.time()
        dist = (t2 - t1) * 340 * 100 / 2
        print(f"Distance is{dist}cm")
        loop(dist)


if __name__ == '__main__':
    try:
        check_distance()
        time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()                      # 释放脚本中使用的资源，避免损坏树莓派
