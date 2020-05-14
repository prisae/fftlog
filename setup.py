# -*- coding: utf-8 -*-
import os
import re
# from setuptools import setup
from numpy.distutils.core import setup, Extension

# Get README and remove badges.
readme = open('README.rst').read()
readme = re.sub('----.*marker', '----', readme, flags=re.DOTALL)

description = ("Python wrapper (f2py) for Fortran FFTLog "
               "(Version 13 March 2000) by Andrew J.S. Hamilton")

setup(
    name='fftlog',
    description=description,
    long_description=readme,
    author='Dieter Werthmüller',
    author_email='dieter@werthmuller.org',
    url='https://github.com/prisae/fftlog',
    license='CC0-1.0',
    packages=['fftlog', ],
    ext_modules=[
        Extension(
            name="fftlog._fftlog",
            sources=['fftlog/fftlog.pyf', ] +
                    [
                        'fftlog/src/cdgamma.f', 'fftlog/src/drfftb.f',
                        'fftlog/src/drfftf.f', 'fftlog/src/drffti.f',
                        'fftlog/src/fftlog.f'
                    ],
                 )
        ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    ],
    install_requires=[
        'scipy',
    ],
    version = '0.2.0rc1',
    # use_scm_version={
    #     'root': '.',
    #     'relative_to': __file__,
    #     'write_to': os.path.join('fftlog', 'version.py'),
    # },
    # setup_requires=['setuptools_scm'],
)
