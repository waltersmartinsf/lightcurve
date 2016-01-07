"""
Lightcurve Model

author: Walter S. Martins Filho
date: 24 july 2015

Obtain the bestfit lightcurve model to your planetary transit: BIC, mpfit solution.
____

This code obtain the bestfit for the airmass correction in a primary transit for a
exoplanet.

It use two external codes (this codes are inside the lightcurve model):

(1) mpfit function in Python that was write in C. This package is mpyfit.

(2) occultquad function: this code was wirte by Laura Kreidberg and you can read
more in her site: http://astro.uchicago.edu/~kreidberg/

___

INPUT FILES:

THe input files are the output files from EXODORL program develop by Kyle Pearson.
You can read more in his website: https://sites.google.com/a/email.arizona.edu/kyle-pearson/exodrpl

sysparam*.txt : file with planet and host star information
hjd : ascci file in Results directory (below your data direcory) with the Julian dates of your transit
XYpos+Airmass.txt : ascii file with the XY-position  (two columns) and the airmass (third column) of your transit
allfulx* files: ascii files with the flux of your host start and comparative star with diferent appertures
error_allflux* files: the associated errorbars of the allflux data

OUTPUT FILES:
"""
import occultation_bic
