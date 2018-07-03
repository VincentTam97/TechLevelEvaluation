import numpy as np
import pandas as pd
from scipy.optimize import leastsq
import pylab as pl

x = np.arange(1, 28, 1)
y = np.array([
53500, 52900, 53200, 51800, 47800, 45500, 45100, 43400, 41800, 41600, 38100, 37400, 46100, 39400, 42300, 43900, 45100, 41800, 44700, 47400, 51100, 47600, 47500, 46900, 47300, 48000, 43200
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
