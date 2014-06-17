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

# 4. Magnetic Lock On/Off on PA4 - TB10  high is lock open
lockOnOff = ["lockOnOff", "PA4", "digital", "lockOnOffF", 1] 
lockOnOffValues = ["discrete", 2, "low", "high"] 
  
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
            celPy.AdjustLocalControlPoint("lockOnOff", 0)
            celPy.AdjustRemoteControlPoint("Machine", "led", 1)
        if (value == 1):
            print("Button down")
            celPy.AdjustLocalControlPoint("lockOnOff", 1)
            celPy.AdjustRemoteControlPoint("Machine", "led", 0)
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

celPy.addTickFunction(workMonitor, 20)

tickCount = 0

def workMonitor():
    if (tickCount == 0):
        # Start the machine and lockout
        celPy.AdjustLocalControlPoint("lockOnOff", 0)
        celPy.AdjustRemoteControlPoint("Machine", "led", 0)       
    if (tickCount > 14):
        # Turn off the machine and unlock
        celPy.AdjustLocalControlPoint("lockOnOff", 1)
        celPy.AdjustRemoteControlPoint("Machine", "led", 1)
    tickCount = (tickCount + 1)
    if (tickCount > 16):
        # Clear after one more tick in the off state to restart routine
        tickCount = 0
  
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
celPy.DeviceName = "Lockout Box"  
celPy.IsSleepyDevice = False
celPy.DataCollectionPoints = [button, reedSw] 
celPy.DataCollectionValues = [bValues, rsValues]
celPy.ControlPoints = [greenLed, redLed, buzzer, lockOnOff] 
celPy.ControlValues = [greenValues, redValues, buzzerVal, lockOnOffValues] 
  
def main(): 
    prevButtonValue = 0 
    tickCount = 0
    celPy.AdjustLocalControlPoint("lockOnOff", 0)
    celPy.AdjustRemoteControlPoint("Machine", "led", 0)
