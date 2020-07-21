import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import sympy as syp

c_a = 0.5
c_b = 1.0
K_a = 1.77*10**-4
y = syp.symbols("y")
x = syp.symbols("x")

no1_method = syp.Eq(K_a * (c_a + y - x),(c_b - y + x) * x )
no2_method = syp.Eq(K_a * (c_a - x),(c_b + x) * (x + y))

no1_ans = syp.solve(no1_method, x)
no2_ans = syp.solve(no2_method, x)

print(no1_ans)
print(no2_ans)
