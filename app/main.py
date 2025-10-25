class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = []

    for human in people:
        result_list.append(Person(name=human["name"], age=human["age"]))

    for human in people:
        if human.get("wife", 0):
            Person.people[human["wife"]].husband = Person.people[human["name"]]
            Person.people[human["name"]].wife = Person.people[human["wife"]]
    return result_list
