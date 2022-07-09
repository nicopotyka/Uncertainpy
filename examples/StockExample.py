import uncertainpy.argumentation as arg

model = arg.systems.QuadraticEnergyModel()
model.approximator = arg.approximators.RK4(model)
model.BAG = arg.BAG("./BAG/stock_example.bag")

result = model.solve(delta=10e-2, epsilon=10e-4, verbose=True, generate_plot=False)
