import numpy as np
import pandas as pd
from scipy.optimize import leastsq
import pylab as pl

x = np.arange(1, 28, 1)
y = np.array([
226, 265, 279, 369, 437, 906, 1530, 2150, 2960, 3620, 4830, 6400, 8950, 10900, 12100, 13400, 14900, 14900, 15900, 16900, 18600, 19200, 20600, 21800, 22100, 21600, 18100
])


z1 = np.polyfit(x, y, 3)
z2 = np.polyfit(x, y, 4)

p1 = np.poly1d(z1)
p2 = np.poly1d(z2)

fu_x = np.arange(1, 28, 1)
fu_y = p1(fu_x)
df = pd.DataFrame(fu_y)

print(df, df.diff(), df.diff().diff())

pl.plot(x, y, 'b^', label='Origin Dots')
pl.plot(fu_x, p1(fu_x), 'gv--', label='Poly Fitting Line(deg=3)')
#pl.plot(fu_x, p2(fu_x), 'r*-', label='Poly Fitting Line(deg=4)')
pl.axis([0, 30, y.min(), y.max()])
pl.legend()
pl.savefig('scipy02.png', dpi=100)
