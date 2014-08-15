####################################################
# MONTY Dev Kit Device
# Immediate Chat End Node Script   
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
celPy.ApplicationName = "Quick Chat"
celPy.DeviceName = "Node 02" 
celPy.IsSleepyDevice = False
celPy.serialReplacementEnable = True
celPy.SerialReplacementStartMode = "immediate"
celPy.SerialReplacementBaudRate = 19200
celPy.ControlPoints = [greenLed, redLed, buzzer]
celPy.ControlValues = [greenValues, redValues, buzzerVal] 
  
def main(): 
    pass
