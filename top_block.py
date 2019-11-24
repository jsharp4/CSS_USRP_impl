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
        #type characters into this text box
        self.variable_text_box_0 = variable_text_box_0 = 0
        #the same characters (hopefully) show up here
        self.variable_static_text_0 = variable_static_text_0 = 0

        self.samp_rate = samp_rate = 44100

        self.fft_size = 1024
        #assuming we're using 915MHz band, can change to 2.4GHz depending on antenna
        self.center_freq = 915000000
        #no idea what this will need to be
        self.gain = 0

        ##################################################
        # Blocks
        ##################################################
        self._variable_text_box_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.variable_text_box_0,
        	callback=self.set_variable_text_box_0,
        	label='variable_text_box_0',
        	converter=forms.float_converter(),
        )
        self.Add(self._variable_text_box_0_text_box)
        self._variable_static_text_0_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.variable_static_text_0,
        	callback=self.set_variable_static_text_0,
        	label='variable_static_text_0',
        	converter=forms.float_converter(),
        )
        self.Add(self._variable_static_text_0_static_text)
        #transmitter
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="sc16",
        		channels=range(1),
        	),
        )
        #receiver
        self.uhd_source_0 = uhd.usrp_source(
            ",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="sc16",
        		channels=range(1),
        	),
        )
        #fft block for decoding received shirp
        self.fft_0 = fft.fft_vcc(
            fft_size, 
            True, 
            fft.window.blackmanharris(fft_size)
        )

        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_source_0.set_gain(gain, 0)

        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_sink_0.set_gain(gain, 0)
        #load wavfile to push to transmitter, will need to make new one for each different file
        self.blocks_wavfile_source_0 = blocks.wavfile_source('chirps/1.wav', False)
        #inv chirp for decoding, will be the same no matter what we are transmitting
        self.blocks_wavfile_source_0 = blocks.wavfile_source('chirps/inv.wav', False)

        ##################################################
        # Connections
        ##################################################
        #loaded chirp pushes to transmitter
        self.connect((self.blocks_wavfile_source_0, 0), (self.uhd_usrp_sink_0, 0))
        #receiver pushes to multiplier
        self.connect((self.uhd_source_0, 0), (self.fft_0, 0))

    def get_variable_text_box_0(self):
        return self.variable_text_box_0

    def set_variable_text_box_0(self, variable_text_box_0):
        self.variable_text_box_0 = variable_text_box_0
        self._variable_text_box_0_text_box.set_value(self.variable_text_box_0)

    def input_text_callback(self, variable_text_box_0):
        set_variable_text_box_0(self, variable_text_box_0)
        for char in self.variable_text_box_0:
            self.disconnect((self.blocks_wavfile_source_0, 0), (self.uhd_usrp_sink_0, 0))
            blocks_wavfile_source_0 = blocks.wavfile_source(char + '.wav', False)
            self.connect((self.blocks_wavfile_source_0, 0), (self.uhd_usrp_sink_0, 0))

    def get_variable_static_text_0(self):
        return self.variable_static_text_0

    def set_variable_static_text_0(self, variable_static_text_0):
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
