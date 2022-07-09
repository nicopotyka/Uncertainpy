class Models:
    def __init__(self, BAG=None, approximator=None, aggregation=None, influence=None, arguments=[], argument_strength=[], attacker=[], supporter=[], name="") -> None:
        self.BAG = BAG
        self.approximator = approximator
        self.aggregation = aggregation
        self.influence = influence
        self.arguments = arguments
        self.argument_strength = argument_strength
        self.attacker = attacker
        self.supporter = supporter
        self.name = name

    def solve(self, delta, epsilon, verbose=True, generate_plot=False):
        result = self.approximator.approximate_solution(delta, epsilon, verbose, generate_plot)
        return result

    def __repr__(self, name) -> str:
        return f"{name}({self.BAG}, {self.approximator}, {self.arguments}, {self.argument_strength}, {self.attacker}, {self.supporter})"

    def __str__(self, name) -> str:
        return f"{name} - BAG: {self.BAG}, Approximator: {self.approximator}, Arguments: {self.arguments}, Argument strength: {self.argument_strength}, Attacker: {self.attacker}, Supporter: {self.supporter})"
