#!/usr/bin/python3

import cgi, cgitb
import RPi.GPIO as GPIO

cgitb.enable ()
print ("content-type:text/html; charset=UTF-8\n")

form = cgi.FieldStorage ()
gpio_pin = int (form.getvalue ("gpio_pin"))
gpio_mode = int (form.getvalue ("gpio_mode"))

GPIO.setmode (GPIO.BOARD)
GPIO.setup (gpio_pin, gpio_mode)

print ("<html>")
print ("<head>")
print ("    <meta http-equiv=\"refresh\" content=\"0;url=gpio.py\"/>")
print ("</head>")
print ("<body>")
print ("</body>")
print ("</html>")
