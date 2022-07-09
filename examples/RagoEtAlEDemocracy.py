from matplotlib import pyplot as plt
import uncertainpydev.argumentation as arg

model = arg.systems.QuadraticEnergyModel()
model.approximator = arg.approximations.PlottingRK4(model)
model.BAG = arg.BAG("./BAG/RagoEtAlEDemocracy.bag")
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
ax.legend()  # Add a legend.

plt.show()