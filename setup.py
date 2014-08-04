#!/usr/bin/env python

import sys, os
from distutils.core import setup

versionfile = 'lib/version.py'
exec(compile(open(versionfile, "rb").read(), versionfile, 'exec'), globals(), locals())
__version__ = '.'.join(version_info)

setup(name = "datachef",
      version = __version__,
      description="Data chef recipes, a grab bag for dealing with all sorts of data",
      author='Uche Ogbuji',
      author_email='uche@ogbuji.net',
      url='http://uche.ogbuji.net',
      package_dir={'datachef': 'lib'},
      packages=['datachef', 'datachef.exhibit', 'datachef.geo', 'datachef.ids', 'datachef.thirdparty', 'datachef.square'],
      scripts=['cmdline/exhibit_agg', 'cmdline/exhibit_lint'],
      )

