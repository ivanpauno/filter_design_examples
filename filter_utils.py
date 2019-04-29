#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ivanpauno
@description: A collection of functions for designing and plotting filters.
"""

import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt


def butter(wp, ws, gpass, gstop):
    n, wb = sig.buttord(wp, ws, gpass, gstop, analog=True)
    return sig.butter(n, wb, analog=True)


def cheby(wp, ws, gpass, gstop):
    n, _ = sig.cheb1ord(wp, ws, gpass, gstop, analog=True)
    return sig.cheby1(n, gpass, wp, analog=True)


def get_group_delay(filt):
    w, _, angle = filt.bode()
    angle = angle * np.pi / 180
    delay = -np.diff(angle)/np.diff(w)
    w = w[1:]
    return w, delay


def plot_bode(filters, *, mag=True, ang=True, gd=False):
    if mag:
        plot_magnitude(filters)
    if ang:
        plot_angle(filters)
    if gd:
        plot_group_delay(filters)


def plot_magnitude(filters):
    try:
        iter(filters)
    except TypeError:
        filters = [filters]
    fig, ax = plt.subplots()
    ax.ticklabel_format(useOffset=False)
    ax.set_ylabel('dB')
    ax.set_xlabel('rad/sec')
    ax.grid(True)
    title = 'Frequency response, magnitude'
    fig.suptitle(title)
    fig.canvas.set_window_title(title)
    for filt in filters:
        w, module, _ = filt.bode()
        ax.semilogx(w, module)


def plot_angle(filters):
    try:
        iter(filters)
    except TypeError:
        filters = [filters]
    fig, ax = plt.subplots()
    ax.ticklabel_format(useOffset=False)
    ax.set_ylabel('rad')
    ax.set_xlabel('rad/sec')
    ax.grid(True)
    title = 'Frequency response, angle'
    fig.suptitle(title)
    fig.canvas.set_window_title(title)
    for filt in filters:
        w, _, angle = filt.bode()
        angle = angle * np.pi / 180
        ax.semilogx(w, angle)


def plot_group_delay(filters):
    try:
        iter(filters)
    except TypeError:
        filters = [filters]
    fig, ax = plt.subplots()
    ax.ticklabel_format(useOffset=False)
    ax.set_ylabel('sec')
    ax.set_xlabel('rad/sec')
    ax.grid(True)
    title = 'Group delay'
    fig.suptitle(title)
    fig.canvas.set_window_title(title)
    for filt in filters:
        w, delay = get_group_delay(filt)
        ax.semilogx(w, delay)


def print_zpk(num, den):
    z, p, k = sig.tf2zpk(num, den)
    print('Poles:')
    print_pole_or_zero_info(p)
    if z.size:
        print('Zeros:')
        print_pole_or_zero_info(z)
    print('K = {}'.format(k))


def print_pole_or_zero_info(pzs):
    for pz in pzs:
        print('\t\ts = {} + j {} ; w0 = {} ; Q = {}\n'.format(
            pz.real, pz.imag, abs(pz), abs(pz)/2/pz.real))


def pzmap(filters):
    try:
        iter(filters)
    except TypeError:
        filters = [filters]
    fig, ax = plt.subplots()
    ax.ticklabel_format(useOffset=False)
    ax.set_ylabel('rad/sec')
    ax.set_xlabel('rad/sec')
    ax.grid(True)
    title = 'pzmap'
    fig.suptitle(title)
    fig.canvas.set_window_title(title)
    r = 1.5
    for filt in filters:
        z, p, k = sig.tf2zpk(filt.num, filt.den)
        poles = ax.plot(p.real, p.imag, 'x', markersize=9, alpha=0.5)
        rx = 1.5 * np.amax(np.concatenate((abs(z), abs(p))))
        r = rx if rx > r else r
        ax.plot(z.real, z.imag, 'o', color='none', markersize=9, alpha=0.5,
            markeredgecolor=poles[0].get_color())
    ax.axis('scaled')
    ax.axis([-r, r, -r, r])


def pretty(num, den):
    num = ['{} s^{}'.format(num[i], len(num)-i-1) if num[i] else '' for i in range(len(num))]
    num = ' + '.join(num)
    den = ['{} s^{}'.format(den[i], len(den)-i-1) if den[i] else '' for i in range(len(den))]
    den = ' + '.join(den)
    max_len = max(len(num), len(den))
    bar = '-' * max_len
    print('       {}{}'.format(' ' * int(max_len/2-len(num)/2), num))
    print('T(s) = {}'.format(bar))
    print('       {}{}'.format(' ' * int(max_len/2-len(den)/2), den))


def afilter(signal, filt, Ts):
    """
    Apply an analog filter to a signal.

    @signal: array_like. The signal to be processed.
    @filter: The analog filter to be applied.
    @Ts: The sampling period applied to 'signal'.

    Note: 1/Ts should be at least 3 or 4 times signal's maximum
    frecuency of interest and of the filter's maximum characteristic
    frequency, in order to get a good simulated result.
    Ten times is preferred.
    """
    num, den = sig.bilinear(filt.num, filt.den, 1/Ts)
    return sig.lfilter(num, den, signal)
