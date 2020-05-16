# -*- coding: utf-8 -*-
import os
import re
from numpy.distutils.core import setup, Extension

# Get README and remove badges.
readme = open('README.rst').read()
readme = re.sub('.*`fftlog` - A', '`fftlog` - A', readme, flags=re.DOTALL)

setup(
    name='fftlog',
    description='Logarithmic Fast Fourier Transform',
    long_description=readme,
    author='Dieter Werthmüller',
    author_email='dieter@werthmuller.org',
    url='https://github.com/prisae/fftlog',
    license='CC0-1.0',
    packages=['fftlog', ],
    include_package_data=True,
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
    use_scm_version={
        'root': '.',
        'relative_to': __file__,
        'write_to': os.path.join('fftlog', 'version.py'),
    },
    setup_requires=['numpy', 'setuptools_scm'],
)
