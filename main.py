import people_factory, simulator

population = 50
villagers = people_factory.create_people(population)

risk = []
for villager in villagers:
    risk.append(villager.riskFactor)

infected_people = []

while True:
    input("Press to advance a day")
    simulator.advance_one_week(villagers, population, infected_people)
