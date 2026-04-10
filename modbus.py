import serial
import time

def envoyer_trame(port, baudrate, requete):
    ser = serial.Serial(port, baudrate, timeout=1)
    ser.write(requete)
    time.sleep(0.1)
    reponse = ser.read(15)
    print(reponse.hex())
    return reponse.hex()
tt