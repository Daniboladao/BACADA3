
#!/usr/bin/ptyhon
#-*- coding: utf8 -*-
var=raw_input()
menu=var.split("=")[0]
print("content-type: text/html")
print("<h1>")
if menu == "f_i":
        print("Firewall inicia")
elif menu == "f_p":
        print("Parar Firewall")
elif menu == "f_r":
        print("Reiniciar Firewall")
elif menu == "d_i":
        print("Iniciar DNS")
elif menu == "d_p":
        print("parar DNS")
elif menu == "d_r":
        print("Reiniciar DNS")
elif menu == "n_i":
        print("Iniciar Nagios")
elif menu == "n_p":
        print("Parar Nagios")
elif menu == "n_r":
        print("Reiniciar Nagios")
else:
        print("Nenhum processo válido")
print("</h1>")
