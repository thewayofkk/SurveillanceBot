from flask import Flask, render_template, request, redirect, url_for, make_response
import time
import RPi.GPIO as GPIO
import serial

mA1=18
mA2=23
mB1=24
mB2=25
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(mA1, GPIO.OUT)
GPIO.setup(mA2, GPIO.OUT)
GPIO.setup(mB1, GPIO.OUT)
GPIO.setup(mB2, GPIO.OUT)
GPIO.output(mA1, 0)
GPIO.output(mA2, 0)
GPIO.output(mB1, 0)
GPIO.output(mB2, 0)
app = Flask(__name__) #set up flask server
#when the root IP is selected, return index.html page
@app.route('/')
def index():
    return render_template('index.html')
#recieve which pin to change from the button press on index.html
#each button returns a number that triggers a command in this function
#
#Uses methods from motors.py to send commands to the GPIO to operate the motors
@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):
    global changePin
    changePin = int(changepin) #cast changepin to an int
    if changePin == 1:
        print ("Left")
        GPIO.output(mA1 , 0)
        GPIO.output(mA2 , 0)
        GPIO.output(mB1 , 1)
        GPIO.output(mB2 , 0)
    elif changePin == 2:
        print ("Forward")
	ser = serial.Serial('/dev/ttyACM0',9600)
	ser.flushInput()
	ser.flushOutput()

	while True:
		read = int(ser.readline())
		print read
		if read <= 22 or changePin != 2:
			GPIO.output(mA1 , 0)
			GPIO.output(mA2 , 0)
			GPIO.output(mB1 , 0)
			GPIO.output(mB2 , 0)
			ser.flushInput()
			ser.flushOutput()
			break
		else:
			GPIO.output(mA1, 1)
			GPIO.output(mA2, 0)
			GPIO.output(mB1, 1)
			GPIO.output(mB2, 0)

    elif changePin == 3:
        print ("Right")
        GPIO.output(mA1 , 1)
        GPIO.output(mA2 , 0)
        GPIO.output(mB1 , 0)
        GPIO.output(mB2 , 0)
    elif changePin == 4:
        print ("Reverse")
	ser1 = serial.Serial('/dev/ttyAMA0',9600)
	ser1.flushInput()
	ser1.flushOutput()
	while True:
		read1=int(ser1.readline())
		print read
		if read1 <= 22 or changePin !=4:
			GPIO.output(mA1 , 0)
			GPIO.output(mA2 , 0)
			GPIO.output(mB1 , 0)
			GPIO.output(mB2 , 0)
			ser1.flushInput()
			ser1.flushOutput()
			break
		else:
			GPIO.output(mA1, 0)
			GPIO.output(mA2, 1)
			GPIO.output(mB1, 0)
			GPIO.output(mB2, 1)
    elif changePin == 5:
        GPIO.output(mA1 , 0)
        GPIO.output(mA2 , 0)
        GPIO.output(mB1 , 0)
        GPIO.output(mB2 , 0)
    response = make_response(redirect(url_for('index')))
    return(response)
app.run(debug=True, host='0.0.0.0', port=8000) #set up the server in debug mode to the port 8000


