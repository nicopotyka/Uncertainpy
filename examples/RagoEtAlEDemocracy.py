import uncertainpydev.argumentation as arg
from uncertainpydev.argumentation.graphing import graph

DELTA = 10e-2
EPSILON = 10e-4

model = arg.systems.QuadraticEnergyModel()
model.approximator = arg.approximations.PlottingRK4(model)
model.BAG = arg.BAG("./BAG/RagoEtAlEDemocracy.bag")

result = model.solve(DELTA, EPSILON, True, True)
plot = graph(model, DELTA, EPSILON)
plot.show()