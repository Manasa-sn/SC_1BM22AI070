#ACO
import numpy as np

def aco_tsp(distances, n_ants=10, n_iterations=100, alpha=1, beta=2, evaporation=0.5):
    n_cities = len(distances)
    pheromone = np.ones((n_cities, n_cities)) / n_cities

    best_distance = float('inf')
    best_tour = None

    for _ in range(n_iterations):
        all_tours = []
        all_distances = []

        for _ in range(n_ants):
            tour = [0]  
            unvisited = set(range(1, n_cities))

            while unvisited:
                current = tour[-1]
                probs = [(pheromone[current][j] ** alpha) *
                        ((1/distances[current][j]) ** beta)
                        for j in unvisited]
                probs = probs / np.sum(probs)
                next_city = np.random.choice(list(unvisited), p=probs)
                tour.append(next_city)
                unvisited.remove(next_city)

            # Calculate tour distance
            distance = sum(distances[tour[i]][tour[i+1]]
                         for i in range(len(tour)-1))
            distance += distances[tour[-1]][tour[0]]  

            all_tours.append(tour)
            all_distances.append(distance)

            if distance < best_distance:
                best_distance = distance
                best_tour = tour.copy()

        # Update pheromones
        pheromone *= (1 - evaporation) 
        for tour, dist in zip(all_tours, all_distances):
            for i in range(len(tour)-1):
                pheromone[tour[i]][tour[i+1]] += 1/dist
            pheromone[tour[-1]][tour[0]] += 1/dist

    return best_tour, best_distance

if __name__ == "__main__":
   
    distances = np.array([
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ])

    tour, distance = aco_tsp(distances)
    print(f"Best tour: {tour}")
    print(f"Distance: {distance}")
