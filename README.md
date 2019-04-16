# Analog filter design examples

## System requirements

Python3, numpy, scipy and matplotlib are required.
Ubuntu install instructions:

```bash
sudo apt update
sudo apt install python3-pip
pip3 install --user numpy scipy matplotlib
```

## filter_utils lib

It contains some utility functions, combining the power of scipy.signal and matplotlib.

## Example descriptions

`cheby_example`
:
Design example of a Chebyshev type 1 filter.

`butter_cheby_comparison`
:
Comparison between order 5 Chebyshev and Butterworth filters.

`comparison_order_butter_cheby`
:
Plots comparing the order of Chebyshev and Butterworth filters of same specs.
