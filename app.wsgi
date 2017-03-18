#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/Catalog_Linux/Catalog_Linux")

from __init__ import app as application
application.secret_key = 'x23bvd'
