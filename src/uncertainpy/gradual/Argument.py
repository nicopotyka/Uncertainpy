class Argument:
    def __init__(self, name, initial_weight, strength=None, attackers=None, supporters=None):
        self.name = name
        self.initial_weight = initial_weight
        self.strength = strength
        self.attackers = attackers
        self.supporters = supporters

        if type(initial_weight) != int and type(initial_weight) != float:
            raise TypeError("initial_weight must be of type integer or float")

        if strength is None:
            self.strength = initial_weight

        if attackers is None:
            self.attackers = {}

        if supporters is None:
            self.supporters = {}

    def get_name(self):
        return self.name

    def add_attacker(self, attacker, attack_weight=1):
        self.attackers[attacker] = attack_weight

    def add_supporter(self, supporter, support_weight=1):
        self.supporters[supporter] = support_weight

    def get_initial_weight(self):
        return self.initial_weight
        
    def reset_initial_weight(self, weight):
        self.initial_weight = weight
        
    def __repr__(self) -> str:
        return f"Argument {self.name}: initial weight {self.initial_weight}, strength {self.strength}, attackers {self.attackers}, supporters {self.supporters}"

    def __str__(self) -> str:
        return f"Argument(name={self.name}, weight={self.initial_weight}, strength={self.strength})"
