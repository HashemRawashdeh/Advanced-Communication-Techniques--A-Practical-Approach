#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: AM Communication System
# Author: Hashem Rawashdeh
# Copyright: 2021
# GNU Radio version: 3.10.10.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class AMCOM(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "AM Communication System", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("AM Communication System")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "AMCOM")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 768E3
        self.mejwiz = mejwiz = firdes.band_pass(15, samp_rate, 1, 25e3, 5e3, window.WIN_HANN, 6.76)
        self.V = V = 2
        self.A = A = 2

        ##################################################
        # Blocks
        ##################################################

        self._V_range = qtgui.Range(0, 5, 0.5, 2, 200)
        self._V_win = qtgui.RangeWidget(self._V_range, self.set_V, "V", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._V_win)
        self._A_range = qtgui.Range(0, 5, 0.5, 2, 20)
        self._A_win = qtgui.RangeWidget(self._A_range, self.set_A, "A", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._A_win)
        self.qtgui_sink_x_1 = qtgui.sink_f(
            2048, #fftsize
            window.WIN_BLACKMAN, #wintype
            0, #fc
            samp_rate, #bw
            'Output', #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_1.set_update_time(1.0/100)
        self._qtgui_sink_x_1_win = sip.wrapinstance(self.qtgui_sink_x_1.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_1.enable_rf_freq(True)

        self.top_layout.addWidget(self._qtgui_sink_x_1_win)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(16, mejwiz)
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('C:\\Users\\user\\Downloads\\Music\\AH.wav', True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(V)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(A)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(1)
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 150e3, 0.5, 0, 0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_am_demod_cf_0 = analog.am_demod_cf(
        	channel_rate=samp_rate,
        	audio_decim=16,
        	audio_pass=20e3,
        	audio_stop=25e3,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_am_demod_cf_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_float_to_complex_0, 0), (self.analog_am_demod_cf_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_sink_x_1, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "AMCOM")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_mejwiz(firdes.band_pass(15, self.samp_rate, 1, 25e3, 5e3, window.WIN_HANN, 6.76))
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_sink_x_1.set_frequency_range(0, self.samp_rate)

    def get_mejwiz(self):
        return self.mejwiz

    def set_mejwiz(self, mejwiz):
        self.mejwiz = mejwiz
        self.interp_fir_filter_xxx_0.set_taps(self.mejwiz)

    def get_V(self):
        return self.V

    def set_V(self, V):
        self.V = V
        self.blocks_multiply_const_vxx_1.set_k(self.V)

    def get_A(self):
        return self.A

    def set_A(self, A):
        self.A = A
        self.blocks_multiply_const_vxx_0.set_k(self.A)




def main(top_block_cls=AMCOM, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
