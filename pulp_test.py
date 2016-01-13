import pulp
x = pulp.LpVariable("x", 0, 3)
y = pulp.LpVariable("y", 0, 1)
prob = pulp.LpProblem("myProblem", pulp.LpMinimize)
prob += x + y <= 2
prob += -4*x + y
status = prob.solve(pulp.solvers.GUROBI_CMD())
print pulp.LpStatus[status]
print pulp.value(x)
print pulp.value(y)

