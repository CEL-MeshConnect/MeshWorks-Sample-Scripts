####################################################
# MONTY Dev Kit Device
# Sample sensor disc script   
####################################################
# we have 3 Control Points: 2 LEDs and 1 PWM buzzer 
  
# 1. green LED is on PA6 
greenLed = ["greenLed", "PA6", "digital", "grLedF", 1]
greenValues = ["discrete", 2, "off", "on"]
  
# 2. red LED is on PA7 
redLed = ["redLed", "PA7", "digital", "rdLedF", 1]
redValues = ["discrete", 2, "off", "on"]
  
# 3. buzzer on PB7  
buzzer = ["buzzer", "PB7", "PWM", "buzzerF", 1] 
buzzerVal = ["range", 1, 12, "tone"]  
  
####################################################
# 2 digital Data Points: button and Reed switch 
  
# 1. button on PB6 
button = ["button", "PB6", "digital", "buttonF", 1] 
bValues = ["discrete", 2, "up", "down"] 
  
prevButtonValue = 0 
buttonTickCount = 0
  
def buttonF():
    value = readDigital()
    if (buttonTickCount > 30):
        buttonTickCount = 0
        sendDataReport(value, "button state")
    # on different value, send report 
    if (value != prevButtonValue):  
        sendDataReport(value, "button state")
    prevButtonValue = value
    buttonTickCount = (buttonTickCount + 1)
  
# 2. reed switch on PB4  
reedSw = ["reedSw", "PB4", "digital", "reedSwF", 1] 
rsValues = ["discrete", 2, "no contact", "contact"] 
  
prevReedSwValue = 0
reedSwTickCount = 0
  
def reedSwF():
    value = readDigital()
    if (reedSwTickCount > 30):
        reedSwTickCount = 0
        sendDataReport(value, "reedsw state")
    # on different value, send report 
    if (value != prevReedSwValue):  
        sendDataReport(value, "reedsw state")
    prevReedSwValue = value
    reedSwTickCount = (reedSwTickCount + 1)

####################################################
# the temp/humiditysensor is an I2C device

# define the temperature measurement data point
tempSensor = ["tempSensor", "PA1", "i2c", "tempMeasFunc", 40]
tempSensorValues = ["range", -40, 120]

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
    sendDataReport(value, "degrees F")

# define the humidity measurement data point
humiditySensor = ["humiditySensor", "PA1", "i2c", "humidMeasFunc", 40]
humiditySensorValues = ["range", 0, 100]

# function to read temperature
def humidMeasFunc():
    value = readI2c(0x41, 0xE5, bigEndian)
    # convert from reading to %
    value = (value * 125)
    value = (value / 65535)
    value = (value - 6)
    sendDataReport(value, "percent RH")

# define the accelerometer sensor data point
accel = ["accel", "PA1", "i2c", "accelFunc", 1]
accelValues = ["range", 0, 65535]
  
# function to read accelerometer 
def accelFunc():
    xValue = readI2c(0x69, 0x3B, bigEndian)
    yValue = readI2c(0x69, 0x3D, bigEndian)
    # Turn on RED led on other node if over approx 45 degress on either axis
    if (xValue > 8700):
        if (xValue < 57000):
            celPy.AdjustRemoteControlPoint("Sensor 2", "redLed", 0)
            return
    if (yValue > 8192):
        if (yValue < 60000):
            celPy.AdjustRemoteControlPoint("Sensor 2", "redLed", 0)
            return
    if (xValue < 8700):
        if (yValue < 8192):
            celPy.AdjustRemoteControlPoint("Sensor 2", "redLed", 1)
            return
        if (yValue > 60000):
            celPy.AdjustRemoteControlPoint("Sensor 2", "redLed", 1)
            return
    if (xValue > 57000):
        if (yValue < 8192):
            celPy.AdjustRemoteControlPoint("Sensor 2", "redLed", 1)
            return
        if (yValue > 60000):
            celPy.AdjustRemoteControlPoint("Sensor 2", "redLed", 1)
            return

# define the proximity sensor data point
proxSens = ["proximitySensor", "PA1", "i2c", "proximitySensorFunc", 1]
proxValues = ["range", 0, 65535]
  
# function to read infrared light 
def proximitySensorFunc():
    writeI2c(0x5A, 0x07, 0x18)
    value = readI2c(0x5A, 0x26, littleEndian)
    if (value > 700):
            if (value > 700):
                celPy.AdjustLocalControlPoint("buzzer", 262)
                return
            if (value > 1400):
                celPy.AdjustLocalControlPoint("buzzer", 523)
                return
            if (value > 2800):
                celPy.AdjustLocalControlPoint("buzzer", 1047)
                return
            if (value > 5600):
                celPy.AdjustLocalControlPoint("buzzer", 2093)
                return
    if (value < 700):
        celPy.AdjustLocalControlPoint("buzzer", 0)

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
celPy.ApplicationName = "MeshWorks Demo"  
celPy.DeviceName = "Sensor 1" 
celPy.IsSleepyDevice = False
celPy.DataCollectionPoints = [button, reedSw, tempSensor, humiditySensor, accel, proxSens] 
celPy.DataCollectionValues = [bValues, rsValues, tempSensorValues, humiditySensorValues, accelValues, proxValues]
celPy.ControlPoints = [greenLed, redLed, buzzer]
celPy.ControlValues = [greenValues, redValues, buzzerVal] 
  
def main(): 
    # Disable buzzer at boot
    celPy.AdjustLocalControlPoint("buzzer", 0)
    # Init prox sensor
    writeI2c(0x5A, 0x17, 0x07)
    writeI2c(0x5A, 0x37, 0x17)
    writeI2c(0x5A, 0xA1, 0x18)
    writeI2c(0x5A, 0x0B, 0x0F)
    # Init accelerometer
    writeI2c(0x69, 0x02, 0x37)
    writeI2c(0x69, 0x01, 0x6B)
