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
  
# button is on GPIO PA3 
buttonPoint = ["button", "PA3", "digital", "buttonF", 1]
buttonValues = ["discrete", 2, "up", "down"]
  
# device configuration
celPy.ApplicationName = "MeshWorks"   
celPy.DeviceName = "Gateway"
celPy.IsSleepyDevice = False
celPy.DataCollectionPoints = [buttonPoint]  
celPy.DataCollectionValues = [buttonValues] 
celPy.ControlPoints = [greenLed, redLed]
celPy.ControlValues = [greenValues, redValues]  
  
def cpCallbackDataPointMessageReceived(deviceName, datapointName, discreteValueString, rangeValue): 
    if (deviceName == "Terrarium"):
        if (datapointName == "reedSw"):
            if (discreteValueString == "contact"):
                lidtState = 1
            if (discreteValueString == "no contact"):
                lidtState = 0
            udpPayload = "cik="
            udpPayload = (udpPayload + cik)
            udpPayload = (udpPayload + "&lid=") 
            udpPayload = (udpPayload + lidtState)
            udp.send("m2.exosite.com", 18494, udpPayload) 
        if (datapointName == "tempSensor"): 
            udpPayload = "cik="
            udpPayload = (udpPayload + cik) 
            udpPayload = (udpPayload + "&temp=") 
            udpPayload = (udpPayload + rangeValue)
            udp.send("m2.exosite.com", 18494, udpPayload) 
        if (datapointName == "humiditySensor"): 
            udpPayload = "cik="
            udpPayload = (udpPayload + cik) 
            udpPayload = (udpPayload + "&humidity=")
            udpPayload = (udpPayload + rangeValue)
            udp.send("m2.exosite.com", 18494, udpPayload) 
    if (deviceName == "Level Sensor"):
        if (datapointName == "lvlSens"): 
            udpPayload = "cik="
            udpPayload = (udpPayload + cik) 
            udpPayload = (udpPayload + "&flvl=")
            udpPayload = (udpPayload + rangeValue)
            udp.send("m2.exosite.com", 18494, udpPayload) 

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
    cik = "USER_CIK"
