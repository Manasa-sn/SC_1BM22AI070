# Ant Colony Optimization

import numpy as np

def objective_function(x):
    return np.sum(x**2)

class Ant:
    def __init__(self, num_vars, bounds, alpha=1, beta=1):
        self.pos = np.random.uniform(bounds[:, 0], bounds[:, 1], num_vars)
        self.alpha = alpha
        self.beta = beta

    def choose_next_position(self, pheromones, bounds):
        num_vars = len(bounds)
        probabilities = np.zeros(num_vars)

        for i in range(num_vars):
            eta = 1/(np.abs(self.pos[i]) + 1e-10)
            probabilities[i] = (pheromones[i] ** self.alpha) * (eta ** self.beta)

        probabilities /= np.sum(probabilities)
        next_var = np.random.choice(np.arange(num_vars), p = probabilities)
        self.pos[next_var] = np.random.uniform(bounds[next_var, 0], bounds[next_var, 1])
        self.pos = np.clip(self.pos, bounds[:, 0], bounds[:, 1])

def ant_colony_optimization(func, bounds,num_ants=10,max_iter=100,alpha=1,beta=1,evaporation_rate=0.5):
    num_vars = len(bounds)
    bounds = np.array(bounds)
    pheromones = np.ones(num_vars)
    best_position = None
    best_value = float('inf')
    for _ in range(max_iter):
        ants = [Ant(num_vars, bounds, alpha, beta ) for _ in range(num_ants)]
        for ant in ants:
            ant.choose_next_position(pheromones, bounds)
            current_value = func(ant.pos)
            if current_value < best_value:
                best_value = current_value
                best_position = ant.pos.copy()
            pheromones *= (1- evaporation_rate)
            for ant in ants:
                pheromones += 1/(1+func(ant.pos))

    return best_position, best_value

bounds = np.array([(-5, 5), (-5, 5)])
best_pos, best_value = ant_colony_optimization(objective_function, bounds)
print(f'Best Position: {best_pos}')
print(f'Best Value: {best_value}')

