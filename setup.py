# -*- coding: utf-8 -*-
import re
import sys

# Get README and remove badges.
readme = open('README.rst').read()
readme = re.sub('.*`fftlog` - A', '`fftlog` - A', readme, flags=re.DOTALL)

metadata = dict(
    name='fftlog',
    version='0.2.1',  # Adjust in fftlog/__init__.py too!
    description='Logarithmic Fast Fourier Transform',
    long_description=readme,
    author='Dieter Werthmüller',
    author_email='dieter@werthmuller.org',
    url='https://github.com/prisae/fftlog',
    license='CC0-1.0',
    packages=['fftlog', ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    ],
    install_requires=[
        'scipy',
    ],
    # setup_requires=['numpy', ],
)


bdist = ('bdist_wheel', 'bdist_egg')
nonumpy = ('--help-commands', 'egg_info', '--version', 'clean')
argv2 = len(sys.argv) >= 2
if argv2 and ('--help' in sys.argv[1:] or sys.argv[1] in nonumpy):
    # For these actions, NumPy is not required.
    #
    # They are required to succeed without Numpy, for example when pip is
    # used to install fftlog when Numpy is not yet present in the system.
    from setuptools import setup
else:
    if (argv2 >= 2 and sys.argv[1] in bdist) or ('develop' in sys.argv):

        # bdist_wheel/bdist_egg needs setuptools
        import setuptools  # noqa

    from numpy.distutils.core import setup, Extension

    metadata['ext_modules'] = [
        Extension(
            name="fftlog._fftlog",
            sources=['fftlog/fftlog.pyf', ] +
                    [
                        'fftlog/src/cdgamma.f', 'fftlog/src/drfftb.f',
                        'fftlog/src/drfftf.f', 'fftlog/src/drffti.f',
                        'fftlog/src/fftlog.f'
                    ],
                 )
        ]

setup(**metadata)
