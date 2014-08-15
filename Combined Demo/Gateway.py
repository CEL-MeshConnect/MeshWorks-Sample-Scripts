      
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
celPy.ApplicationName = "MeshWorks"  
celPy.DeviceName = "Gateway"
celPy.IsSleepyDevice = False
celPy.DataCollectionPoints = [buttonPoint, reedSwPoint] 
celPy.DataCollectionValues = [buttonValues, reedSwValues] 
celPy.ControlPoints = [greenLed, redLed, buzzer]
celPy.ControlValues = [greenValues, redValues, buzzerVal] 
  
def cpCallbackDataPointMessageReceived(deviceName, datapointName, discreteValueString, rangeValue): 
    if (deviceName == "Terrarium"): 
        if (datapointName == "tempSensor"): 
            cloudUpdate("temp", rangeValue) 
        if (datapointName == "humiditySensor"): 
            cloudUpdate("humidity", rangeValue) 
        if (datapointName == "reedSw"):
            if (discreteValueString == "contact"):
                lidtState = 1
            if (discreteValueString == "no contact"):
                lidtState = 0
            cloudUpdate("lid", lidtState)
        return
    if (deviceName == "Level Sensor"):
        if (datapointName == "lvlSens"): 
            cloudUpdate("flvl", rangeValue)

def cpCallbackVariableUpdate(variableName, value):
    if (variableName == "lockStatus"):
        cloudUpdate("lkbx", value) 

# Check for lockout override ever 20 seconds
celPy.addTickFunction(pollCloudForUpdate, 200)

def pollCloudForUpdate():
    cloudSubscribe("lkbx", "Lockout Box", "lockOnOff")
  
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
    
# check buzzer every 5 seconds - turn it off
celPy.addTickFunction(checkBuzzer, 50)
def checkBuzzer():
    celPy.AdjustLocalControlPoint("buzzer", 0)  
  
def main(): 
    print("execute MAIN function")
    cloudInit("b48c8d4c39c9c85493ad07b44d736ef9b0bdbaa4") 
  
