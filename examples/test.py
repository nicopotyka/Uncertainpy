import uncertainpydev.argumentation as arg

model = arg.systems.QuadraticEnergyModel
approximation = arg.approximations.RK4
BAG = arg.BAG("example.bag")

arg_system = arg.System(model, approximation, BAG)

result = arg.solve(arg_system, delta=10e-2, epsilon=10e-4, verbose=True)
print(arg_system)
print(repr(arg_system))
print(result)

print(repr(BAG))
print("\n\n")
print(str(BAG))