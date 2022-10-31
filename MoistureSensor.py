import ADC0834
import Rpi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#adc = ADC0834()
#value =adc.read( channel = 0 )
sig = ADC0834.getResult(0)
print("anliegende Spannung: %.2f" %(sig / 1023.0 * 3.3))