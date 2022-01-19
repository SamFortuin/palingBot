#print slow from sabastion on stackoverflow, good lad
from string import ascii_lowercase
from serial import Serial, SerialException
from time import sleep
from sys import stdout
from os import system

def comScan(checkRange,bluetooth=False,debugMode=False): #checks all open ports, returns the first
    bluetoothPorts = [3,4] #*change if your bluetooth ports are different
    debug,output = [],[] #empty lists
    for i in range(checkRange):
        if i+1 in bluetoothPorts and bluetooth:
            pass
        else:
            port = f'COM{i+1}'
            try:
                serial_port = Serial(port=port, baudrate=115200, timeout=1)
            except SerialException as e:
                debug.append("could not open serial port '{}': {}".format(port, e))
            else:
                output.append(port)
                debug.append("serial port {port} is open and not busy.")
                serial_port.close()

    if debugMode:
        print(*debug,sep='\n') #use if debug is True
    if len(output) > 0:
        return output[0] #returns first available port
    else:
        print("Could not find any COM ports")
        exit() #exits because code falls apart if there is no COM port.
        #scorched earth type beat. kinda. not really.


def slowPrint(str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(0.04)
   
#clears screen after given time
def clearScreen(sleepTime):
    sleep(sleepTime)
    system("cls")

def invalidInput(text='\ninvalid input, exeting program',delay=0.2):
    print(text)
    sleep(delay)
    exit()

def listPrint(List,delay=False):
    roomCount = len(List)
    for i in range(roomCount):
        if delay:
            sleep(0.12)
        print(List[i])

def intConvert(num):
    numConvert2 = True
    alphabet = list(ascii_lowercase) #makes list of the alphabet
    for i in range(10):
        if str(i) in num:
            numConvert1 = True
    for x in range(26):
        if alphabet[x] in num:
            numConvert2 = False
    if numConvert1 == True and numConvert2 == True: #if there are no letters but are numbers it returns the input as an int
        return int(num)
    else:
        print('Niet een getal.')
        exit()