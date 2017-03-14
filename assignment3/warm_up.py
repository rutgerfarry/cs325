from pulp import LpVariable, LpProblem, LpMaximize, LpMinimize, LpStatus, value
import numpy as np

points = np.array([[1, 2, 3, 5, 7, 8, 10], 
                 [3, 5, 7, 11, 14, 15, 19]])

prob = LpProblem("warmUp", LpMinimize)

m = LpVariable("m")
a = LpVariable("a")
b = LpVariable("b")
prob += m

# Make each point a constraint
for i in range(points.shape[1]):
    prob += a*points[0][i]+b-points[1][i] <= m
    prob += -a*points[0][i]-b+points[1][i] <= m
    
status = prob.solve()
print status, LpStatus[status]
print "a: {0} b: {1}".format(value(a), value(b))
