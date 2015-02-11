########################################
# MeshWorks Development Kit
# 2lemetry Gateway script
########################################

celPy.ApplicationName = "MeshWorks"
celPy.DeviceName = "Gateway"
celPy.IsSleepyDevice = False

# Button to connect to 2lemetry  
buttonPoint = ["button", "PA3", "digital", "buttonF", 1]
buttonValues = ["discrete", 2, "up", "down"]
celPy.DataCollectionPoints = [buttonPoint]  
celPy.DataCollectionValues = [buttonValues] 
celPy.ControlPoints = []
celPy.ControlValues = []  
  
def buttonF():
    value = readDigital() 
    if (value == 1):
        if (bConnected == 0): 
            tcpPayload = x"1065"
            tcpPayload = (tcpPayload + x"0006") 
            tcpPayload = (tcpPayload + "MQIsdp")
            tcpPayload = (tcpPayload + x"03c200b4") 
            tcpPayload = (tcpPayload + x"000f") 
            tcpPayload = (tcpPayload + "MidwayGateway01") 
            tcpPayload = (tcpPayload + x"0024") 
            tcpPayload = (tcpPayload + username)
            tcpPayload = (tcpPayload + x"0020") 
            tcpPayload = (tcpPayload + md5secret)
            print("tcp send [%s]", tcpPayload)
            tcp.send("q.m2m.io", 1883, tcpPayload)
  
def cpCallbackTcpReceived(type, ip, srcPort, dstPort, data):
    print("RX TCP from %s", ip) 
    print("    src port %d", srcPort) 
    print("    dst port %d", dstPort)
    print("    data string: %s", data)
    resp = string.find(data, x"2002")
    print("    response: %d", resp)
    if (resp == 0):
        bConnected = 1
        print("    Connect SUCCESS!")

def cpCallbackDataPointMessageReceived(deviceName, datapointName, discreteValueString, rangeValue): 
    if (bConnected == 1):
        if (datapointName == "button"): 
            print("Button report received from %s", deviceName) 
            tcpPayload = x"323e001f" 
            tcpPayload = (tcpPayload + project) 
            tcpPayload = (tcpPayload + "/simulators/sim1")
            tcpPayload = (tcpPayload + x"0001") 
            tcpPayload = (tcpPayload + x"7b22") 
            tcpPayload = (tcpPayload + deviceName)
            tcpPayload = (tcpPayload + x"223a7b22") 
            tcpPayload = (tcpPayload + "button")
            tcpPayload = (tcpPayload + x"223a22") 
            tcpPayload = (tcpPayload + rangeValue)  
            tcpPayload = (tcpPayload +  x"227d7d")
            print("tcp send [%s]", tcpPayload)
            tcp.send("q.m2m.io", 1883, tcpPayload)
        if (datapointName == "reedSw"): 
            print("Reed switch report received from %s", deviceName) 
            tcpPayload = x"3243001f" 
            tcpPayload = (tcpPayload + project) 
            tcpPayload = (tcpPayload + "/simulators/sim1")
            tcpPayload = (tcpPayload + x"0001") 
            tcpPayload = (tcpPayload + x"7b22") 
            tcpPayload = (tcpPayload + deviceName)
            tcpPayload = (tcpPayload + x"223a7b22") 
            tcpPayload = (tcpPayload + "reed switch")
            tcpPayload = (tcpPayload + x"223a22") 
            tcpPayload = (tcpPayload + rangeValue)  
            tcpPayload = (tcpPayload +  x"227d7d")
            print("tcp send [%s]", tcpPayload)
            tcp.send("q.m2m.io", 1883, tcpPayload)            
        if (datapointName == "tempSensor"): 
            print("Temperature report received from %s", deviceName)
            tcpPayload = x"3244001f" 
            tcpPayload = (tcpPayload + project) 
            tcpPayload = (tcpPayload + "/simulators/sim1")
            tcpPayload = (tcpPayload + x"0001") 
            tcpPayload = (tcpPayload + x"7b22") 
            tcpPayload = (tcpPayload + deviceName)
            tcpPayload = (tcpPayload + x"223a7b22") 
            tcpPayload = (tcpPayload + "temperature")
            tcpPayload = (tcpPayload + x"223a22") 
            tcpPayload = (tcpPayload + rangeValue)  
            tcpPayload = (tcpPayload +  x"227d7d")
            print("tcp send [%s]", tcpPayload)
            tcp.send("q.m2m.io", 1883, tcpPayload)
        if (datapointName == "humiditySensor"): 
            print("Humidity report received from %s", deviceName) 
            tcpPayload = x"3240001f" 
            tcpPayload = (tcpPayload + project) 
            tcpPayload = (tcpPayload + "/simulators/sim1")
            tcpPayload = (tcpPayload + x"0001") 
            tcpPayload = (tcpPayload + x"7b22") 
            tcpPayload = (tcpPayload + deviceName)
            tcpPayload = (tcpPayload + x"223a7b22") 
            tcpPayload = (tcpPayload + "humidty")
            tcpPayload = (tcpPayload + x"223a22") 
            tcpPayload = (tcpPayload + rangeValue)  
            tcpPayload = (tcpPayload +  x"227d7d")
            print("tcp send [%s]", tcpPayload)
            tcp.send("q.m2m.io", 1883, tcpPayload)

celPy.addTickFunction(ping2lemetry, 200)

def ping2lemetry():
    if(bConnected == 1):
        # send a ping every 20 seconds to keep session alive when not publishing
        tcpPayload = x"c000"
        tcp.send("q.m2m.io", 1883, tcpPayload)

def main(): 
    # Connect to 2lemetry 
    bConnected = 0
    # The follow variables are unique to each project and
    # can be found on the projects Credentials page
    project = "om4rakpxjdwsdho"
    username = "489d6d62-e94d-4c9b-8dba-619a4e840cef"
    md5secret = "e3b5cda38dae68a96e4f36b7eb383a9c"
    tcpPayload = x"1065"
    tcpPayload = (tcpPayload + x"0006") 
    tcpPayload = (tcpPayload + "MQIsdp")
    tcpPayload = (tcpPayload + x"03c200b4") 
    tcpPayload = (tcpPayload + x"000f") 
    tcpPayload = (tcpPayload + "MidwayGateway01") 
    tcpPayload = (tcpPayload + x"0024") 
    tcpPayload = (tcpPayload + username)
    tcpPayload = (tcpPayload + x"0020") 
    tcpPayload = (tcpPayload + md5secret)
    print("tcp send [%s]", tcpPayload)
    tcp.send("q.m2m.io", 1883, tcpPayload)
