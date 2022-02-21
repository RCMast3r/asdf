import serial
import syslog
import time
from curtsies import Input
port ='/dev/ttyACM0'

ard=serial.Serial(port,9600,timeout=5)




def main():
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            #print(repr(e))
            #print(type(e))
            b=bytes(e,'utf-8')
            #print(b)
            ard.write(b)
            time.sleep(.002)
            x=ard.read(ard.inWaiting())
    
            time.sleep(.002)
    

            try:
                print((x[-1])*(1024/255))
            except:
                continue
        


if __name__ == '__main__':
    main()