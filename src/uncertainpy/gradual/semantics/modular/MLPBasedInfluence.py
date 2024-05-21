import math

class MLPBasedInfluence:
    def __init__(self) -> None:
        pass

    def compute_strength(self, weight, aggregate):
        return 1/(1 + math.exp(- math.log(weight/(1-weight)) - aggregate))

    def __str__(self) -> str:
        return __class__.__name__