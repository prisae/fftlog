`fftlog` - python wrapper FFTLog
================================

This is a simple `f2py`-wrapper for the logarithmic FFT code *FFTLog* as
presented in Appendix B of [Hamilton_2000]_ and published at
`casa.colorado.edu/~ajsh/FFTLog <http://casa.colorado.edu/~ajsh/FFTLog>`_.

A pure python version (`pyfftlog`) can be found on
`github.com/prisae/pyfftlog <https://github.com/prisae/pyfftlog>`_.
Tests have shown that `fftlog` is a bit faster than `pyfftlog`, but `pyfftlog`
is easier to implement, as you only need `NumPy` and `SciPy`, without the
need to compile anything.

I hope that `FFTLog` will make it into `SciPy` in the future, which will make
this project redundant.


Description of FFTLog from the FFTLog-Website
---------------------------------------------

FFTLog is a set of fortran subroutines that compute the fast Fourier or Hankel
(= Fourier-Bessel) transform of a periodic sequence of logarithmically spaced
points.

FFTLog can be regarded as a natural analogue to the standard Fast Fourier
Transform (FFT), in the sense that, just as the normal FFT gives the exact (to
machine precision) Fourier transform of a linearly spaced periodic sequence, so
also FFTLog gives the exact Fourier or Hankel transform, of arbitrary order m,
of a logarithmically spaced periodic sequence.

FFTLog shares with the normal FFT the problems of ringing (response to sudden
steps) and aliasing (periodic folding of frequencies), but under appropriate
circumstances FFTLog may approximate the results of a continuous Fourier or
Hankel transform.

The FFTLog algorithm was originally proposed by [Talman_1978]_.

*For the full documentation, see*
`casa.colorado.edu/~ajsh/FFTLog <http://casa.colorado.edu/~ajsh/FFTLog>`_.


Installation
------------

To install it in your python distribution:

.. code:: bash

   python setup.py install


To just create the module that you can import locally:

.. code:: bash

   f2py -c fftlog.pyf src/*

You need a fortran compiler for this to work.

Check out the Jupyter Notebook `fftlogtest.ipynb` in the root directory. It is
a translation of the test-function `fftlogtest.f`, and should get you started.


Creation
--------

The power of `f2py` did most of the work.

The *src*-directory contains the original fortran files as downloaded from
`casa.colorado.edu/~ajsh/FFTLog <http://casa.colorado.edu/~ajsh/FFTLog>`_.  The
only change I made was to recode the coding of *fftlog.f*, as `f2py` struggled
with a few characters in the description part:

.. code:: bash

   recode latin1..UTF-8 fftlog.f

Thereafter I used `f2py` to produce the `pyf`-instructions with the following
command, generating only hooks for the functions `fhti`, `fttl`, `fht`, and
`fhtq`:

.. code:: bash

   f2py src/* -m fftlog -h fftlog.pyf only: fhti fftl fht fhtq :

Lastly I amended the `pyf`-instructions, mainly with some :code:`intent` and
:code:`optional` statements as well as the corresponding default values.


Notes
-----
1. :code:`kropt = 3` (interactive adjusting) is not possible with `fftlog`
2. :code:`wsave`-dimension is set to :code:`2*n+3*(n/2)+19`, the biggest of the
   four minimum sizes described in `fftlog.f`.


References
----------

.. [Hamilton_2000] Hamilton, A. J. S., 2000, Uncorrelated modes of the
    non-linear power spectrum: Monthly Notices of the Royal Astronomical
    Society, 312, pages 257-284; DOI: `10.1046/j.1365-8711.2000.03071.x
    <http://dx.doi.org/10.1046/j.1365-8711.2000.03071.x>`_; Website of FFTLog:
    `casa.colorado.edu/~ajsh/FFTLog <http://casa.colorado.edu/~ajsh/FFTLog>`_.

.. [Talman_1978] Talman, J. D., 1978, Numerical Fourier and Bessel transforms
    in logarithmic variables: Journal of Computational Physics, 29, pages
    35-48; DOI: `10.1016/0021-9991(78)90107-9
    <http://dx.doi.org/10.1016/0021-9991(78)90107-9>`_.


License and Credits
-------------------

These additions to the original FFTLog-code are released to the public domain
under the `CC0 1.0 License
<http://creativecommons.org/publicdomain/zero/1.0>`_.

Permission to distribute the original Fortran `FFTLog` code with this Python
`fftlog` package has been granted (email from Andrew Hamilton to Dieter
Werthmüller dated 28 September 2016).

Credits commented in the original code:

`FFTLog` uses the NCAR suite of FFT routines, and a modified version of the
complex Gamma function from the gamerf package at
`momonga.t.u-tokyo.ac.jp/~ooura/gamerf.html
<http://momonga.t.u-tokyo.ac.jp/~ooura/gamerf.html>`_.
The original gamerf copyright statement states::

   Copyright(C) 1996 Takuya OOURA (email: ooura@mmm.t.u-tokyo.ac.jp).
   You may use, copy, modify this code for any purpose and
   without fee. You may distribute this ORIGINAL package.

Permission to distribute the modified gamma function code with the FFTLog
package has been granted (email from Takuya Ooura to Andrew Hamilton dated 16
March 1999).
