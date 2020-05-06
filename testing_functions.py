# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:39:07 2020

@author: A_Santos
"""

import matplotlib.pyplot as plt
import numpy as np
import math

def equation(x):
    return np.log(x)

x = np.linspace(0, 5, num = 100)

f_x = []

for i in range(len(x)):
    f_x.append(equation(x[i]))

x_low = 0.5
x_high = 4

plt.plot(x, f_x)
plt.scatter(x_low, equation(x_low), color = 'y')
plt.scatter(x_high, equation(x_high), color = 'y')
plt.plot(([x_low, x_high]), ([equation(x_low), equation(x_high)]), color = 'r')
plt.grid()
plt.axhline(color = 'k')
plt.axvline(color = 'k')
plt.show()

#%%
import matplotlib.pyplot as plt
import numpy as np
import math
from bisectionMethod_tools import *

def equation(x):
    return x**2 - 1

x_root = getRoot_BisectionMethod(-2, 2, 0.01, equation)
plotFunctionAndRoot(-2, 2, x_root, equation)

#%%
import matplotlib.pyplot as plt
import numpy as np
import math
from fakePositionMethod_tools import *

def equation(x):
    return x**10 - 1

x_root = getRoot_FakePositionMethod(0, 1.5, 0.01, equation)
plotFunctionAndRoot(0, 1.5, x_root, equation)

#%%
import matplotlib.pyplot as plt
import numpy as np
import math
from fakePositionMethod_tools import *

def equation(x):
    return x**10 - 1

x_root = getRoot_FakePositionMethodImproved(0, 1.5, 0.01, equation)
plotFunctionAndRoot(0, 1.5, x_root, equation)