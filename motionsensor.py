from gpiozero import MotionSensor, LED
from time import sleep
import mysql.connector

pir = MotionSensor(4)
led2 = LED(2)
led3 = LED(3)
led4 = LED(4)

mydb = mysql.connector.connect(
    host="www.comercializadoralanacional.com.co",
    user="comerc10_us_eeed",
    passwd="2gI(3T+)N}Pr",
    database="comerc10_evaluateeneldeporte"
)

mycursor = mydb.cursor()

def funcion1():
    led2.off()
    led3.on()
    
def funcion2():
    led2.on()
    led3.off()

def insert():
    sql = "INSERT INTO sensor (posicion) VALUES (%s)"
    val = ("A")
    mycursor.execute(sql, val)
    mydb.commit()
    led4.on()
    sleep(5)
    led4.off()

while True:
    led2.on()
    pir.wait_for_motion()
    pir.when_motion = funcion1()
        
    print("Movimiento detectado")
    pir.wait_for_no_motion()
    insert()
    pir.when_no_motion = funcion2()
