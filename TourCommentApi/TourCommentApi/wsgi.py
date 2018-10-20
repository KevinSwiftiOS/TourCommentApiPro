# -*- coding: utf-8 -*-
"""
WSGI config for TourCommentApi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TourCommentApi.settings")
#
# application = get_wsgi_application()
import sys
import os
path = '/root/ckqtemp/TourCommentApiPro/TourCommentApi'
if path not in sys.path:
 sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'TourCommentApi.settings'

# then:

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()