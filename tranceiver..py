#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Nov 17 16:24:02 2019
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import fft
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        # type characters into this text box
        self.variable_text_box_0 = variable_text_box_0 = 0
        # the same characters (hopefully) show up here
        self.variable_static_text_0 = variable_static_text_0 = 0

        self.samp_rate = samp_rate = 44100

        self.fft_size = 1024
        # assuming we're using 915MHz band, can change to 2.4GHz depending on antenna
        self.center_freq = 915000000
        # no idea what this will need to be
        self.gain = 0

        # TODO variables to pass into custom fft_decoder
        self.coeff_0 # y-intercept of decode function
        self.coeff_1 #slope of decode function

        ##################################################
        # Blocks
        ##################################################
        self._variable_text_box_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.variable_text_box_0,
            #fancy custom callback! (see below)
        	callback=self.input_text_callback,
        	label='data to transmit',
        	converter=forms.float_converter(),
        )
        self.Add(self._variable_text_box_0_text_box)
        self._variable_static_text_0_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.variable_static_text_0,
        	callback=self.set_variable_static_text_0,
        	label='received data',
        	converter=forms.float_converter(),
        )
        self.Add(self._variable_static_text_0_static_text)
        # transmitter
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="sc16",
        		channels=range(1),
        	),
        )
        # receiver
        self.uhd_source_0 = uhd.usrp_source(
            ",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="sc16",
        		channels=range(1),
        	),
        )
        # fft block for decoding received shirp
        self.fft_0 = fft.fft_vfc(
            fft_size, 
            True, 
            fft.window.blackmanharris(fft_size)
        )

        # TODO create simple sink block to convert output from fft to a character value
        self.fft_decoder = fft_decoder(
            self.coeff_1, # slope of function relating fft to ascii
            self.coeff_0, # y-intercept of function relating fft to ascii
            set_received_text #callback to set gui text value
        )

        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_source_0.set_gain(gain, 0)

        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_sink_0.set_gain(gain, 0)
        # load wavfile to push to transmitter, will need to make new one for each different file
        self.blocks_wavfile_source_0 = blocks.wavfile_source('chirps/1.wav', False)
        # inv chirp for decoding, will be the same no matter what we are transmitting
        self.blocks_wavfile_source_inv = blocks.wavfile_source('chirps/inv.wav', False)
        # multipier for raw inv * received chirp
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)

        ##################################################
        # Connections
        ##################################################
        # loaded chirp pushes to transmitter
        self.connect((self.blocks_wavfile_source_0, 0), (self.uhd_usrp_sink_0, 0))
        # receiver pushes to multiplier
        self.connect((self.uhd_source_0, 0), (self.blocks_multiply_xx_0, 0))
        # inverse chirp pushes to multiplier
        self.connect((self.blocks_wavfile_source_inv, 0), (self.blocks_multiply_xx_0, 1))
        # multiplier pushes to fft
        self.connect((self.blocks_multiply_xx_0, 0)), (self.fft_0, 0)
        # TODO 


    def get_variable_text_box_0(self):
        return self.variable_text_box_0

    def set_variable_text_box_0(self, variable_text_box_0):
        self.variable_text_box_0 = variable_text_box_0
        self._variable_text_box_0_text_box.set_value(self.variable_text_box_0)

    # this is callback we want to be using for the gui text box
    # basically, when there's input to the text box, we want to load a new wavfile for each character,
    #  connect it, and transmit
    def input_text_callback(self, variable_text_box_0):
        set_variable_text_box_0(self, variable_text_box_0)
        for char in self.variable_text_box_0:
            self.disconnect((self.blocks_wavfile_source_0, 0), (self.uhd_usrp_sink_0, 0))
            # files are indexed right now as 1...94. chars in ASCII table are 32...195
            blocks_wavfile_source_0 = blocks.wavfile_source(str(char - 31) + '.wav', False)
            # connect new file to transmit
            # note: I'm not sure if this is event triggered on a new connection or not,
            #  we might need to find some way to time it so that it transmits each new letter
            #  only once
            self.connect((self.blocks_wavfile_source_0, 0), (self.uhd_usrp_sink_0, 0))

    def get_variable_static_text_0(self):
        return self.variable_static_text_0
    # put the fft through a linear function to get new letter, append to current string
    # this function needs to be used by the custom fft -> char conversion block
    def set_received_text(self, new_letter):
        self.variable_static_text_0 = variable_static_text_0 + new_letter
        self._variable_static_text_0_static_text.set_value(self.variable_static_text_0)

    def set_variable_static_text_0(self, new_letter):
        self.variable_static_text_0 = variable_static_text_0
        self._variable_static_text_0_static_text.set_value(self.variable_static_text_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
