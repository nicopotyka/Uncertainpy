import uncertainpy.argumentation as arg
from uncertainpy.argumentation.graphing import graph

DELTA = 10e-2
EPSILON = 10e-4

model = arg.systems.QuadraticEnergyModel()
model.approximator = arg.approximators.RK4(model)
model.BAG = arg.BAG("./BAG/RagoEtAlEDemocracy.bag")

result = model.solve(DELTA, EPSILON, True, True)
plot = graph(model, DELTA, EPSILON)
plot.show()