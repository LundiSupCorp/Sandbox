import ADC0834
import RPi.GPIO as GPIO # Hier war zuvor ein Typo beim Klassenbezeichner. Rpi mit kleinem p ist falsch. Die Klasse gibt es nicht. RPi hingegen schon.
GPIO.setmode(GPIO.BCM)
ADC0834.setup() # Setup-Funktion muss aufgerufen werden, da diese die GPIO-Pins konfiguriert.
#value =adc.read( channel = 0 )
sig = ADC0834.getResult(0) # Sofern die GPIO-Pins konfiguriert sind, und alles korrekt verkabelt ist, sollte ein Wert abgefragt werden können.
print("anliegende Spannung: %.2f" %(sig / 1023.0 * 3.3))
