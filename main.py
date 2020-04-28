import people_factory
import simulator

population = 50
villagers = people_factory.create_people(population)

risk = []
for villager in villagers:
    risk.append(villager.riskFactor)

while True:
    input("Press to advance a day")
    infected_people = (simulator.advance_one_week(villagers))
    
