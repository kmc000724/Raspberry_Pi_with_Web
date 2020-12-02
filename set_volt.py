#!/usr/bin/python3

import cgi, cgitb
import RPi.GPIO as GPIO

cgitb.enable ()
print ("content-type:text/html; charset=UTF-8\n")

form = cgi.FieldStorage ()
gpio_pin = int (form.getvalue ("gpio_pin"))
GPIO.setmode (GPIO.BOARD)
GPIO.setup (gpio_pin, GPIO.OUT)

if GPIO.input (gpio_pin) == 1:
    GPIO.output (gpio_pin, 0)
else:
    GPIO.output (gpio_pin, 1)

print ("<html>")
print ("<head>")
print ("    <meta http-equiv=\"refresh\" content=\"0;url=gpio.py\"/>")
print ("</head>")
print ("<body>")
print ("</body>")
print ("</html>")
