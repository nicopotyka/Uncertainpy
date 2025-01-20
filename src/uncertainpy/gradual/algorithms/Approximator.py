class Approximator:
    graph_data = {}

    def __init__(self, ads, time=0, arguments=[], argument_strength={}, attacker={}, supporter={}, name="") -> None:
        self.ads = ads
        self.time = time
        self.arguments = arguments
        self.argument_strength = argument_strength
        self.attacker = attacker
        self.supporter = supporter
        self.name = name

    def initialise_arrays(self):
        argument_set = list(self.ads.BAG.arguments.values())
        arguments = []
        argument_strength = {}

        for a in argument_set:
            arguments.append(a)
            argument_strength[a] = a.strength

        attacker = {}
        supporter = {}

        for a in argument_set:

            attacker_child = {}
            for b in a.attackers:
                attacker_child[b] = a.attackers[b]

            attacker[a] = attacker_child

            supporter_child = {}
            for b in a.supporters:
                supporter_child[b] = a.supporters[b]

            supporter[a] = supporter_child

        self.ads.arguments = arguments
        self.ads.argument_strength = argument_strength
        self.ads.attacker = attacker
        self.ads.supporter = supporter

    def rewrite_arrays(self):
        for a in self.ads.arguments:
            a.strength = self.ads.argument_strength[a]

    def perform_iteration(delta, epsilon):
        return None

    def initialise_graph_data(self):
        for argument in self.ads.arguments:
            self.graph_data[argument.name] = [(0, argument.initial_weight)]

    def update_graph_data(self, time):
        for argument in self.ads.arguments:
            self.graph_data[argument.name].append((time, self.ads.argument_strength[argument]))

    def approximate_solution(self, delta, epsilon, verbose=False, generate_plot=False):
        self.initialise_arrays()

        if generate_plot:
            self.initialise_graph_data()

        time = 0
        time_limit = 99999999999
        max_derivative = 0

        while True:
            max_derivative = self.perform_iteration(delta, epsilon)
            time += delta

            if generate_plot:
                self.update_graph_data(time)

            if(max_derivative < epsilon or time >= time_limit):
                break

        self.rewrite_arrays()

        if (verbose):
            print_args = '\n'.join([str(x) for x in self.ads.arguments])
            print(f"{self.ads.name}, {self.ads.approximator.name}\nTime: {time}\n{print_args}\n")

        return max_derivative
