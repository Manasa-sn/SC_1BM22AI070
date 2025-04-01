# GeneticAlgorithm
import random

POP_SIZE = 10
MUT_RATE = 0.9
def initial_population(POP_SIZE):
    pop = list()
    for _ in range(POP_SIZE):
        temp = list()
        for i in range(4):
            temp.append(int(random.random()*10))
        pop.append(temp)
    return pop
def fitness_cal(initial_pop):
    fitness = 0
    population = list()
    for chromo in initial_pop:
        fitness = 0
        fitness = abs((chromo[0])+(2*chromo[1])+(3*chromo[2])+(4*chromo[3])-30)
        prob = 1/(1+fitness)
        population.append([prob, chromo])
    return population
def selection(initial_pop):
    selected = list()
    selected = sorted(initial_pop, key= lambda x : x[0], reverse=True)
    return selected[:int(POP_SIZE*0.5)]
def crossover(selected, initial_pop):

    crossovered = list()
    selected_pop = list()
    ini_pop = list()
    for chromo_selected in selected:
        selected_pop.append(chromo_selected[1])

    for chromo_ini in initial_pop:
        ini_pop.append(chromo_ini[1])
    c = 0
    for chromo in selected_pop:
        p1 = selected_pop[c]
        p2 = ini_pop[c]
        c+=1
        crossover_point = random.randint(1, len(chromo)-1)
        child1 =  p1[:crossover_point] + p2[crossover_point:]
        child2 = p2[:crossover_point] + p1[crossover_point:]
        crossovered.extend([child1, child2])
    return crossovered
def mutation(crossovered, MUT_RATE):

    for chromo in crossovered:
        num = random.randrange(0,30)
        index = random.randrange(0, len(chromo)-1)
        prob = random.random()
        if prob < MUT_RATE:
            chromo[index] = num
    return crossovered
def replacement(new_gen, initial_pop):
    for _ in range(len(initial_pop)):
        if initial_pop[_][0] < new_gen[_][0]:
          initial_pop[_][1] = new_gen[_][1]
          initial_pop[_][0] = new_gen[_][0]
    return initial_pop
def main(MUT_RATE, POP_SIZE):
    initial_pop = initial_population(POP_SIZE)
    population = fitness_cal(initial_pop)
    generation = 1
    found = False

    while not found and generation <=500:
        selected = selection(population)
        crossovered = crossover(selected, population)
        mutated = mutation(crossovered, MUT_RATE)
        new_gen = list()
        new_gen = fitness_cal(mutated)
        new_gen = sorted(new_gen, key= lambda x:x[0], reverse=True)
        population = replacement(new_gen, population)
        print('Generation: ' + str(generation) + ' Chromosome: ' + str(population[0]))
        generation+=1

        if population[0][0] == 1:
            print('FOUND')
            print(str(population[0][0]) + ' ' + str(population[0][1]))
            found = True

main (MUT_RATE, POP_SIZE)
