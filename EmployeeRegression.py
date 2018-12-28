import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import statsmodels.api as sm


def make_error(x, y):
    add = sm.add_constant(x)
    model = sm.OLS(y, add).fit()
    m = model.params[1]
    b = model.params[0]
    desv_std = np.std(y)
    coef_corr = np.corrcoef(x, y)[0][1]
    err = desv_std * math.sqrt(1 - coef_corr ** 2)
    points = np.linspace(x.min(), x.max())
    plt.plot(points, m * points + b)
    plt.plot(points, m * points + (b + err))
    plt.plot(points, m * points + (b - err))
    print(err)


data1 = pd.read_csv('empleados.csv')
y1 = data1.received
x1 = data1.requested
fig = plt.plot(x1, y1, 'x')
div1 = 6
plt.axvline(div1, color='k')
data2 = data1[(data1.requested <= div1)]
x2 = data2.requested
y2 = data2.received
make_error(x2, y2)
data3 = data1[(data1.requested > div1)]
x3 = data3.requested
y3 = data3.received
make_error(x3, y3)
plt.show()
