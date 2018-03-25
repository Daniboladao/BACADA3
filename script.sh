#!/bin/bash
cp firewall.sh /usr/bin/firewall
case $1 in
 bind9) $(systemctl $2 $1) ;;
 nagios3) $(systemctl $2 $1) ;;
 firewall) $(firewall $2);;
*) exit 1 ;;
esac

