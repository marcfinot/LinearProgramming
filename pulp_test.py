import pulp
x = pulp.LpVariable("x", 0, 3)
y = pulp.LpVariable("y", 0, 1)
prob = pulp.LpProblem("myProblem", pulp.LpMinimize)
prob += x + y <= 2
prob += -4*x + y
status = prob.solve(pulp.solvers.GUROBI_CMD())
pulp.LpStatus[status]
pulp.value(x)
pulp.value(y)

