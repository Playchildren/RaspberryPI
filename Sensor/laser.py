import RPi.GPIO as GPIO
import time

LedPin = 17    # 定义激光模块BCM编码引脚17


def setup():
    GPIO.setmode(GPIO.BCM)                          # 使用BCM编码的引脚图
    GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.LOW)  # 初始化引脚信息


def loop():
    while True:
        print("...Laser off...")
        GPIO.output(LedPin, GPIO.LOW)   # 输出引脚设置为低电平，此时停止激光
        time.sleep(0.5)
        print("...Laser on...")
        GPIO.output(LedPin, GPIO.HIGH)  # 输出引脚设置为高电平，此时开始激光
        time.sleep(0.5)


def destroy():
    GPIO.output(LedPin, GPIO.LOW)      # 输出引脚设置为低电平，此时停止激光
    GPIO.cleanup()                     # 释放脚本中使用的资源，避免损坏树莓派


if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        print("... Laser stop...")
        destroy()
