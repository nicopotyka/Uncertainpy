class Approximations:
    def __init__(self, ads, time=0, arguments=[], argument_strength=[], attacker=[], supporter=[]) -> None:
        self.ads = ads
        self.time = time
        self.arguments = arguments
        self.argument_strength = argument_strength
        self.attacker = attacker
        self.supporter = supporter

    def initialise_arrays(self):
        argument_set = self.ads.BAG.arguments
        arg_to_index = {}

        arguments = []
        argument_strength = []

        for z, a in enumerate(argument_set.values()):
            arguments.append(a)
            argument_strength.append(a.strength)
            arg_to_index[a] = z

        attacker = []
        supporter = []

        for a in argument_set.values():
            a_index = []

            attacker_child = []
            for z, b in enumerate(a.attackers):
                attacker_child.append(arg_to_index[b])

            attacker.append(attacker_child)

            supporter_child = []
            for z, b in enumerate(a.supporters):
                supporter_child.append(arg_to_index[b])

            supporter.append(supporter_child)

        self.ads.arguments = arguments
        self.ads.argument_strength = argument_strength
        self.ads.attacker = attacker
        self.ads.supporter = supporter

    def rewrite_arrays(self):
        for i in range(len(self.arguments)):
            self.arguments[i].strength = self.argument_strength[i]

    def perform_iteration(delta, epsilon):
        return None

    def approximate_solution(self, delta, epsilon, verbose):
        self.initialise_arrays()

        time = 0
        max_derivative = 0
        print(epsilon)
        while True:
            max_derivative = self.perform_iteration(delta, epsilon)
            print(max_derivative)
            time += delta

            if(max_derivative > epsilon):
                break

        self.rewrite_arrays()

        if (verbose):
            print(f"{self.ads.name}\nTime: {time}{', '.join([x for x in self.arguments])}\n")
