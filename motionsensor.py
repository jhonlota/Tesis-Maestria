from gpiozero import MotionSensor, LED
from time import sleep

pir = MotionSensor(4)
led1 = LED(2)
led2 = LED(15)

def funcion1():
    led1.off()
    led2.on()
    
def funcion2():
    led1.on()
    led2.off()

while True:
    led1.on()
    pir.wait_for_motion()
    pir.when_motion = funcion1()
        
    print("Movimiento detectado")
    pir.wait_for_no_motion()
    sleep(5)    
    pir.when_no_motion = funcion2()
