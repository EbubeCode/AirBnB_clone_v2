#!/usr/bin/env bash
# setup script for webstatic deployment

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

sudo truncate -s 0 /data/web_static/releases/test/index.html
printf "<html>\n<head></head>\n<body>Hello World!</body><html>\n" | sudo tee -a /data/web_static/releases/test/index.html \
	>> /dev/null
if [ -e /data/web_static/current ]; then
	sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
sudo truncate -s 0 /etc/nginx/sites-available/default
printf "server {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\
	\n\troot /var/www/html;\n\tindex index.html index.htm index.nginx-debian.html;\
	\n\terror_page 404 403 500 503 /error-page.html;\n\tadd_header X-Served-By %s;\
	\n\tserver_name _;\n\tlocation / {\n\t\ttry_files \$uri \$uri/ =404;\n\t}\n\tlocation = /error-page.html {\
	\n\t\tinternal;\n\t}\n\tlocation /hbnb_static {\n\t\t alias /data/web_static/current/;\n\t}\n}\n" \
	"$HOSTNAME" | sudo tee -a /etc/nginx/sites-available/default >> /dev/null
sudo service nginx restart
