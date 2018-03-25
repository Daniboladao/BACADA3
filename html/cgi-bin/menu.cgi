#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()
menu=var.split("=")[0]

def cabecalho():
	print("content-type: text/html")
	print("")

def Gerencia():
	cabecalho()
	ge = open("/var/www/html/gerencia.html", "r")
	html=ge.read()
	ge.close()
	print(html)

def Agendar():
	cabecalho()
	ag = open("/var/www/html/agendar.html", "r")
	html=ag.read()
	ag.close()
	print(html)

def Processos():
	cabecalho()
	print("<link href='/styles.css' rel='stylesheet'>")
	print ("<h1 class='titulo'>Processos<h1/>")
	print ("<textarea rows='100' cols='100' class='user' >")
	ps = open("/var/www/html/cgi-bin/processos.log", "r")
	html=ps.read()
	ps.close()
	print(html)
	print ("</textarea>")


if menu == "GE":
	Gerencia()
elif menu == "AG":
	Agendar()
elif menu == "PS":
	Processos()	
