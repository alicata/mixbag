#!/usr/bin/python

import sys
import numpy as np
from matplotlib import pyplot as plt

# ------------------------
# ts        c1      c2
# ------------------------
# 166.0     549     221
# 167.0     553     221
# 168.0     555     213

def main(argv):
    ts = []
    c1 = []
    c2 = []

    filename = str(argv[0])

    with open(filename) as f:
        for line in f:
            data = line.split()
            ts.append(float(data[0]))
            c1.append(int(data[1]))
            c2.append(int(data[2]))

    for i in xrange(len(ts)):
        print ("%f %d %d" % (ts[i], c1[i], c2[i]))

    with plt.style.context('fivethirtyeight'):
        plt.plot(ts, c1)
        plt.plot(ts, c2)

    plt.show()


if __name__ == "__main__":
    
    if (len(sys.argv)<2):
        print 'usage %s datafile' % sys.argv[0]
        exit()

    main(sys.argv[1:])