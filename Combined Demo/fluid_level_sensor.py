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
# 3 digital Data Points: button, Reed switch and ADC
  
# 1. button on PB6
button = ["button", "PB6", "digital", "buttonF", 1] 
bValues = ["discrete", 2, "up", "down"] 
  
# 2. reed switch on PB4 
reedSw = ["reedSw", "PB4", "digital", "reedSwF", 1] 
rsValues = ["discrete", 2, "no contact", "contact"] 
  
# 3. Level Sensor (ADC) on PB5  
lvlSens = ["lvlSens", "PB5", "analog", "lvlSensF", 1] 
lvlSensValues = ["range", 0, 1, "volts"]  

previousFluidLevel = 0
  
# Function to read level sensor 
def lvlSensF(): 
    # Get ADC voltage in 10ths of mV (0.1234V => 1234)
    value = readAnalog()
    # Convert from volts to inches
    value = (value - 10629) 
    value = (value / 657) 
    invert = (0 - 1)
    value = (value * invert)
    if (value != previousFluidLevel):
        sendDataReport(value, "inches") 
        celPy.setRemoteVariable("Display", "flevel", value)
    previousFluidLevel = value
  
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
celPy.DeviceName = "Level Sensor" 
celPy.IsSleepyDevice = False
celPy.DataCollectionPoints = [button, reedSw, lvlSens]
celPy.DataCollectionValues = [bValues, rsValues, lvlSensValues] 
celPy.ControlPoints = [greenLed, redLed, buzzer]
celPy.ControlValues = [greenValues, redValues, buzzerVal] 
  
def main(): 
    pass
  
