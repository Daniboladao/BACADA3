#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()
#min=*&hor=*&dia=*&mes=&sem=*&usr=root&cmd=ping+8.8.8.8+-c
import os,re
Min=var.split("&")[0].split("=")[1]
Hor=var.splir("&")[1].split("=")[1]
Dia=var.split("&")[2].split("=")[1]
Mes=var.split("&")[3].split("=")[1]
Sem=var.split("&")[4].split("=")[1]
Usr=var.split("&")[5].split("=")[1]
Cmd=var.split("&")[6].split("=")[1]

print("content-type: text/html")
print("")

def validacao():
	if re.match("^([*]|[1-9]|[1-5][0-9])$", Min) \
		and re.match("^([*]|[0-9]|1[0-9]|2[0-3])$", Hor)\
		and re.match("^([*]|[1-9]|[12][0-9]|3[01])$", Dia)\
		and re.match("^([*]|[1-9]|[1][0-2])$", Mes)\
		and re.match("^([*]|[0-8])$", Sem)\
		and re.match("^([*]|[a-zA-Z0-9])$", Usr)\
		and re.match("[a-zA-Z0-9&><|+- ]+", Cmd):
	return True
else:
	return False

def agendar():
	os.system("echo " + \
	Min + " " + \
	Hor + " " + \
	Dia + " " + \
	Mes + " " + \
	Sem + " " + \
	Usr + " " + \
	Cmd + "&>> /usr/lib/cgi-bin/cron.log")
if validacao():
	agendar()
else:
	erro()

