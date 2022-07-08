import os
import re

class Argument:
    def __init__(self, name, initial_weight, strength=None, attackers=[], supporters=[]) -> None:
        self.name= name
        self.initial_weight = initial_weight
        self.strength = strength
        self.attackers = attackers
        self.supporters = supporters

        if strength is None:
            self.strength = initial_weight

    def get_name(self):
        return self.name

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
                k_args = re.findall(rf"{k_name}\((.*?)\)", line)[0].split(",")
                
                if k_name == "arg":
                    argument = Argument(k_args[0], k_args[1])
                    self.arguments[Argument.name] = argument
                
                elif k_name == "att":
                    
                    attacker = argument_hashmap[k_args[0]]
                    attacked = argument_hashmap[k_args[1]]
                    self.add_attack(attacker, attacked)


                elif k_name == "sup":
                    supporter = argument_hashmap[k_args[0]]
                    supported = argument_hashmap[k_args[1]]
                    self.add_support(attacker, attacked)

    def addAttack(self, attacker, attacked):
        self.arguments.put(attacker.getName(), attacker);
        self.arguments[attacker.name]
		arguments.put(attacked.getName(), attacked);
		attacked.addAttacker(attacker);
		attacks.add(new Attack(attacker, attacked));