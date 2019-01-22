import mysql.connector
import sys
from gpiozero import MotionSensor, LED
from time import sleep

pir = MotionSensor(14)
led2 = LED(2)
led3 = LED(3)
led4 = LED(4)
sensor = "C"

mydb = mysql.connector.connect(
    host="www.comercializadoralanacional.com.co",
    user="comerc10_us_eeed",
    passwd="2gI(3T+)N}Pr",
    database="comerc10_evaluateeneldeporte"
)
mydb.close()

def funcion1():
    led2.off()
    led3.on()
    
def funcion2():
    led2.on()
    led3.off()

def insert():
    try: 
        mydb.reconnect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO sensor ( posicion, idprueba, idpractica, idjugador ) "
        sql += "VALUES "
        sql += "( '" + sensor + "', "
        sql += "(SELECT idprueba FROM estado WHERE estado = 1), " 
        sql += "(SELECT idpractica FROM estado WHERE estado = 1), "
        sql += "(SELECT idjugador FROM estado WHERE estado = 1) )"
        mycursor.execute(sql)
        mydb.commit()
        
        led4.on()
        sleep(3)
        led4.off()
        mycursor.close()
        mydb.close()
    except mysql.connector.Error as e:
        mycursor.close()
        mydb.close()
        mydb.reconnect()
        
        sleep(3)
        print(e)
        return None
    
while True:
    try:
        led2.on()
        pir.wait_for_motion()
        pir.when_motion = funcion1()
            
        print("Movimiento detectado")
        pir.wait_for_no_motion()
        insert()
        pir.when_no_motion = funcion2()
    except (KeyboardInterrupt, SystemExit):
        led2.off()
        led3.off()
        led4.off()
        print("Salida")
        sys.exit()
