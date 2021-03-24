from sense_emu import SenseHat
import time
sense = SenseHat()

def medida():       
        temp= sense.temp 
        pre =sense.pressure
        hum= sense.humidity
        medidas=[temp, pre, hum]
        #print(medidas)
        return medidas