import uncertainpydev.argumentation as arg
from uncertainpydev.argumentation import Argument
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

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
delta = 10e-2
epsilon = 10e-4
result = model.solve(delta, epsilon, True, True)

# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
fig, ax = plt.subplots()
for x in model.approximator.graph_data:
    x_values = [x[0] for x in model.approximator.graph_data[x]]
    y_values = [y[1] for y in model.approximator.graph_data[x]]
    ax.plot(x_values, y_values, label=x)

ax.set_xlabel('Time (t)')  # Add an x-label to the axes.
ax.set_ylabel('Strength (t)')  # Add a y-label to the axes.
ax.set_title(f"Evolution Qudaratic Energy Model, RK4, d={delta}, e={epsilon}")  # Add a title to the axes.
ax.legend();  # Add a legend.

plt.show()