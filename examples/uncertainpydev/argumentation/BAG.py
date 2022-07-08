import os
import re
import string

class Attack:
    def __init__(self, attacker, attacked) -> None:
        self.attacker = attacker
        self.attacked = attacked
    
    def get_attacker(self):
        return self.attacker

    def get_attacked(self):
        return self.attacked

    def __repr__(self) -> str:
        return f"Attack({self.attacker}, {self.attacked})"

    def __str__(self) -> str:
        return f"Attack by {self.attacker} to {self.attacked}"

class Support:
    def __init__(self, supporter, supported) -> None:
        self.supporter = supporter
        self.supported = supported
    
    def get_supporter(self):
        return self.supporter

    def get_supported(self):
        return self.supported

class Argument:
    def __init__(self, name, initial_weight, strength=None, attackers=[], supporters=[]) -> None:
        self.name = name
        self.initial_weight = initial_weight
        self.strength = strength
        self.attackers = attackers
        self.supporters = supporters

        if strength is None:
            self.strength = initial_weight

    def get_name(self):
        return self.name

    def add_attacker(self, attacker):
        self.attackers.append(attacker)
        
    def add_supporter(self, supporter):
        self.supporters.append(supporter)
    
    def __repr__(self) -> str:
        return f"Argument {self.name}: initial weight {self.initial_weight}, strength {self.strength}, attackers {self.attackers}, supporters {self.supporters}"

    def __str__(self) -> str:
        return f"Argument({self.name}, {self.initial_weight}, {self.strength}, {self.attackers}, {self.supporters})"

class BAG:
    # {Name: Argument}
    arguments = {}
    attacks = []
    supports = []

    def __init__(self, path) -> None:
        self.path = path

        with open(os.path.abspath(path), "r") as f:
            for line in f.readlines():
                k_name = line.split("(")[0]
                if k_name in string.whitespace:
                    pass
                else:
                    k_args = re.findall(rf"{k_name}\((.*?)\)", line)[0].replace(" ", "").split(",")
                    
                    if k_name == "arg":
                        argument = Argument(k_args[0], k_args[1])
                        self.arguments[argument.name] = argument
                    
                    elif k_name == "att":
                        attacker = self.arguments[k_args[0]]
                        attacked = self.arguments[k_args[1]]
                        self.add_attack(attacker, attacked)


                    elif k_name == "sup":
                        supporter = self.arguments[k_args[0]]
                        supported = self.arguments[k_args[1]]
                        self.add_support(attacker, attacked)


    def add_attack(self, attacker, attacked):
        self.arguments[attacker.name] = attacker
        self.arguments[attacked.name] = attacked
        attacked.add_attacker(attacker)

        self.attacks.append(Attack(attacker, attacked))

    def add_support(self, supporter, supported):
        self.arguments[supporter.name] = supporter
        self.arguments[supported.name] = supported
        supported.add_supporter(supporter)

        self.supports.append(Support(supporter, supported))

    def __str__(self) -> str:
        return f"BAG set to read from {self.path} with arguments: {self.arguments}, attacks: {self.attacks} and supports: {self.supports}"

    def __repr__(self) -> str:
        return f"BAG({self.path}) Arguments: {self.arguments} Attacks: {self.attacks} Supports: {self.supports}"
