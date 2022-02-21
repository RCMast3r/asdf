import serial
import syslog
import time
from curtsies import Input
port ='/dev/ttyACM0'

ard=serial.Serial(port,9600,timeout=5)



while True:
    x=ard.read(ard.inWaiting())
    
    time.sleep(.002)
    
    
    with Input(keynames='curses') as input_generator:
        if(input_generator=='q'):
            try:
                print(x[-1])
            except:
                continue
        
ard.close()