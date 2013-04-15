#!/usr/bin/env python

from distutils.core import setup
#from lib import __version__

setup(name = "datachef",
      #version = __version__,
      version = "0.2.0",
      description="Data chef recipes, a grab bag for dealing with all sorts of data",
      author='Uche Ogbuji',
      author_email='uche@ogbuji.net',
      url='http://uche.ogbuji.net',
      package_dir={'datachef': 'lib'},
      packages=['datachef', 'datachef.exhibit', 'datachef.geo', 'datachef.thirdparty', 'datachef.squaredata'],
      scripts=['script/exhibit_agg',],
      #package_data={'akara': ["akara.conf"]},
      )
