import RPi.GPIO as GPIO
import time
from flask import Flask, render_template
app = Flask(__name__,template_folder='/home/pi/raspberryPi/flaskPiLEDControl')

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/turnOnGreen')
def turnOnGreen():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.OUT)
    GPIO.output(5, False)
    return render_template('index.html')

@app.route('/turnOnRed')
def turnOnRed():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, False)
    return render_template('index.html')

@app.route('/turnOffGreen')
def turnOffGreen():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.OUT)
    GPIO.output(5, True)
    return render_template('index.html')

@app.route('/turnOffRed')
def turnOffRed():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, True)
    return render_template('index.html')

@app.route('/blinkGreen')
def blinkGreen():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.OUT)
    try:    
        while True:
            GPIO.output(5, True)
            time.sleep(0.3)
            GPIO.output(5, False)
            time.sleep(0.3)
    except:
        GPIO.cleanup(5)
    return render_template('index.html')

@app.route('/blinkRed')
def blinkRed():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.OUT)
    try:
        while True:
            GPIO.output(6, True)
            time.sleep(0.3)
            GPIO.output(6, False)
            time.sleep(0.3)
    except:
        GPIO.cleanup(6)
    return render_template('index.html')

@app.route('/stopBlinkGreen')
def stopBlinkGreen():
    GPIO.setwarnings(False)
    GPIO.cleanup(5)
    return render_template('index.html')

@app.route('/stopBlinkRed')
def stopBlinkRed():
    GPIO.setwarnings(False)
    GPIO.cleanup(6)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port = 5000)
