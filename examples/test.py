import uncertainpydev.argumentation as arg

model = arg.systems.QuadraticEnergyModel()
model.approximator = arg.approximations.RK4(model)
model.BAG = arg.BAG("example.bag")


result = model.solve(delta=10e-2, epsilon=10e-4, verbose=True)
print(result)
