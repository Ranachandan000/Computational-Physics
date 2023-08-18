#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Choose an interval [a, b] where the function changes sign.
#2. Calculate the midpoint c = (a + b) / 2 and evaluate f(c).
#3. If |f(c)| ≤ ε, c is an acceptable root approximation.
#4. If f(c) and f(a) have different signs, update a = c.
#5. If f(c) and f(b) have different signs, update b = c.
#6. Repeat steps 2-5 until |f(c)| ≤ ε.
#7. The final c is an approximation of the root within the tolerance ε.


# In[1]:


def bisection_method(func, a, b, error, max_iter):
    if func(a) * func(b) >= 0:
        raise ValueError("Function values at 'a' and 'b' must have different signs.")
    
    iter_count = 0
    while (b - a) / 2 > error and iter_count < max_iter:
        c = (a + b) / 2
        if func(c) == 0:
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    
    return (a + b) / 2

# Example usage:
def example_function(x):
    return x**2 - 4

a = 1.0
b = 3.0
tolerance = 1e-6
max_iterations = 100

root = bisection_method(example_function, a, b, tolerance, max_iterations)
print("Approximate root:", root)
print("Function value at root:", example_function(root))


# In[2]:


def bisection_method(func, a, b, tol):
    if func(a) * func(b) >= 0:
        raise ValueError("Function values at 'a' and 'b' must have different signs.")
    
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if func(c) == 0:
            return c
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
    
    return (a + b) / 2

# Example usage:
def custom_function(x):
    return x**3 - 6*x**2 + 11*x - 6

a = 0.0
b = 4.0
tolerance = 1e-5

root = bisection_method(custom_function, a, b, tolerance)
print("Approximate root:", root)
print("Function value at root:", custom_function(root))


# In[3]:


import matplotlib.pyplot as plt


# In[6]:


x = []
y = []
for i in range(0,40, 1):
    Y = custom_function(i)
    x.append(i)
    y.append(y)


# In[ ]:


plt.plot(x ,y)


# In[ ]:




