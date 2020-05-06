# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:28:56 2020

@author: A_Santos
"""

def getRoot_FakePositionMethod(x_low, x_high, error_a, equation):
    import numpy as np
    import math
    iterations = 0
    error_a_iterations = math.nan
    x_c_previous = 0
    x_low_stored = x_low
    x_high_stored = x_high
    no_root = False
    while((error_a_iterations > error_a) or (math.isnan(error_a_iterations))):
        x_c_current = x_high - ((equation(x_high)*(x_low - x_high))/(equation(x_low) - equation(x_high)))
        f_x_low = equation(x_low)
        f_x_high = equation(x_high)
        f_x_c = equation(x_c_current)
        if (f_x_low*f_x_c < 0):
            x_high = x_c_current
        elif (f_x_high*f_x_c < 0):
            x_low = x_c_current
        elif ((f_x_high*f_x_c == 0) or (f_x_low*f_x_c == 0)):
            print("Exact root was found")
            no_root = True
            break
        else:
            print("There is not root in this range")
            x_c_current = math.nan
            no_root = True
            break
        if (iterations > 0):
            error_a_iterations = np.abs((x_c_current - x_c_previous)/x_c_current)*100
        print("Iteration =", iterations, \
              "  x_low =", round(x_low_stored, 5), \
              "  x_high=", round(x_high_stored, 5), \
              "  x_root_approx =", round(x_c_current, 5), \
              "  relative_error", round(error_a_iterations, 5))
        x_c_previous = x_c_current
        x_low_stored = x_low
        x_high_stored = x_high
        iterations += 1
    
    if (no_root == False):
        print("\nx_root_approx =", x_c_current, "whit relative_error = (+/-)", error_a, "%")
    return x_c_current

def getRoot_FakePositionMethodImproved(x_low, x_high, error_a, equation):
    import numpy as np
    import math
    iterations = 0
    error_a_iterations = math.nan
    x_c_previous = 0
    x_low_stored = x_low
    x_high_stored = x_high
    no_root = False
    counter_f_x_low = 0
    counter_f_x_high = 0
    f_x_low = equation(x_low)
    f_x_high = equation(x_high)
    while((error_a_iterations > error_a) or (math.isnan(error_a_iterations))):
        x_c_current = x_high - ((f_x_high*(x_low - x_high))/(f_x_low - f_x_high))
        f_x_c = equation(x_c_current)
        if (f_x_low*f_x_c < 0):
            counter_f_x_high = 0
            x_high = x_c_current
            f_x_high = equation(x_high)
            counter_f_x_low += 1
            if(counter_f_x_low >= 2):
                f_x_low = f_x_low/2
        elif (f_x_high*f_x_c < 0):
            counter_f_x_low = 0
            x_low = x_c_current
            f_x_low = equation(x_low)
            counter_f_x_high += 1
            if(counter_f_x_high >= 2):
                f_x_high = f_x_high/2
        elif ((f_x_high*f_x_c == 0) or (f_x_low*f_x_c == 0)):
            print("Exact root was found")
            no_root = True
            break
        else:
            print("There is not root in this range")
            x_c_current = math.nan
            no_root = True
            break
        if (iterations > 0):
            error_a_iterations = np.abs((x_c_current - x_c_previous)/x_c_current)*100
        print("Iteration =", iterations, \
              "  x_low =", round(x_low_stored, 5), \
              "  x_high=", round(x_high_stored, 5), \
              "  x_root_approx =", round(x_c_current, 5), \
              "  relative_error", round(error_a_iterations, 5))
        x_c_previous = x_c_current
        x_low_stored = x_low
        x_high_stored = x_high
        iterations += 1
    
    if (no_root == False):
        print("\nx_root_approx =", x_c_current, "whit relative_error = (+/-)", error_a, "%")
    return x_c_current

def plotFunctionAndRoot(x_low, x_high, x_root_approx, equation):
    import matplotlib.pyplot as plt
    import numpy as np
    import math
    x = np.linspace((x_low - 0.05*np.abs(x_high - x_low)), (x_high + 0.05*np.abs(x_high - x_low)), num = 1000)
    f_x = []
    for i in range(len(x)):
        f_x.append(equation(x[i]))
    
    plt.plot(x, f_x)
    if not(math.isnan(x_root_approx)):
        plt.scatter(x_root_approx, 0, color = 'r')
    plt.grid()
    plt.axvline(x_low, color = 'r')
    plt.axvline(x_high, color = 'r')
    plt.axhline(color = 'k')
    plt.show()