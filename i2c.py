import smbus
from time import sleep
import pigpio





# Configure ADC on pin 32
soil_moisture = ADC(Pin(32))
soil_moisture.atten(ADC.ATTN_11DB)  # Set attenuation for full 0-3.3V range

# Calibration values (adjust these based on actual readings)
DRY_VALUE = 4095   # Sensor value in dry air
WET_VALUE = 3805 

class MCP3021:
    bus = smbus.SMBus(1)
   
    def __init__(self, address = 0x4B):
        self.address = address
   
    def read_raw(self):
        # Reads word (16 bits) as int
        rd = self.bus.read_word_data(self.address, 0)
        # Exchanges upper and lower bytes
        data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
        # Ignores two least significiant bits
        return data >> 2

adc = MCP3021()




while True:
    raw = adc.read_raw()

    moisture_percentage = ((DRY_VALUE - raw) * 100.0) / (DRY_VALUE - WET_VALUE)

    print(f"Raw: {raw}, Moisture: {moisture_percentage:.2f}%")
    print("Raw :", raw)
    time.sleep(1)