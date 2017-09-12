#!/usr/bin/env python
import cgitb
cgitb.enable(display=0, logdir="/home/pi/logs/")
print "Content-type: text/html\n\n"
print "<h1>Hello World</h1>"
print "<h2>Bye W0rld</h2>"
