#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/jsarp4/Documents/gnu_radio_flowcharts/CSS_USRP_impl/gr-fft_decoder/python
export PATH=/home/jsarp4/Documents/gnu_radio_flowcharts/CSS_USRP_impl/gr-fft_decoder/python/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/jsarp4/Documents/gnu_radio_flowcharts/CSS_USRP_impl/gr-fft_decoder/python/swig:$PYTHONPATH
/usr/bin/python2 /home/jsarp4/Documents/gnu_radio_flowcharts/CSS_USRP_impl/gr-fft_decoder/python/qa_fft_decoder.py 
