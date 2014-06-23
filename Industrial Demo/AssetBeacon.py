####################################################
# 1. red LED on PA7 
led = ["led", "PA7", "digital", "ledF", 1]
ledValues = ["discrete", 2, "off", "on"]
  
# 2. green LED on PA6 
heartLed = ["heartLed", "PA6", "digital", "heartLedF", 1] 
heartLedValues = ["discrete", 2, "off", "on"] 
  
####################################################
# device configuration
celPy.ApplicationName = "Industrial Demo"   
celPy.DeviceName = "Asset Beacon"   
celPy.IsSleepyDevice = False
celPy.ControlPoints = [led, heartLed]   
celPy.ControlValues = [ledValues, heartLedValues] 
  
celPy.addTickFunction(heartbeatLed, 20) 
  
ledState = 0
  
def heartbeatLed(): 
    if (ledState == 0): 
        celPy.AdjustLocalControlPoint("heartLed", 1)
        celPy.AdjustLocalControlPoint("led", 1)
        ledState = 1
        return
    if (ledState == 1): 
        celPy.AdjustLocalControlPoint("heartLed", 0)
        celPy.AdjustLocalControlPoint("led", 0)
        ledState = 0
  
def main(): 
    pass  
