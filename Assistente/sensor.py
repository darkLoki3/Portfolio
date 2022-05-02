import RPi.GPIO as GPIO
import time

def sensor():
    """configuração do sensor de ultra som
    """    
    try:
        GPIO.setmode(GPIO.BOARD)
        PIN_TRIGGER = 7
        PIN_ECCHO = 11

        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECCHO, GPIO.IN)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        print (" Aguardando o sensor estabilizar")

        time.sleep(2)

        print("Calculo da distância")

        GPIO.output(PIN_TRIGGER, GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECCHO)==0:
            pulse_start_time = time.time()
            while GPIO.input(PIN_ECCHO)==1:
                pulse_end_time = time.time()

            pulse_duration = pulse_end_time - pulse_start_time

            distance = round(pulse_duration * 17150, 2)

            print("Distância: ", distance, "em cm")
    finally:
    #    GPIO.cleanup()
        exit()

if __name__ == '__main__':
    sensor()