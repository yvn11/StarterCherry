#!/usr/bin/python

import cgi

fields = cgi.FieldStorage()
title = "Motion Trigger"

print "Content-Type: text/html"
print

print "<html>"
print "<title>",title,"</title>"

print "<body>"

for k in fields.keys():
	print "<b>", k.upper(), "</b>", fields[k].value,"<br>"

print "</body>"
print "</html>"

