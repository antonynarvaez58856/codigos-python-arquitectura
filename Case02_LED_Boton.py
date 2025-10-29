import RPi.GPIO as GPIO

# Declarar constantes
PIN_BOTON = 3
PIN_LED = 7

# Declarar variables
estadoBoton = False

# zona de  Configuración
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) #desactivar menasajes de advertencia
GPIO.setup(PIN_BOTON, GPIO.IN)
GPIO.setup(PIN_LED, GPIO.OUT)

# Programa principal
while True:
	estadoBoton = GPIO.input(PIN_BOTON) # guardar el estado de la entrada en una variable
 
	if estadoBoton == True: # si el boton esta precionado, entonces:
        	GPIO.output(PIN_LED, True) # encender led
	print("PRESIONADO")
	else:   # si el boton no esta precionado entonces :
        	GPIO.output(PIN_LED, False) # apagar led
