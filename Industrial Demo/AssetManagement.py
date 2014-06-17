####################################################
# MONTY Dev Kit Device
# Sample script 
  
####################################################
# we have 3 Control Points: 2 LEDs and 1 PWM buzzer 
  
# 1. green LED input is PA6 
greenLed = ["greenLed", "PA6", "digital", "grLedF", 1]
greenValues = ["discrete", 2, "off", "on"]
  
# 2. red LED input is PA7 
redLed = ["redLed", "PA7", "digital", "rdLedF", 1]
redValues = ["discrete", 2, "off", "on"]
  
# 3. buzzer input on PB7  
buzzer = ["buzzer", "PB7", "PWM", "buzzerF", 1] 
buzzerVal = ["range", 1, 12, "tone"]  
  
  
####################################################
# 2 digital Data Points: button and Reed switch 
  
# 1. button output on PB6 
button = ["button", "PB6", "digital", "buttonF", 3] 
bValues = ["discrete", 2, "up", "down"] 
  
# 2. reed switch output on PB4  
reedSw = ["reedSw", "PB4", "digital", "reedSwF", 3] 
rsValues = ["discrete", 2, "no contact", "contact"] 
  
  
####################################################
# the light sensor is an I2C device 
# it can do visible light and IR light
  
# define the proximity sensor data point
proxSens = ["proximitySensor", "PA1", "i2c", "proximitySensorFunc", 1]
proxValues = ["range", 0, 65535]
  
# function to read infrared light 
def proximitySensorFunc():
    writeI2c(0x5A, 0x07, 0x18)
    value = readI2c(0x5A, 0x26, littleEndian)
    sendDataReport(value, "PS raw reading") 
    if (value > 3000):
        alarmState = 0
        celPy.AdjustLocalControlPoint("redLed", 1)
        return
    if (value < 3000):
        alarmState = 1
        celPy.AdjustLocalControlPoint("redLed", 0)

# define the accelerometer sensor data point
accel = ["accel", "PA1", "i2c", "accelFunc", 1]
accelValues = ["range", 0, 65535]
  
# function to read accelerometer 
def accelFunc():
    xValue = readI2c(0x69, 0x3B, bigEndian)
    yValue = readI2c(0x69, 0x3D, bigEndian)
    if (xValue > 57000):
        if (yValue < 8192):
            tiltAlarmState = 0
            celPy.AdjustLocalControlPoint("redLed", 1)
            return
        if (yValue > 60000):
            tiltAlarmState = 0
            celPy.AdjustLocalControlPoint("redLed", 1)
            return
    if (xValue < 8700):
        if (yValue < 8192):
            tiltAlarmState = 0
            celPy.AdjustLocalControlPoint("redLed", 1)
            return
        if (yValue > 60000):
            tiltAlarmState = 0
            celPy.AdjustLocalControlPoint("redLed", 1)
            return
    if (xValue < 57000):
        if (xValue > 8700):
            tiltAlarmState = 1
            celPy.AdjustLocalControlPoint("redLed", 0)
    if (yValue > 8192):
        if (yValue < 60000):
            tiltAlarmState = 1
            celPy.AdjustLocalControlPoint("redLed", 0)

# alarm tick every 200 ms 
celPy.addTickFunction(alarm, 2)

alarmState = 0 
  
def alarm():
    if (alarmState == 0):
        if (tiltAlarmState == 0):
            celPy.AdjustLocalControlPoint("buzzer", 0) 
    if (alarmState == 1):
        celPy.AdjustLocalControlPoint("buzzer", 1000)
        alarmState = 2
        return
    if (alarmState == 2):
        celPy.AdjustLocalControlPoint("buzzer", 3000)
        alarmState = 1

# alarm tick every 200 ms 
celPy.addTickFunction(tiltAlarm, 2)

tiltAlarmState = 0 
  
def tiltAlarm():
    if (tiltAlarmState == 0):
        if (alarmState == 0):
            celPy.AdjustLocalControlPoint("buzzer", 0) 
    if (tiltAlarmState == 1):
        celPy.AdjustLocalControlPoint("buzzer", 6000)
        tiltAlarmState = 2
        return
    if (tiltAlarmState == 2):
        celPy.AdjustLocalControlPoint("buzzer", 3000)
        tiltAlarmState = 1
  
celPy.addTickFunction(heartbeatLed, 20) 
  
ledState = 0
  
def heartbeatLed(): 
    if (ledState == 0): 
        celPy.AdjustLocalControlPoint("greenLed", 1)
        ledState = 1
        return
    if (ledState == 1): 
        celPy.AdjustLocalControlPoint("greenLed", 0)
        ledState = 0
  
####################################################
# device configuration
celPy.ApplicationName = "Industrial Demo" 
celPy.DeviceName = "Crate" 
celPy.IsSleepyDevice = False
celPy.DataCollectionPoints = [button, reedSw, proxSens, accel] 
celPy.DataCollectionValues = [bValues, rsValues, proxValues, accelValues]
celPy.ControlPoints = [greenLed, redLed, buzzer]
celPy.ControlValues = [greenValues, redValues, buzzerVal] 
  
def main(): 
    # Init prox sensor
    writeI2c(0x5A, 0x17, 0x07)
    writeI2c(0x5A, 0x37, 0x17)
    writeI2c(0x5A, 0xA1, 0x18)
    writeI2c(0x5A, 0x0B, 0x0F)
    # Init accelerometer
    writeI2c(0x69, 0x02, 0x37)
    writeI2c(0x69, 0x01, 0x6B)
    celPy.AdjustLocalControlPoint("buzzer", 0)
    alarmState = 0
    tiltAlarmState = 0
