import math
from .Model import Model


class ContinuousEulerBasedModel(Model):
    def __init__(self, aggregation=None, influence=None, BAG=None, approximator=None, arguments=..., argument_strength=..., attacker=..., supporter=..., name="") -> None:
        super().__init__(BAG, approximator, aggregation, influence, arguments, argument_strength, attacker, supporter, name)
        self.name = __class__.__name__

    def compute_derivative_at(self, state):
        derivatives = {}

        for arg in self.arguments:
            energy = 0


            for s in self.supporter[arg]:
                energy += state[s]

            for a in self.attacker[arg]:
                energy -= state[a]

            weight = arg.initial_weight
            derivative = 1 - (1-weight**2) / (1 + weight * math.exp(energy))
            derivative -= state[arg]


            derivatives[arg] = derivative

        return derivatives

    def __repr__(self) -> str:
        return super().__repr__(__name__)

    def __str__(self) -> str:
        return super().__str__(__name__)
    
