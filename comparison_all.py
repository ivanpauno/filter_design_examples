#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 12:14:28 2019

@author: ivanpauno
"""

import scipy.signal as sig
import matplotlib.pyplot as plt
import filter_utils


# Comparación orden 3, att max 3dB
num, den = sig.butter(3, 1, analog=True)  # n, wp
butter = sig.TransferFunction(num, den)
num, den = sig.cheby1(3, 3, 1, analog=True)  # n, att max, wp
cheby1 = sig.TransferFunction(num, den)
num, den = sig.cheby2(3, 20, 1.539389818149637, analog=True)  # n, att min, ws
cheby2 = sig.TransferFunction(num, den)
num, den = sig.bessel(3, 1, analog=True, norm='mag')  # n, wp
bessel = sig.TransferFunction(num, den)
num, den = sig.ellip(3, 3, 20, 1, analog=True)  # n, att max, att min, wp
ellip = sig.TransferFunction(num, den)

print('Transferencia Butterworth:\n')
filter_utils.pretty(butter.num, butter.den)
print('\n\n')
filter_utils.print_zpk(butter.num, butter.den)
print('\n\nTransferencia Chebyshev tipo 1:\n')
filter_utils.pretty(cheby1.num, cheby1.den)
print('\n\n')
filter_utils.print_zpk(cheby1.num, cheby1.den)
print('\n\nTransferencia Chebyshev tipo 2:\n')
filter_utils.pretty(cheby2.num, cheby2.den)
print('\n\n')
filter_utils.print_zpk(cheby2.num, cheby2.den)
print('\n\nTransferencia Bessel:\n')
filter_utils.pretty(bessel.num, bessel.den)
print('\n\n')
filter_utils.print_zpk(bessel.num, bessel.den)
print('\n\nTransferencia Cauer, att min 20dB:\n')
filter_utils.pretty(ellip.num, ellip.den)
print('\n\n')
filter_utils.print_zpk(ellip.num, ellip.den)

filters = [butter, cheby1, cheby2, bessel, ellip]
filter_utils.pzmap(filters)
filter_utils.plot_bode(filters, gd=True)

plt.show()
