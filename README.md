# Catalog_Linux
This project uses a Linux Web Server to host a WSGI app. 

Public IP Address: http://54.205.56.181<br>
URL: ec2-54.205.56.181.compute-1.amazonaws.com<br>
SSH port: 2200<br>

<hr>
Dependencies:

1. Apache2
2. PostgreSQL
3. libapache2-mod-wsgi
4. git 
5. pip
6. psycopg2
7. requests
8. http2lib
9. jinja2
10. flask
11. SQLalchemy
12. Facebook API
13. Google API

<hr>

WSGI Configuration 


<VirtualHost *:80>

        ServerName 54.205.56.181
        ServerAdmin admin@54.205.56.181
        ServerAlias ec2-54.205.56.181.compute-1.amazonaws.com
        WSGIScriptAlias / /var/www/Catalog_Linux/app.wsgi
        <Directory /var/www/Catalog_Linux/catalog/>
                Order allow,deny
                Allow from all
        </Directory>
        Alias /static /var/www/Catalog_Linux/catalog/static
        <Directory /var/www/Catalog_Linux/catalog/static>
                Order allow,deny
                Allow from all
        </Directory>

        ErrorLog ${APACHE_LOG_DIR}/error.log
        LogLevel warn
        CustomLog ${APACHE_LOG_DIR}/access.log combined


</VirtualHost>

vim: syntax=apache ts=4 sw=4 sts=4 sr noet

<hr>


Resources
<br>
https://discussions.udacity.com/c/nd004-p7-linux-based-server-configuration
http://stackoverflow.com/questions/28307431/python-ioerror-errno-2-no-such-file-or-directory-but-file-exists
https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
https://www.digitalocean.com/community/tutorials/how-to-secure-postgresql-on-an-ubuntu-vps
https://techarena51.com/index.php/flask-sqlalchemy-postgresql-tutorial/
http://docs.sqlalchemy.org/en/latest/core/engines.html
http://stackoverflow.com/questions/37386481/connection-refused-to-postgresql
https://github.com/hotosm/osm-tasking-manager2/issues/23
