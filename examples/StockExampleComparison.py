import uncertainpydev.argumentation as arg
from uncertainpydev.argumentation.graphing import graph

DELTA = 10e-2
EPSILON = 10e-4

models = []
plots = []

models.append(arg.systems.QuadraticEnergyModel())
models.append(arg.systems.ContinuousModularModel(arg.aggregation.SumAggregation(), arg.influence.QuadraticMaximumInfluence(conservativeness=1)))
models.append(arg.systems.ContinuousEulerBasedModel())
models.append(arg.systems.ContinuousModularModel(arg.aggregation.SumAggregation(), arg.influence.EulerBasedInfluence()))

for model in models:
    BAG = arg.BAG("./BAG/stock_example.bag")
    BAG.reset_strength_values()
    model.approximator = arg.approximations.PlottingRK4(model)
    model.BAG = BAG

    result = model.solve(delta=DELTA, epsilon=EPSILON, verbose=True, generate_plot=True)
    title = f"{model.name}, {model.approximator}, ε: {EPSILON}, δ: {DELTA}"
    if model.aggregation is not None:
        title += f"\nAGG. {model.aggregation}"
    if model.influence is not None:
        title += f" INFL. {model.influence}"

    plots.append(graph(model, DELTA, EPSILON, title))

for plot in plots:
    plot.show()
