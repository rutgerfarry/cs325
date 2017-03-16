from pulp import LpVariable, LpProblem, LpMinimize, LpStatus, value

def warm_up():
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
    print "Status: " + LpStatus[status]
    print "a: " + str(value(a))
    print "b: " + str(value(b))

# Prevent running if imported as a module
if __name__ == "__main__":
    warm_up()
