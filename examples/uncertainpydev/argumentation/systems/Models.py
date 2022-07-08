class Models:
    def __init__(self) -> None:
        pass


    def run(state):
        derivatives = [];
		
		for i in self. {
			
			double energy = 0;
			for(int s: supporter[i]) {
				energy += state[s];
			}
			for(int a: attacker[i]) {
				energy -= state[a];
			}

			double weight = arguments[i].getInitialWeight();
			double derivative = weight;
			double squaredEnergy = energy * energy;
			if(energy>0) {
				derivative += (1 - weight) * squaredEnergy / (1 + squaredEnergy);
			}
			else if(energy < 0) {
				derivative -= weight * squaredEnergy  / (1 + squaredEnergy);
			}
			derivative -= state[i];
			
			derivatives[i] = derivative;
			
		}
		

		return derivatives;