import uncertainpydev.argumentation as arg
from uncertainpydev.argumentation import Argument
from uncertainpydev.argumentation.graphing import graph

DELTA = 10e-2
EPSILON = 10e-4
N = 10

model = arg.systems.QuadraticEnergyModel()
BAG = arg.BAG()

a = Argument("A", 1)
b = []
for i in range(N):
    b.append(Argument(f"B{i}", 0))

c = []
for i in range(N):
    c.append(Argument(f"C{i}", 0))

for i in range(N):
    BAG.add_support(a, b[i])
    for j in range(N):
        BAG.add_support(b[i], c[j])
        BAG.add_attack(c[j], a)

model.approximator = arg.approximations.PlottingRK4(model)
model.BAG = BAG
result = model.solve(DELTA, EPSILON, True, True)

plot = graph(model, DELTA, EPSILON)
plot.show()
