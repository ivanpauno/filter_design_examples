#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ivanpauno
"""

import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
import filter_utils

wp = 2 * np.pi * 1000
ws = 2 * np.pi * 5000
alpha_max=0.5
alpha_min=25

num, den = filter_utils.cheby(wp, ws, alpha_max, alpha_min)
cheby = sig.TransferFunction(num, den)

print('Resultado:\n')
filter_utils.pretty(cheby.num, cheby.den)
print('\n\n')
filter_utils.print_zpk(cheby.num, cheby.den)

filter_utils.pzmap(cheby)
filter_utils.plot_bode(cheby, gd=True)

plt.show()
