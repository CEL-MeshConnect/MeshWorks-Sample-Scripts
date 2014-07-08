####################################################
# MeshWorks Loopback/Range Test Remote Node Device
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
  
def buttonF():
    value = readDigital() 
    # on different value, send report 
    if (value != prevButtonValue):  
        sendDataReport(value, "button state")
    prevButtonValue = value 
  
# 2. reed switch on PB4  
reedSw = ["reedSw", "PB4", "digital", "reedSwF", 1] 
rsValues = ["discrete", 2, "no contact", "contact"] 
  
prevReedSwValue = 0 
  
def reedSwF():
    value = readDigital() 
    # on different value, send report 
    if (value != prevReedSwValue):  
        sendDataReport(value, "reedsw state")
    prevReedSwValue = value 

# When GW tells node to change LED state, ack back with same state
def cpCallbackVariableUpdate(variableName, value):
    if (variableName == "redLedState"):
        celPy.AdjustLocalControlPoint("redLed", value)
        celPy.setRemoteVariable("Gateway", "ackBack", value)


# Blink green LED every 2 seconds
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
celPy.ApplicationName = "Loopback Test"
celPy.DeviceName = "Node" 
celPy.IsSleepyDevice = False
celPy.DataCollectionPoints = [button, reedSw] 
celPy.DataCollectionValues = [bValues, rsValues]
celPy.ControlPoints = [greenLed, redLed, buzzer]
celPy.ControlValues = [greenValues, redValues, buzzerVal] 
  
def main(): 
    pass
