#     AUTOR:    BrincandoComIdeias
#     APRENDA:  https://cursodearduino.net/
#     SKETCH:   Meu primeiro Robo com Pico
#     DATA:     05/12/22

import machine
from utime import sleep as delay 

pinSensor = machine.ADC(28)
pinLED    = machine.Pin(25, machine.Pin.OUT)

# Equivalente a função map()
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    
    leitura = pinSensor.read_u16() # 0 ~ 65535
    tensao = map(leitura, 0, 65535, 0, 330)
    estado = pinLED.value()
    
    print(f"LED: {estado}     ", end='\r')
    pinLED.toggle()
    delay(0.5) # delay de 1 seg.
    