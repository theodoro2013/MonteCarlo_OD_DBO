import random
import matplotlib.pyplot as plt
import numpy as np
import time
k1v = []
kdv = []
k2tv = []


totalsimulacao=5

for c in range(0,totalsimulacao):
    k1= random.uniform(0.55,0.96)
    kd= random.uniform(0.55,1.91)
    k2t= random.uniform(5.73,11.89)
    k1v.append(k1)
    kdv.append(k1)
    k2tv.append(k1)

 
print(k1v,kdv,k2tv)
