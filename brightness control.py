from machine import ADC,Pin
from utime import sleep

potPin = 35
pot = ADC (Pin(potPin))
pot.width(ADC.WIDTH_12BIT)
pot.atten(ADC.ATTN_11DB)

b = Pin(25,Pin.OUT)
b1 = Pin(14,Pin.OUT)
g = Pin(26,Pin.OUT)
y1 = Pin(12,Pin.OUT)
r = Pin(27,Pin.OUT)
r1 = Pin(13,Pin.OUT)

while True:

    potValue = pot.read()
    print("POT value =", potValue)
    
    
    if (potValue <= 500 ):
     b1.value(0)
     y1.value(0)
     r1.value(1)
     b.value(0)
     y.value(0)
     r.value(1)
     sleep(1)
     
    elif (potValue <= 1000):
    
         b1.value(0)
         y1.value(1)
         r1.value(0)
         b.value(0)
         y.value(1)
         r.value(0)
         sleep(1)
     
    elif (potValue <= 1500):
    
         b1.value(0)
         y1.value(1)
         r1.value(1)
         b.value(0)
         y.value(1)
         r.value(1)
         sleep(1)
     
    elif (potValue <= 2000):
        
         b1.value(1)
         y1.value(0)
         r1.value(0)
         b.value(1)
         y.value(0)
         r.value(0)
         sleep(1)
     
    elif (potValue <= 2500):
        
         b1.value(1)
         y1.value(0)
         r1.value(1)
         b.value(1)
         y.value(0)
         r.value(1)
         sleep(1) 
    elif (potValue <= 3000):
    
         b1.value(1)
         y1.value(1)
         r1.value(0)
         b.value(1)
         y.value(1)
         r.value(0)
         sleep(1)
     
    elif (potValue <= 3500):
    
         b1.value(1)
         y1.value(1)
         r1.value(1)
         b.value(1)
         y.value(1)
         r.value(1)
         sleep(1)
    
    else:
    
     b1.value(0)
     y1.value(0)
     r1.value(0)
     b.value(0)
     y.value(0)
     r.value(0)
     sleep(1)
   