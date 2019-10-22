"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2


def PmfMean(pmf):
    mean = 0
    for value, ratio in pmf.Items():
        mean += value * ratio
    return mean


def PmfVar(pmf):
    var = 0
    mean = PmfMean(pmf)
    for value, ratio in pmf.Items():
        var += ratio * (value - mean)**2
    return var


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    pmf = thinkstats2.Pmf(live.prglngth)

    # test PmfMean
    mean = PmfMean(pmf)
    print('Mean of preg length', mean)
    assert mean == pmf.Mean(), mean

    # test PmfVar
    var = PmfVar(pmf)
    print('Variance of preg length', var)
    assert var == pmf.Var(), var

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
