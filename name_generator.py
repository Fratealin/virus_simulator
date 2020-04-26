import random


def make_name():
    first_names = "Boris Xi Abe Bernard Paddington Mao Caesar Yotam Winston".split()
    last_names = "Who Truman Ottoman Augustus Ottolenghi Thor Bezos".split()
    return " ".join([random.choice(first_names), random.choice(last_names)])


def make_name_list(number):
    full_names = []
    for n in range(number):
        full_names.append(make_name())
    return full_names
