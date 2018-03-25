#!/bin/bash
cp firewall.sh /usr/bin/firewall
chmod 777 /etc/crontab
case $1 in
 bind9) $(systemctl $2 $1) ;;
 nagios3) $(systemctl $2 $1) ;;
 firewall) $(firewall $2);;
 cron) $(systemctl $2 $1);;
*) exit 1 ;;
esac

~
~
~
