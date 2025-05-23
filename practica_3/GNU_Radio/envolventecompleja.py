# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: envolventecompleja
# GNU Radio version: v3.10.11.0-89-ga17f69e7

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import threading







class envolventecompleja(gr.hier_block2):
    def __init__(self, Ac=1, Ka=1):
        gr.hier_block2.__init__(
            self, "envolventecompleja",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Ac = Ac
        self.Ka = Ka

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################

        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(Ac)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(Ka)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self, 0), (self.blocks_multiply_const_vxx_0, 0))


    def get_Ac(self):
        return self.Ac

    def set_Ac(self, Ac):
        self.Ac = Ac
        self.blocks_multiply_const_vxx_0_0.set_k(self.Ac)

    def get_Ka(self):
        return self.Ka

    def set_Ka(self, Ka):
        self.Ka = Ka
        self.blocks_multiply_const_vxx_0.set_k(self.Ka)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

