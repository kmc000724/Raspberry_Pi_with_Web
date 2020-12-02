#!/usr/bin/env python3

import os
import cgi
import cgitb

cgitb.enable ()

print ("content-type:text/html; charset=UTF-8\n")
print ("<html>")
print ("<head>")
print ("    <title>ABCD</title>")
print ("</head>")
print ("<body>")
print ("<table style=\"text-align:center;border:1px solid black;\">")
print ("    <thead>")
print ("        <tr>")
print ("            <td style=\"border:1px solid black;font-weight:bold\">BCM</td>")
print ("            <td style=\"border:1px solid black;font-weight:bold\">wPi</td>")
print ("            <td style=\"border:1px solid black;font-weight:bold\">Name</td>")
print ("            <td style=\"border:1px solid black;font-weight:bold\">Mode</td>")
print ("            <td style=\"border:1px solid black;font-weight:bold\">V</td>")
print ("            <td style=\"border:1px solid black;font-weight:bold\" colspan=\"3\">Physical</td>")
print ("            <td style=\"border:1px solid black;font-weight:bold\">V</td>")
print ("            <td style=\"border:1px solid black;font-weight:bold\">Mode</td>")
print ("            <td style=\"border:1px solid black;font-weight:bold\">Name</td>")
print ("            <td style=\"border:1px solid black;font-weight:bold\">wPi</td>")
print ("            <td style=\"border:1px solid black;font-weight:bold\">BCM</td>")
print ("        </tr>")
print ("    </thead>")
print ("    <tbody>")

result = os.popen("gpio readall")
count = 0
for raw in result:
    if count < 3:
        count += 1
        continue
    print ("    <tr>")
    data_list = raw.split ("|")
    for i in range (len (data_list)):
        data = data_list[i].strip ()
        if i > 0:
            if i == 4:
                if data_list[4].strip () == "IN":
                    print ("<td style=\"border:1px solid black\"><a href=\"set_mode.py?gpio_pin={}&gpio_mode=0\">{}</a></td>".format (data_list[6], data))
                else:
                    print ("<td style=\"border:1px solid black\"><a href=\"set_mode.py?gpio_pin={}&gpio_mode=1\">{}</a></td>".format (data_list[6], data))
            elif i == 6:
                    print ("<td style=\"border:1px solid black\"><a href=\"set_volt.py?gpio_pin={}\">{}</a></td>".format (data_list[6], data))
            elif i == 8:
                    print ("<td style=\"border:1px solid black\"><a href=\"set_volt.py?gpio_pin={}\">{}</a></td>".format (data_list[8], data))
            elif i == 10:
                if data_list[10].strip () == "IN":
                    print ("<td style=\"border:1px solid black\"><a href=\"set_mode.py?gpio_pin={}&gpio_mode=0\">{}</a></td>".format (data_list[8], data))
                else:
                    print ("<td style=\"border:1px solid black\"><a href=\"set_mode.py?gpio_pin={}&gpio_mode=1\">{}</a></td>".format (data_list[8], data))
            else:
                print ("<td style=\"border:1px solid black\">" + data + "</td>")
        if i > 12:
            break
    print ("    </tr>")
    if (count > 21):
        break
    count += 1
result.close ()

print ("</tbody>")
print ("</table>")
print ("</body>")
print ("</html>")
