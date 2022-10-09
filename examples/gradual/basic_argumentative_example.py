import uncertainpy.argumentation as arg


arg_system = arg.system()
arg_system.model = arg.systems.QuadraticEnergyModel
arg_system.approximator = arg.approximators.RK4
arg_system.BAG = arg.BAG("./example.bag")

result = arg.solve(arg_system, delta=10e-2, epsilon=10e-4, verbose=True)
print(result)