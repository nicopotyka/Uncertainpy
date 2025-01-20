class SumAggregation:
    def __init__(self) -> None:
        pass

    def aggregate_strength(self, attackers, supporters, state):
        aggregate = 0
        for a in attackers:
            attack_weight = attackers[a]
            aggregate -= state[a] * attack_weight

        for s in supporters:
            support_weight = supporters[s]
            aggregate += state[s] * support_weight

        return aggregate
    
    def __str__(self) -> str:
        return __class__.__name__
