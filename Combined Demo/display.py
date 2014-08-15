####################################################
# Wireless LED Matrix Display Script  
  
####################################################
# we have 4 Control Points: 2 LEDs, 1 PWM buzzer and an LED display 
  
# 1. green LED input is PA6 
greenLed = ["greenLed", "PA6", "digital", "grLedF", 1]
greenValues = ["discrete", 2, "off", "on"]
  
# 2. red LED input is PA7 
redLed = ["redLed", "PA7", "digital", "rdLedF", 1]
redValues = ["discrete", 2, "off", "on"]
  
# 3. buzzer input on PB7  
buzzer = ["buzzer", "PB7", "PWM", "buzzerF", 1] 
buzzerVal = ["range", 1, 12, "tone"]  
  
# 4. I2C LED Matrix Display 
matrixDisplay = ["matrixDisplay", "PA1", "i2c", "matrixDisplayF", 1]
matrixDisplayValues = ["range", 0, 65535] 
  
rightDisplay = 0x70 
leftDisplay = 0x72
onesDigit = 0 
tensDigit = 0 
  
celPy.addTickFunction(leftDisplayTick, 5) 
  
def leftDisplayTick():
    if (tensDigit == 0):
        writeI2c(leftDisplay, 0x3F, 0x00) 
        writeI2c(leftDisplay, 0xFF, 0x02) 
        writeI2c(leftDisplay, 0xC2, 0x04) 
        writeI2c(leftDisplay, 0xC4, 0x06) 
        writeI2c(leftDisplay, 0xC8, 0x08) 
        writeI2c(leftDisplay, 0xD0, 0x0A) 
        writeI2c(leftDisplay, 0xFF, 0x0C) 
        writeI2c(leftDisplay, 0x3F, 0x0E) 
    if (tensDigit == 1):
        writeI2c(leftDisplay, 0x00, 0x00) 
        writeI2c(leftDisplay, 0x80, 0x02) 
        writeI2c(leftDisplay, 0xB0, 0x04) 
        writeI2c(leftDisplay, 0xFF, 0x06) 
        writeI2c(leftDisplay, 0xFF, 0x08) 
        writeI2c(leftDisplay, 0x80, 0x0A) 
        writeI2c(leftDisplay, 0x80, 0x0C) 
        writeI2c(leftDisplay, 0x00, 0x0E) 
    if (tensDigit == 2):
        writeI2c(leftDisplay, 0xA1, 0x00) 
        writeI2c(leftDisplay, 0xE3, 0x02) 
        writeI2c(leftDisplay, 0xC2, 0x04) 
        writeI2c(leftDisplay, 0xC6, 0x06) 
        writeI2c(leftDisplay, 0xC4, 0x08) 
        writeI2c(leftDisplay, 0xEC, 0x0A) 
        writeI2c(leftDisplay, 0xF9, 0x0C) 
        writeI2c(leftDisplay, 0xB1, 0x0E) 
    if (tensDigit == 3):
        writeI2c(leftDisplay, 0x21, 0x00) 
        writeI2c(leftDisplay, 0xE1, 0x02) 
        writeI2c(leftDisplay, 0xC4, 0x04) 
        writeI2c(leftDisplay, 0xCC, 0x06) 
        writeI2c(leftDisplay, 0xCC, 0x08) 
        writeI2c(leftDisplay, 0xCC, 0x0A) 
        writeI2c(leftDisplay, 0xFF, 0x0C) 
        writeI2c(leftDisplay, 0x3B, 0x0E) 
    if (tensDigit == 4):
        writeI2c(leftDisplay, 0x7C, 0x00) 
        writeI2c(leftDisplay, 0x7C, 0x02) 
        writeI2c(leftDisplay, 0x0C, 0x04) 
        writeI2c(leftDisplay, 0x0C, 0x06) 
        writeI2c(leftDisplay, 0x0C, 0x08) 
        writeI2c(leftDisplay, 0xFF, 0x0A) 
        writeI2c(leftDisplay, 0xFF, 0x0C) 
        writeI2c(leftDisplay, 0x0C, 0x0E) 
    if (tensDigit == 5):
        writeI2c(leftDisplay, 0x79, 0x00) 
        writeI2c(leftDisplay, 0xF9, 0x02) 
        writeI2c(leftDisplay, 0xC8, 0x04) 
        writeI2c(leftDisplay, 0xC8, 0x06) 
        writeI2c(leftDisplay, 0xC8, 0x08) 
        writeI2c(leftDisplay, 0xCD, 0x0A) 
        writeI2c(leftDisplay, 0xCF, 0x0C) 
        writeI2c(leftDisplay, 0x47, 0x0E) 
    if (tensDigit == 6):
        writeI2c(leftDisplay, 0x37, 0x00) 
        writeI2c(leftDisplay, 0xFF, 0x02) 
        writeI2c(leftDisplay, 0xC8, 0x04) 
        writeI2c(leftDisplay, 0xC8, 0x06) 
        writeI2c(leftDisplay, 0xC8, 0x08) 
        writeI2c(leftDisplay, 0xC8, 0x0A) 
        writeI2c(leftDisplay, 0xCF, 0x0C) 
        writeI2c(leftDisplay, 0x07, 0x0E) 
    if (tensDigit == 7):
        writeI2c(leftDisplay, 0x60, 0x00) 
        writeI2c(leftDisplay, 0x60, 0x02) 
        writeI2c(leftDisplay, 0x40, 0x04) 
        writeI2c(leftDisplay, 0xC7, 0x06) 
        writeI2c(leftDisplay, 0xCF, 0x08) 
        writeI2c(leftDisplay, 0x58, 0x0A) 
        writeI2c(leftDisplay, 0x70, 0x0C) 
        writeI2c(leftDisplay, 0x60, 0x0E) 
    if (tensDigit == 8):
        writeI2c(leftDisplay, 0x37, 0x00) 
        writeI2c(leftDisplay, 0xFD, 0x02) 
        writeI2c(leftDisplay, 0xC8, 0x04) 
        writeI2c(leftDisplay, 0xC8, 0x06) 
        writeI2c(leftDisplay, 0xC8, 0x08) 
        writeI2c(leftDisplay, 0xC8, 0x0A) 
        writeI2c(leftDisplay, 0xFD, 0x0C) 
        writeI2c(leftDisplay, 0x37, 0x0E) 
    if (tensDigit == 9):
        writeI2c(leftDisplay, 0x38, 0x00) 
        writeI2c(leftDisplay, 0xFC, 0x02) 
        writeI2c(leftDisplay, 0xC4, 0x04) 
        writeI2c(leftDisplay, 0xC4, 0x06) 
        writeI2c(leftDisplay, 0xC4, 0x08) 
        writeI2c(leftDisplay, 0xC4, 0x0A) 
        writeI2c(leftDisplay, 0xFF, 0x0C) 
        writeI2c(leftDisplay, 0x3B, 0x0E) 
  
celPy.addTickFunction(rightDisplayTick, 5)
  
def rightDisplayTick(): 
    if (onesDigit == 0):
        writeI2c(rightDisplay, 0x3F, 0x00)
        writeI2c(rightDisplay, 0xFF, 0x02)
        writeI2c(rightDisplay, 0xC2, 0x04)
        writeI2c(rightDisplay, 0xC4, 0x06)
        writeI2c(rightDisplay, 0xC8, 0x08)
        writeI2c(rightDisplay, 0xD0, 0x0A)
        writeI2c(rightDisplay, 0xFF, 0x0C)
        writeI2c(rightDisplay, 0x3F, 0x0E)
    if (onesDigit == 1):
        writeI2c(rightDisplay, 0x00, 0x00)
        writeI2c(rightDisplay, 0x80, 0x02)
        writeI2c(rightDisplay, 0xB0, 0x04)
        writeI2c(rightDisplay, 0xFF, 0x06)
        writeI2c(rightDisplay, 0xFF, 0x08)
        writeI2c(rightDisplay, 0x80, 0x0A)
        writeI2c(rightDisplay, 0x80, 0x0C)
        writeI2c(rightDisplay, 0x00, 0x0E)
    if (onesDigit == 2):
        writeI2c(rightDisplay, 0xA1, 0x00)
        writeI2c(rightDisplay, 0xE3, 0x02)
        writeI2c(rightDisplay, 0xC2, 0x04)
        writeI2c(rightDisplay, 0xC6, 0x06)
        writeI2c(rightDisplay, 0xC4, 0x08)
        writeI2c(rightDisplay, 0xEC, 0x0A)
        writeI2c(rightDisplay, 0xF9, 0x0C)
        writeI2c(rightDisplay, 0xB1, 0x0E)
    if (onesDigit == 3):
        writeI2c(rightDisplay, 0x21, 0x00)
        writeI2c(rightDisplay, 0xE1, 0x02)
        writeI2c(rightDisplay, 0xC4, 0x04)
        writeI2c(rightDisplay, 0xCC, 0x06)
        writeI2c(rightDisplay, 0xCC, 0x08)
        writeI2c(rightDisplay, 0xCC, 0x0A)
        writeI2c(rightDisplay, 0xFF, 0x0C)
        writeI2c(rightDisplay, 0x3B, 0x0E)
    if (onesDigit == 4):
        writeI2c(rightDisplay, 0x7C, 0x00)
        writeI2c(rightDisplay, 0x7C, 0x02)
        writeI2c(rightDisplay, 0x0C, 0x04)
        writeI2c(rightDisplay, 0x0C, 0x06)
        writeI2c(rightDisplay, 0x0C, 0x08)
        writeI2c(rightDisplay, 0xFF, 0x0A)
        writeI2c(rightDisplay, 0xFF, 0x0C)
        writeI2c(rightDisplay, 0x0C, 0x0E)
    if (onesDigit == 5):
        writeI2c(rightDisplay, 0x79, 0x00)
        writeI2c(rightDisplay, 0xF9, 0x02)
        writeI2c(rightDisplay, 0xC8, 0x04)
        writeI2c(rightDisplay, 0xC8, 0x06)
        writeI2c(rightDisplay, 0xC8, 0x08)
        writeI2c(rightDisplay, 0xCD, 0x0A)
        writeI2c(rightDisplay, 0xCF, 0x0C)
        writeI2c(rightDisplay, 0x47, 0x0E)
    if (onesDigit == 6):
        writeI2c(rightDisplay, 0x37, 0x00)
        writeI2c(rightDisplay, 0xFF, 0x02)
        writeI2c(rightDisplay, 0xC8, 0x04)
        writeI2c(rightDisplay, 0xC8, 0x06)
        writeI2c(rightDisplay, 0xC8, 0x08)
        writeI2c(rightDisplay, 0xC8, 0x0A)
        writeI2c(rightDisplay, 0xCF, 0x0C)
        writeI2c(rightDisplay, 0x07, 0x0E)
    if (onesDigit == 7):
        writeI2c(rightDisplay, 0x60, 0x00)
        writeI2c(rightDisplay, 0x60, 0x02)
        writeI2c(rightDisplay, 0x40, 0x04)
        writeI2c(rightDisplay, 0xC7, 0x06)
        writeI2c(rightDisplay, 0xCF, 0x08)
        writeI2c(rightDisplay, 0x58, 0x0A)
        writeI2c(rightDisplay, 0x70, 0x0C)
        writeI2c(rightDisplay, 0x60, 0x0E)
    if (onesDigit == 8):
        writeI2c(rightDisplay, 0x37, 0x00)
        writeI2c(rightDisplay, 0xFD, 0x02)
        writeI2c(rightDisplay, 0xC8, 0x04)
        writeI2c(rightDisplay, 0xC8, 0x06)
        writeI2c(rightDisplay, 0xC8, 0x08)
        writeI2c(rightDisplay, 0xC8, 0x0A)
        writeI2c(rightDisplay, 0xFD, 0x0C)
        writeI2c(rightDisplay, 0x37, 0x0E)
    if (onesDigit == 9):
        writeI2c(rightDisplay, 0x38, 0x00)
        writeI2c(rightDisplay, 0xFC, 0x02)
        writeI2c(rightDisplay, 0xC4, 0x04)
        writeI2c(rightDisplay, 0xC4, 0x06)
        writeI2c(rightDisplay, 0xC4, 0x08)
        writeI2c(rightDisplay, 0xC4, 0x0A)
        writeI2c(rightDisplay, 0xFF, 0x0C)
        writeI2c(rightDisplay, 0x3B, 0x0E)
  
####################################################
# 3 digital Data Points: button, Reed switch and ADC
  
# 1. button on PB6
button = ["button", "PB6", "digital", "buttonF", 1] 
bValues = ["discrete", 2, "up", "down"] 
  
prevButtonValue = 0 
  
def buttonF():
    value = readDigital() 
    # on different value, send report 
    if (value != prevButtonValue):  
        if (value == 1):
            print("Button pressed")
    prevButtonValue = value 
     
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

def cpCallbackVariableUpdate(variableName, value):
    if (variableName == "flevel"):
        tensDigit = (value / 10) 
        tempValue = (tensDigit * 10)
        onesDigit = (value - tempValue)
  
####################################################
# device configuration
celPy.ApplicationName = "MeshWorks"  
celPy.DeviceName = "Display"  
celPy.IsSleepyDevice = False
celPy.DataCollectionPoints = [button] 
celPy.DataCollectionValues = [bValues]  
celPy.ControlPoints = [greenLed, redLed, buzzer, matrixDisplay]  
celPy.ControlValues = [greenValues, redValues, buzzerVal, matrixDisplayValues]   
  
def main(): 
    displayValue = 0
    # Enable display oscillator 
    writeI2c(leftDisplay, 0x00, 0x21) 
    writeI2c(rightDisplay, 0x00, 0x21)
    # Clear all rows display
    writeI2c(leftDisplay, 0x00, 0x00) 
    writeI2c(leftDisplay, 0xFF, 0x02) 
    writeI2c(leftDisplay, 0x00, 0x04) 
    writeI2c(leftDisplay, 0xFF, 0x06) 
    writeI2c(leftDisplay, 0x00, 0x08) 
    writeI2c(leftDisplay, 0xFF, 0x0A) 
    writeI2c(leftDisplay, 0x00, 0x0C) 
    writeI2c(leftDisplay, 0xFF, 0x0E) 
    writeI2c(rightDisplay, 0xFF, 0x00)
    writeI2c(rightDisplay, 0x00, 0x02)
    writeI2c(rightDisplay, 0xFF, 0x04)
    writeI2c(rightDisplay, 0x00, 0x06)
    writeI2c(rightDisplay, 0xFF, 0x08)
    writeI2c(rightDisplay, 0x00, 0x0A)
    writeI2c(rightDisplay, 0xFF, 0x0C)
    writeI2c(rightDisplay, 0x00, 0x0E)
    # Set Dimming to 4/16 duty
    writeI2c(leftDisplay, 0x00, 0xEF) 
    writeI2c(rightDisplay, 0x00, 0xEF)
    # Turn on display 
    writeI2c(leftDisplay, 0x00, 0x81) 
    writeI2c(rightDisplay, 0x00, 0x81)
