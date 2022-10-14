#!/usr/bin/env bash
# Script that configures Nginx server with some folders and files
apt-get -y update
apt-get -y install nginx
sudo service nginx start
if ! [ -d '/data/web_static/releases/test/' ]
then
	mkdir -p /data/web_static/releases/test/;
fi

if ! [ -d '/data/web_static/shared/' ]
then
	mkdir -p /data/web_static/shared/;
fi
echo "Holberton School" > /data/web_static/releases/test/index.html
if ! [ -h '/data/web_static/current' ]
then
	ln -sf /data/web_static/releases/test/ /data/web_static/current
fi
chown -R ubuntu:ubuntu /data/
locatehbnb="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n" 
sed -i "/server_name _;/a $locatehbnb" /etc/nginx/sites-enabled/default
service nginx restart
exit 0
