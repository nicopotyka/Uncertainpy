import os
import re
import string
from .Argument import Argument
from .Support import Support
from .Attack import Attack


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
                        argument = Argument(k_args[0], float(k_args[1]))
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

    def get_arguments(self):
        return list(self.arguments.values())

    def __str__(self) -> str:
        return f"BAG set to read from {self.path} with arguments: {self.arguments}, attacks: {self.attacks} and supports: {self.supports}"

    def __repr__(self) -> str:
        return f"BAG({self.path}) Arguments: {self.arguments} Attacks: {self.attacks} Supports: {self.supports}"
