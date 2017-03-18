#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/Catalog_Linux/")

from catalog import app as application
application.secret_key = 'x23bvd'
