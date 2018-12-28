import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols 

data1 = pd.read_csv('Sitio1.csv')
y = data1.Ganancias
x = data1.TiempoEnSitio
x2 = sm.add_constant(x)
data_model = sm.OLS(y, x2).fit()

print(data_model.summary())

intercept, slope = data_model.params

y1 = x * slope + intercept
fig = plt.plot(x, y, 'o')
fig = plt.plot(x, y1)

print(fig)
plt.show()
