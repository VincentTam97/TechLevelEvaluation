import numpy as np
import pandas as pd
from scipy.optimize import leastsq
import pylab as pl
import AnalysisUtilities as util

x = np.arange(1, 28, 1)
y = np.array([
53500, 52900, 53200, 51800, 47800, 45500, 45100, 43400, 41800, 41600, 38100, 37400, 46100, 39400, 42300, 43900, 45100, 41800, 44700, 47400, 51100, 47600, 47500, 46900, 47300, 48000, 43200
])

y_pred = util.predictWithPolyFunction(x, y)
start_year = 0
print(util.getPeriod1(y_pred) + start_year)
print(util.getPeriod2(y_pred) + start_year)
print(util.getPeriod3(y_pred) + start_year)
print(util.getPeriod4(y_pred) + start_year)
