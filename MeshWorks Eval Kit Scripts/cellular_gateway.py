######################################################
# CEL MeshWorks Sample Script 
# Gateway with control and data points
######################################################
  
# green LED is on GPIO PA6
greenLed = ["greenLed", "PA6", "digital", "grLedF", 1]
greenValues = ["discrete", 2, "off", "on"]
  
# red LED is on GPIO PA7
redLed = ["redLed", "PA7", "digital", "rdLedF", 1]
redValues = ["discrete", 2, "off", "on"]
  
# button is on GPIO PB6 
buttonPoint = ["button", "PB6", "digital", "buttonF", 1]
buttonValues = ["discrete", 2, "up", "down"]
  
# reed switch is on GPIO PB4  
reedSwPoint = ["reedSw", "PB4", "digital", "reedSwF", 3]
reedSwValues = ["discrete", 2, "no contact", "contact"] 
  
# buzzer is on GPIO PB7 
buzzer = ["buzzer", "PB7", "PWM", "buzzerF", 1] 
buzzerVal = ["range", 1, 12, "tone"]  
  
# device configuration
celPy.ApplicationName = "MeshWorks"  
celPy.DeviceName = "Gateway"
celPy.IsSleepyDevice = False
celPy.DataCollectionPoints = [buttonPoint, reedSwPoint] 
celPy.DataCollectionValues = [buttonValues, reedSwValues] 
celPy.ControlPoints = [greenLed, redLed, buzzer]
celPy.ControlValues = [greenValues, redValues, buzzerVal] 
  
def cpCallbackDataPointMessageReceived(deviceName, datapointName, discreteValueString, rangeValue): 
    if (deviceName == "Sensor 1"):
        if (datapointName == "button"): 
            cloudUpdate("sens1btn", rangeValue) 
        if (datapointName == "reedSw"): 
            cloudUpdate("sens1reedsw", rangeValue) 
        if (datapointName == "tempSensor"): 
            cloudUpdate("sens1temp", rangeValue)
        if (datapointName == "humiditySensor"): 
            cloudUpdate("sens1hmdty", rangeValue) 
    if (deviceName == "Sensor 2"):
        if (datapointName == "button"): 
            cloudUpdate("sens2btn", rangeValue) 
        if (datapointName == "reedSw"): 
            cloudUpdate("sens2reedsw", rangeValue) 
        if (datapointName == "tempSensor"): 
            cloudUpdate("sens2temp", rangeValue)
        if (datapointName == "humiditySensor"): 
            cloudUpdate("sens2hmdty", rangeValue) 
  
# every half second 
celPy.addTickFunction(blinkLed, 5)
  
ledState = 0
  
# blink the green LED   
def blinkLed(): 
    if (ledState == 0): 
        celPy.AdjustLocalControlPoint("greenLed", 1)
        ledState = 1
        return
    if (ledState == 1): 
        celPy.AdjustLocalControlPoint("greenLed", 0)
        ledState = 0
  
# Define what executes once on power up or script start   
def main(): 
    print("execute MAIN function")
    #cloudInit("USER_CIK")
