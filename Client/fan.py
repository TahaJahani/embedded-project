import RPi.GPIO as GPIO

FAN_PORT_NO = 16
is_on = False


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FAN_PORT_NO, GPIO.OUT)


def turn_off_fan():
    global is_on
    GPIO.output(FAN_PORT_NO, GPIO.LOW)
    is_on = False


def turn_on_fan():
    global is_on
    GPIO.output(FAN_PORT_NO, GPIO.HIGH)
    is_on = True


def cleanup():
    GPIO.cleanup()
