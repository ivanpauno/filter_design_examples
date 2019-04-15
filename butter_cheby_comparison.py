#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 12:14:28 2019

@author: ivanpauno
"""

import scipy.signal as sig
import matplotlib.pyplot as plt
import filter_utils


# Comparación orden 5, e=1
num, den = sig.butter(5, 1, analog=True)
butter = sig.TransferFunction(num, den)
num, den = sig.cheby1(5, 3, 1, analog=True)
cheby = sig.TransferFunction(num, den)

print('Transferencia Butterworth:\n')
filter_utils.pretty(butter.num, butter.den)
print('\n\n')
filter_utils.print_zpk(butter.num, butter.den)
print('\n\nTransferencia Chebyshev:\n')
filter_utils.pretty(cheby.num, cheby.den)
print('\n\n')
filter_utils.print_zpk(cheby.num, cheby.den)

filters = [butter, cheby]
filter_utils.pzmap(filters)
filter_utils.plot_bode(filters, gd=True)

plt.show()
