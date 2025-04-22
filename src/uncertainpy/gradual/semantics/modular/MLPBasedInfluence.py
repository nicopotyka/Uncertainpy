import math

class MLPBasedInfluence:
    def __init__(self) -> None:
        pass

    def compute_strength(self, weight, aggregate):
        epsilon = 1e-10  # avoid weight=0 or 1
        weight = max(epsilon, min(1 - epsilon, weight))
        logit_weight = math.log(weight / (1 - weight))
        return 1 / (1 + math.exp(- logit_weight - aggregate))

    def __str__(self) -> str:
        return __class__.__name__