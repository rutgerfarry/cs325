from pulp import LpVariable, LpProblem, LpMaximize, LpMinimize, LpStatus, value

points = [(1, 3),
          (2, 5),
          (3, 7),
          (5, 11),
          (7, 14),
          (8, 15),
          (10, 19)]

prob = LpProblem("warmUp", LpMinimize)

m = LpVariable("m")
a = LpVariable("a")
b = LpVariable("b")
prob += m

# Make each point a constraint
for point in points:
    prob += a * point[0] + b - point[1] <= m
    prob += -a * point[0] - b + point[1] <= m
    
status = prob.solve()
print status, LpStatus[status]
print "a: {0} b: {1}".format(value(a), value(b))

