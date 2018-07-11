import numpy as np
import pandas as pd
from scipy.optimize import leastsq
import pylab as pl
import SingleFileVersion as util
import AnalysisUtilities as AU

x = np.arange(1, 28, 1)
y = [0, 0, 20, 56, 78, 150, 168, 144, 200, 270, 360, 400, 269, 185, 75, 25, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


start_year = 1990
AU.analyseDBContent()