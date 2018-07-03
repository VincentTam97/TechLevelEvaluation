import numpy as np
import pandas as pd
from scipy.optimize import leastsq
import pylab as pl
import Utilities as util

x = np.arange(1, 28, 1)
y = np.array([
    226, 265, 279, 369, 437, 906, 1530, 2150, 2960, 3620, 4830, 6400, 8950, 10900, 12100, 13400, 14900, 14900, 15900, 16900, 18600, 19200, 20600, 21800, 22100, 21600, 18100
])

y_pred = util.predictWithPolyFunction(x, y)
start_year = 0
print(util.getPeriod1(y_pred) + start_year)
print(util.getPeriod2(y_pred) + start_year)
print(util.getPeriod3(y_pred) + start_year)
print(util.getPeriod4(y_pred) + start_year)
