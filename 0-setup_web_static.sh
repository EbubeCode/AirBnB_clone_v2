#!/usr/bin/env bash
# setup script for webstatic deployment

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

printf "<html>\n<head></head>\n<body>Hello World!</body><html>\n" > /data/web_static/releases/test/index.html
if [ -e /data/web_static/current ]; then
	rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf "server {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\
	\n\troot /var/www/html;\n\tindex index.html index.htm index.nginx-debian.html;\
	\n\terror_page 404 403 500 503 /error-page.html;\n\tadd_header X-Served-By %s;\
	\n\tserver_name _;\n\tlocation / {\n\t\ttry_files \$uri \$uri/ =404;\n\t}\n\tlocation = /error-page.html {\
	\n\t\tinternal;\n\t}\n\tlocation /hbnb_static {\n\t\t alias /data/web_static/current/;\n\t}\n}\n" \
	"$HOSTNAME"> /etc/nginx/sites-available/default
service nginx restart
