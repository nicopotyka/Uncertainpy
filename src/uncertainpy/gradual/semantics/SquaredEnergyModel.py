from .Model import Model


class SquaredEnergyModel(Model):
    def __init__(self, aggregation=None, influence=None, BAG=None, approximator=None, arguments=..., argument_strength=..., attacker=..., supporter=..., name="") -> None:
        super().__init__(BAG, approximator, aggregation, influence, arguments, argument_strength, attacker, supporter, name)
        self.name = __class__.__name__

    def compute_derivative_at(self, state):
        derivatives = {}

        for arg in self.arguments:
            energy = 0

            for s in self.supporter[arg]:
                energy += state[s]**2

            for a in self.attacker[arg]:
                energy -= state[a]**2

            weight = arg.initial_weight

            derivative = weight

            if energy > 0:
                derivative += (1 - weight) * (energy / (1 + energy))
            elif energy < 0:
                derivative += weight * (energy / (1 - energy))

            derivative -= state[arg]
            derivatives[arg] = derivative

        return derivatives

    def __repr__(self) -> str:
        return super().__repr__(__name__)

    def __str__(self) -> str:
        return super().__str__(__name__)
