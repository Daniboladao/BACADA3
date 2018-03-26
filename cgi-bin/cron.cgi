#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()
#Min=59&Hor=23&Dia=31&Mes=12&Sem=7&Usr=root&Cmd=ping+8.8.8.8
import os,re
Min=var.split("&")[0].split("=")[1]
Hor=var.split("&")[1].split("=")[1]
Dia=var.split("&")[2].split("=")[1]
Mes=var.split("&")[3].split("=")[1]
Sem=var.split("&")[4].split("=")[1]
Usr=var.split("&")[5].split("=")[1]
Cmd=var.split("=")[7].split("+")[1]

print("content-type: text/html")
print("")
print("<link href='/styles.css' rel='stylesheet' >")

def erro():
    print("<h1 class='user'>Erro Tente Novamente..<h1/>")

def validacao():
    if re.match("^([*]|[1-9]|[1-5][0-9])$", Min)\
        and re.match("[*]|^([0-9]|1[0-9]|2[0-3])$", Hor)\
        and re.match("[*]|^([1-9]|[12][0-9]|3[0-1])$", Dia)\
        and re.match("[*]|^([1-9]|[1][0-2])$", Mes)\
        and re.match("[*]|^([0-7])$", Sem)\
        and re.match("^([a-zA-Z0-9])", Usr)\
        and re.match("[a-zA-Z0-9&><%|+-]+", Cmd):
        agendar()
    else:
        erro()


def agendar():
    os.system("echo "  + Min + " " + Hor + " " + Dia + " " + Mes + " " + Sem + " " + Usr + " " + Cmd + " " '>> /etc/crontab')
    os.system("sudo /var/www/html/cgi-bin/script.sh cron restart")
    print("<h1 class='user'>Agendado Com Sucesso!<h1/>")

if validacao():
    agendar()

