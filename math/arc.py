import numpy as np
#example
x = [1,1]
y= [-1,1]
A = ([(2,-1), (-1, 4)])
Angle = x.T@A@y /(x.T@A@x * y.T@A@y)**1/2
print(Angle)
