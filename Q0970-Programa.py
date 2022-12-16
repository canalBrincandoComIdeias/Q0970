#     AUTOR:    BrincandoComIdeias
#     APRENDA:  https://cursodearduino.net/
#     SKETCH:   Fontes e Baterias para o Pico
#     DATA:     14/12/22

import machine
from utime import sleep as delay 

pinLED    = machine.Pin(17, machine.Pin.OUT)

while True:
    
    estado = pinLED.value()
    print(f"LED: {estado}     ", end='\r')
    
    delay(0.5) # delay de 1 seg.
    pinLED.toggle()
    