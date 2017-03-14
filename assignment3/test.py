from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value

f = LpVariable("f", 0, 110000)
h = LpVariable("h", 0)

prob = LpProblem("myProblem", LpMaximize)
prob += 1.2*f + 1.4*h
prob += 1.5*f + h <= 180000
prob += f + 2*h <= 240000
prob += f <= 110000

status = prob.solve()

print status

print "f: {0}, h: {1}".format(value(f), value(h))

print LpStatus[status]
