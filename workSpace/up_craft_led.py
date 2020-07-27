import time
import machine

#pin = machine.Pin(14, machine.Pin.OUT)
#pin2 = machine.Pin(16, machine.Pin.OUT)


pin2 = machine.Pin(2, machine.Pin.OUT) #create output pin on GPIO2


while 1:
  pin2.on()     #set pin to "on" (high) level
  time.sleep(1) # sleep for 1 second
  print(pin2.value()) #we can check if the pin is high/low
  
	pin2.off()    #set pin to "off" (low) level
  print(pin2.value())
  time.sleep(1) # sleep for 1 second
