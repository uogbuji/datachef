#!/usr/bin/env python

from distutils.core import setup
#from lib import __version__

setup(name = "datachef",
      #version = __version__,
      version = "0.2",
      description="Data chef recipes",
      author='Uche Ogbuji',
      author_email='uche@ogbuji.net',
      url='http://uche.ogbuji.net',
      package_dir={'datachef': 'lib'},
      packages=['datachef'],
      #scripts=['ingest','fetch_catalogs','nightly'],
      #package_data={'akara': ["akara.conf"]},
      )

