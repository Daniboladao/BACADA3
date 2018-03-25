#!/usr/bin/python
#-*- coding: utf8 -*-
import os
var=raw_input()
#d_i=iniciar
acao=var.split("=")[0]
print("content-type: text/html")
print("")
print("<link href='/styles.css' rel='stylesheet'>")
print("<h1 class='titulo'>")
if acao == "f_i":
        print("Firewall iniciado com sucesso!")
        os.system("sudo /var/www/html/cgi-bin/script.sh firewall start")
elif acao == "f_p":
        print("Firewall desligado com sucesso!")
        os.system("sudo /var/www/html/cgi-bin/script.sh firewall stop")
elif acao =="f_r":
        print("Firewall reiniciado com sucesso!")
        os.system("sudo /var/www/html/cgi-bin/script.sh firewall restart")
elif acao == "d_i":
        print("Dns iniciado com sucesso!")
        os.system("sudo /var/www/html/cgi-bin/script.sh bind9 start")
elif acao == "d_p":
        print("Dns parado com sucesso!")
        os.system("sudo /var/www/html/cgi-bin/script.sh bind9 stop")
elif acao =="d_r":
        print("Dns reiniciado com sucesso!")
        os.system("sudo /var/www/html/cgi-bin/script.sh bind9 restart")
elif acao == "n_i":
        print("Nagios iniciado com sucesso!")
        os.system("sudo /var/www/html/cgi-bin/script.sh nagios3 start")
elif acao == "n_p":
        print("Nagios parado com sucesso")
        os.system("sudo /var/www/html/cgi-bin/script.sh nagios3 stop")
elif acao =="n_r":
        print("Nagios reiniciado com sucesso!")
        os.system("sudo /var/www/html/cgi-bin/script.sh nagios3 restart")
else:
        print("Não foi possivel processar sua solicitação")
print("<h1/>")
	
