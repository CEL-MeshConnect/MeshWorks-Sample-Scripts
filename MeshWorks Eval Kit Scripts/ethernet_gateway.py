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
    if (deviceName == "Sensor 1"):
        if (datapointName == "button"):
            udpPayload = "cik="
            udpPayload = (udpPayload + cik) 
            udpPayload = (udpPayload + "&sens1btn=")
            udpPayload = (udpPayload + rangeValue)
            udp.send("m2.exosite.com", 18494, udpPayload) 
        if (datapointName == "reedSw"): 
            udpPayload = "cik="
            udpPayload = (udpPayload + cik)
            udpPayload = (udpPayload + "&sens1reedsw=") 
            udpPayload = (udpPayload + rangeValue)
            udp.send("m2.exosite.com", 18494, udpPayload) 
        if (datapointName == "tempSensor"): 
            udpPayload = "cik="
            udpPayload = (udpPayload + cik) 
            udpPayload = (udpPayload + "&sens1temp=") 
            udpPayload = (udpPayload + rangeValue)
            udp.send("m2.exosite.com", 18494, udpPayload) 
        if (datapointName == "humiditySensor"): 
            udpPayload = "cik="
            udpPayload = (udpPayload + cik) 
            udpPayload = (udpPayload + "&sens1hmdty=")
            udpPayload = (udpPayload + rangeValue)
            udp.send("m2.exosite.com", 18494, udpPayload) 
    if (deviceName == "Sensor 2"):
        if (datapointName == "button"): 
            udpPayload = "cik="
            udpPayload = (udpPayload + cik) 
            udpPayload = (udpPayload + "&sens2btn=")
            udpPayload = (udpPayload + rangeValue)
            udp.send("m2.exosite.com", 18494, udpPayload) 
        if (datapointName == "reedSw"): 
            udpPayload = "cik="
            udpPayload = (udpPayload + cik) 
            udpPayload = (udpPayload + "&sens2reedsw=") 
            udpPayload = (udpPayload + rangeValue)
            udp.send("m2.exosite.com", 18494, udpPayload) 
        if (datapointName == "tempSensor"): 
            udpPayload = "cik="
            udpPayload = (udpPayload + cik) 
            udpPayload = (udpPayload + "&sens2temp=") 
            udpPayload = (udpPayload + rangeValue)
            udp.send("m2.exosite.com", 18494, udpPayload) 
        if (datapointName == "humiditySensor"): 
            udpPayload = "cik="
            udpPayload = (udpPayload + cik) 
            udpPayload = (udpPayload + "&sens2hmdty=")
            udpPayload = (udpPayload + rangeValue)
            udp.send("m2.exosite.com", 18494, udpPayload) 
  
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
    cik = "[USER CIK GOES HERE]"
