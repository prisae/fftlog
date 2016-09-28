#!/usr/bin/env python
from numpy.distutils.core import setup, Extension

setup(name = "fftlog",
      version = "1.0",
      description = "Wrapper (f2py) for Fortran FFTLog (Version 13 March 2000) by Andrew J.S. Hamilton",
      author = 'Dieter Werthmüller',
      author_email = 'dieter.werthmuller@gmx.ch',
      license='CC0',
      url='https://github.com/prisae/fftlog',
      ext_modules = [Extension(name = "fftlog", sources = ['fftlog.pyf',] +
                     ['src/cdgamma.f', 'src/drfftb.f', 'src/drfftf.f',
                      'src/drffti.f', 'src/fftlog.f'],)],
      )
