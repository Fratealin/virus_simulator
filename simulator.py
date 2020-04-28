import random


def advance_one_week(people):
    infected_people = []
    for person in people:
        risk_percentage = random.random()*10
        if person.riskFactor >= risk_percentage:
            person.infection = True
        if person.infection:
            infected_people.append(person.name)

    print(f"{len(infected_people)} people have got the virus:\n{', '.join(infected_people)}")
    return infected_people
