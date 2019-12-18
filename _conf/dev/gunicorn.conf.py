# -*- coding: utf-8 -*-

bind = '127.0.0.1:1688'
pidfile = '/home/www/aviasales/run/aviasales.gunicorn.pid'
workers = 1
timeout = 900

## Logging
loglevel = 'critical'
errorlog = '/home/www/aviasales/log/gunicorn.error.log'
# accesslog = '/home/www/aviasales/log/gunicorn.access.log'
