#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:03:51 2019

@author: ivanpauno
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    # A = sqrt(10^(.1*alpha_min-1)/10^(.1*alpha_max-1))
    A = np.logspace(np.log10(2), np.log10(100), num=200)
    ws_array = [1.1, 1.5, 2, 3]
    n_butter = [np.log(A)/np.log(ws) for ws in ws_array]
    n_cheby = [np.arccosh(A)/np.arccosh(ws) for ws in ws_array]
    # Para verlo redondeado, descomentar las dos lineas siguientes.
    n_butter = np.ceil(n_butter)
    n_cheby = np.ceil(n_cheby)
    for i in range(len(n_butter)):
        fig, ax = plt.subplots()
        ax.ticklabel_format(useOffset=False)
        ax.set_xlabel('A')
        ax.set_ylabel('n')
        ax.grid(True)
        ax.plot(A, n_butter[i], 'k')
        ax.plot(A, n_cheby[i], 'r')
        title = 'Order comparison ws={}'.format(ws_array[i])
        fig.suptitle(title)
        fig.canvas.set_window_title(title)
    plt.show()

if __name__ == '__main__':
    main()
