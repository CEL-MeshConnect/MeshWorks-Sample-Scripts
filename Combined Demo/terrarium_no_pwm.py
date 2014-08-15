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
  
fanOnOff = ["fanOnOff", "PA4", "digital", "fanOnOffF", 1] 
fanOnOffValues = ["discrete", 2, "low", "high"] 
  
lightOnOff= ["lightOnOff", "PA3", "digital", "lightOnOffF", 1]
lightOnOffValues = ["discrete", 2, "on", "off"] 
  
####################################################
# 2 digital Data Points: button and Reed switch 
  
# 1. button output on PB6 
button = ["button", "PB6", "digital", "buttonF", 1] 
bValues = ["discrete", 2, "up", "down"] 
  
prevButtonValue = 0 
  
def buttonF():
    value = readDigital() 
    # on different value, send report 
    if (value != prevButtonValue):  
        if (value == 0):
            print("Button up")
            celPy.AdjustLocalControlPoint("lightOnOff", 1)
            celPy.AdjustLocalControlPoint("fanOnOff", 0)
        if (value == 1):
            print("Button down")
            celPy.AdjustLocalControlPoint("fanOnOff", 1)
            celPy.AdjustLocalControlPoint("lightOnOff", 0)
    prevButtonValue = value 
  
# 2. reed switch output on PB4  
reedSw = ["reedSw", "PB4", "digital", "reedSwF", 1] 
rsValues = ["discrete", 2, "no contact", "contact"] 
  
prevReedSwValue = 0 
  
def reedSwF():
    value = readDigital() 
    # on different value, send report 
    if (value != prevReedSwValue):  
        if (value == 0):
            sendDataReportString("no contact")
        if (value == 1):
            sendDataReportString("contact") 
    prevReedSwValue = value 
  
####################################################
# the temp/humiditysensor is an I2C device
  
# define the temperature measurement data point 
tempSensor = ["tempSensor", "PA1", "i2c", "tempMeasFunc", 20] 
tempSensorValues = ["range", -40, 120]

# Temperature to hold the system at
holdTemp = 75
  
# function to read temperature
def tempMeasFunc(): 
    value = readI2c(0x41, 0xE3, bigEndian)
    # convert from reading to degrees C 
    value = (value * 175) 
    value = (value / 65535) 
    value = (value - 47)
    # convert from degrees C to degrees F 
    value = (value * 18)
    value = (value / 10)
    value = (value + 32)
    # X0 adjustment 
    value = (value - 13)
    sendDataReport(value, "degrees F")
    if (value > 78):
        celPy.AdjustLocalControlPoint("fanOnOff", 1)
        celPy.AdjustLocalControlPoint("lightOnOff", 0)
    if (value < 74):
        celPy.AdjustLocalControlPoint("fanOnOff", 0)
        celPy.AdjustLocalControlPoint("lightOnOff", 1)
  
# define the humidity measurement data point
humiditySensor = ["humiditySensor", "PA1", "i2c", "humidMeasFunc", 20]
humiditySensorValues = ["range", 0, 100]
  
# function to read temperature
def humidMeasFunc():
    value = readI2c(0x41, 0xE5, bigEndian)
    # convert from reading to % 
    value = (value * 125) 
    value = (value / 65535) 
    value = (value - 6) 
    sendDataReport(value, "percent RH") 
  
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
celPy.ApplicationName = "MeshWorks"  
celPy.DeviceName = "Terrarium"  
celPy.IsSleepyDevice = False
celPy.DataCollectionPoints = [button, reedSw, tempSensor, humiditySensor] 
celPy.DataCollectionValues = [bValues, rsValues, tempSensorValues, humiditySensorValues]
celPy.ControlPoints = [greenLed, redLed, buzzer, fanOnOff, lightOnOff] 
celPy.ControlValues = [greenValues, redValues, buzzerVal, fanOnOffValues, lightOnOffValues] 
  
def main(): 
    prevButtonValue = 0 
    # Init temp/humidity sensor 
    celPy.AdjustLocalControlPoint("buzzer", 0)
    celPy.AdjustLocalControlPoint("fanOnOff", 0)
    celPy.AdjustLocalControlPoint("lightOnOff", 1)
  
