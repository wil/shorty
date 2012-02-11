# -*- coding: utf-8 -*-

import os

BASE_URL = os.environ.get('BASE_URL', 'http://localhost:5000')

PREFIX = '_'

DEBUG = True
TESTING = False

SECRET_KEY = os.environ.get('SECRET_KEY', 'DuMmY sEcReT kEy')
CSRF_ENABLED = True
CSRF_SESSION_KEY = '_csrf_token'

if 'DATABASE_URL' in os.environ:
    import urlparse

    # Register database schemes in URLs.
    urlparse.uses_netloc.append('postgres')
    urlparse.uses_netloc.append('mysql')

    url = urlparse.urlparse(os.environ['DATABASE_URL'])

    if url.scheme == 'postgres':
        scheme = 'postgresql+psycopg2'
    elif url.scheme == 'mysql':
        scheme = 'mysql+mysqldb'
    else:
        assert False, "Unknown scheme %s" % url.scheme

    SQLALCHEMY_DATABASE_URI = '%s:///%s:%s@%s%s/%s' % (
        scheme,
        url.username,
        url.password,
        url.hostname,
        ':%s' % url.port if url.port else '',
        url.path[1:],
    )
else:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///shorty.sqlite'

try:
    from .local_config import *
except ImportError:
    pass
