import name_generator
import random


class Person:
    def __init__(self):
        self.name = name_generator.make_name()
        self.hygiene = random.randrange(1, 11)
        self.gotoWork = random.randrange(0, 6)
        self.otherTrips = random.randrange(0, 8)
        self.keepDistance = random.randrange(1, 11)
        self.infection = False

    def display_information(self):
        if self.infection:
            infection = "do"
        else:
            infection = "don't"
        print(f"Hi, my name is {self.name}, I am a {self.location}.I am {self.hygiene} hygienic, I go to work {self.gotowork} times a week. I go out {self.otherTrips} times a week. I have a keep distance score of {self.keepDistance}. My daily risk factor is {self.riskfactorratio}. I {infection} have Wuhan pneumonia.")


class VillagePerson(Person):
    def __init__(self):
        super().__init__()
        self.location = "village person"
        self.populationDensity = 400
        meters_per_journey = 2000
        meters_per_square_kilometer = 1000000
        people_per_meter_squared = float(self.populationDensity / meters_per_square_kilometer)
        people_contact = meters_per_journey * people_per_meter_squared * 2
        self.complianceFactor = self.keepDistance * self.hygiene
        self.riskFactor = self.gotoWork * people_contact / self.complianceFactor + self.otherTrips * people_contact / self.complianceFactor

    def display_information(self):
        if self.infection:
            infection = "do"
        else:
            infection = "don't"
        print(f"Hi, my name is {self.name}, I am a {self.location}."
              f"\nI am {self.hygiene} hygienic, I go to work {self.gotoWork} times a week. I go out {self.otherTrips} times a week."
              f"\nI have a keep distance score of {self.keepDistance}. My daily risk factor is {self.riskFactor}."
              f"\nI {infection} have Wuhan pneumonia.")


def create_people(number):
    villagers = []
    for n in range(number):
        villagers.append(VillagePerson())
        villagers[n].display_information()
    return villagers