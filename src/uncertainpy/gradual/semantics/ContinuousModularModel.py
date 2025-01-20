from .Model import Model


class ContinuousModularModel(Model):
    def __init__(self, aggregation=None, influence=None, BAG=None, approximator=None, arguments=..., argument_strength=..., attacker=..., supporter=..., name="") -> None:
        super().__init__(BAG, approximator, aggregation, influence, arguments, argument_strength, attacker, supporter, name)
        self.name = __class__.__name__

    def compute_derivative_at(self, state):
        derivatives = {}
        for a in self.arguments:
            aggregate_strength = self.aggregation.aggregate_strength(self.attacker[a], self.supporter[a], state)
            derivative = self.influence.compute_strength(a.initial_weight, aggregate_strength)
            derivative -= state[a]

            derivatives[a] = derivative

        return derivatives

    def __repr__(self) -> str:
        return super().__repr__(__name__)

    def __str__(self) -> str:
        return super().__str__(__name__)
