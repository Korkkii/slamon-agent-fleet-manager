#!/usr/bin/env python
import argparse

import logging

from bottle import run
import sys

from slamon_afm import afm_app
from slamon_afm.admin import create_tables, drop_tables
from slamon_afm.settings import Settings
from slamon_afm.routes import agent_routes, bpms_routes, status_routes
from slamon_afm.routes.testing import testing_routes
from slamon_afm.database import init_connection


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'tasks': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'testing': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG'
        }
    }
}

def main():
    logging.basicConfig(level=logging.INFO)

    if Settings.testing_urls_available:
        pass

    parser = argparse.ArgumentParser(description='Admin util for SLAMon Agent Fleet Manager')
    parser.add_argument('-c', '--create-tables', help='Create tables', action='store_true', default=False)
    parser.add_argument('-d', '--drop-tables', help='Drop all tables', action='store_true', default=False)
    parser.add_argument('-h', '--host', help='Host name', action='store', require=True)

    init_connection(unittest=False)

    args = parser.parse_args()
    if args.create_tables is True:
        create_tables()
    elif args.drop_tables is True:
        drop_tables()

    run(afm_app.app, host=args.host, port=Settings.port, debug=True)


if __name__ == '__main__':
    main()
