class Attack:
    def __init__(self, attacker, attacked, weight=1) -> None:
        self.attacker = attacker
        self.attacked = attacked
        self.weight = weight

    def get_attacker(self):
        return self.attacker

    def get_attacked(self):
        return self.attacked

    def get_weight(self):
        return self.weight

    def __repr__(self) -> str:
        return f"Attack({self.attacker}, {self.attacked}, weight={self.weight})"

    def __str__(self) -> str:
        return f"Attack by {self.attacker} to {self.attacked} with weight {self.weight}"
