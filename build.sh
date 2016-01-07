#!/bin/bash

printf '\n'
printf 'Begin the install of the lightcurve procedure: \n'
printf '\n'

printf 'Installing the fast procedure to obtain the limbdarkening: \n'
#installing the fast limbdarkening code
cd Fast_MA
bash build.sh
python setup.py install

printf '\n'
printf 'Installing the mpyfit package \n'
printf '(this is the mpfit package) : \n'
#installing the mpfit python function module
cd ..
cd mpyfit-master
python setup.py install

printf '\n'
printf 'Installing the lightcurve model package: \n'
#installing the lightcurve procedure
cd ..
cd lightcurve
python setup.py install

printf '\n'
printf 'END of the PROCESS \n'
