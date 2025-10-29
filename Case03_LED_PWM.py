import RPi.GPIO as GPIO
import time

# Declarar constante
pinLed = 19

# Configuración
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLed, GPIO.OUT)

# Crear objeto PWM (frecuencia 100Hz)
led = GPIO.PWM(pinLed, 100)
led.start(100)

# Programa principal
while True:
    # Aumentar brillo gradualmente
    for i in range(0, 100, 10):
        led.ChangeDutyCycle(i)
        time.sleep(0.1)

    time.sleep(1)

    # Disminuir brillo gradualmente
    for i in range(100, 0, -10):
        led.ChangeDutyCycle(i)
        time.sleep(0.1)

    time.sleep(1)
