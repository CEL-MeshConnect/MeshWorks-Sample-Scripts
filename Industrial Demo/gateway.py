      
# Gateway with control and data points
# green LED input is PA6
greenLed = ["greenLed", "PA6", "digital", "grLedF", 1]
greenValues = ["discrete", 2, "off", "on"]
  
# red LED input is PA7
redLed = ["redLed", "PA7", "digital", "rdLedF", 1]
redValues = ["discrete", 2, "off", "on"]
  
# button output on PB6
buttonPoint = ["button", "PB6", "digital", "buttonF", 1]
buttonValues = ["discrete", 2, "up", "down"]
  
# reed switch output on PB4 
reedSwPoint = ["reedSw", "PB4", "digital", "reedSwF", 3]
reedSwValues = ["discrete", 2, "no contact", "contact"] 
  
# buzzer input on PB7 
buzzer = ["buzzer", "PB7", "PWM", "buzzerF", 1] 
buzzerVal = ["range", 1, 12, "tone"]  
  
# I2C temp sensor and I2C light sensor on PA1, PA2
  
buttonPressCount = 0
reedSwitchContactCount = 0
  
# device configuration
celPy.ApplicationName = "Industrial Demo"  
celPy.DeviceName = "Gateway"
celPy.IsSleepyDevice = False
celPy.DataCollectionPoints = [buttonPoint, reedSwPoint] 
celPy.DataCollectionValues = [buttonValues, reedSwValues] 
celPy.ControlPoints = [greenLed, redLed, buzzer]
celPy.ControlValues = [greenValues, redValues, buzzerVal] 
  
def cpCallbackDataPointMessageReceived(deviceName, datapointName, discreteValueString, rangeValue):
    if (deviceName == "Level Sensor"):
        if (datapointName == "lvlSens"): 
            cloudUpdate("flvl", rangeValue) 
  
# every half second 
celPy.addTickFunction(blinkLed, 5)
  
ledState = 0
  
def blinkLed(): 
    if (ledState == 0): 
        celPy.AdjustLocalControlPoint("greenLed", 1)
        ledState = 1
        return
    if (ledState == 1): 
        celPy.AdjustLocalControlPoint("greenLed", 0)
        ledState = 0
      
def main(): 
    cloudInit("b24848596e9e8a67a3b3ed9451e843f63d5dbf01") 
  
