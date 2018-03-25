#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()
usuario=var.split("&")[0].split("=")[1]
senha=var.split("&")[1].split("=")[1]

def cabecalho():
	print("content-type: text/html")
	print("")
	print("<link href='/styles.css' rel='stylesheet'>")

def menu():
	cabecalho()
	f = open("/var/www/html/menu.html", "r")
	html=f.read()
	f.close()
	print(html)

def erro():
	cabecalho()
	print("<h1 class='titulo'>Login Falhou..</h1>")

if usuario == "daniel" and senha == "oliveira":
	menu()
else:
	erro()
