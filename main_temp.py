import machine
import utime

sensorTemperatura = machine.ADC(4)
factorConversion = 3.3/65535

while True:
    lectura = sensorTemperatura.read_u16()*factorConversion
    temp = round(27(lectura-0.706)/0.001721,2)
    print("La temperatura actual es de: ",temp)
    utime.sleep(0.1)