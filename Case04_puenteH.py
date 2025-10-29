import RPi.GPIO as GPIO
from time import sleep

# Declarar constantes
PIN_IN1 = 7   # GPIO4
PIN_IN2 = 11  # GPIO17
PIN_IN3 = 13  # GPIO27
PIN_IN4 = 15  # GPIO22
PIN_ENA = 32  # PWM
PIN_ENB = 33  # PWM

# Declarar variables
maxSpeed = 100
minSpeed = 0

# Configuración
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(PIN_IN1, GPIO.OUT)
GPIO.setup(PIN_IN2, GPIO.OUT)
GPIO.setup(PIN_IN3, GPIO.OUT)
GPIO.setup(PIN_IN4, GPIO.OUT)
GPIO.setup(PIN_ENA, GPIO.OUT)
GPIO.setup(PIN_ENB, GPIO.OUT)

# Configurar PWM
motorIzq = GPIO.PWM(PIN_ENA, maxSpeed)
motorDer = GPIO.PWM(PIN_ENB, maxSpeed)

# Iniciar PWM
motorIzq.start(maxSpeed)
motorDer.start(maxSpeed)

# Programa principal
while True:
    motorIzq.ChangeDutyCycle(maxSpeed)
    motorDer.ChangeDutyCycle(maxSpeed)

    GPIO.output(PIN_IN1, True)
    GPIO.output(PIN_IN2, False)
    GPIO.output(PIN_IN3, True)
    GPIO.output(PIN_IN4, False)
