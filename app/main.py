class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = [Person(name=human["name"], age=human["age"])
                   for human in people]

    for i in range(len(people)):
        if "wife" in people[i] and people[i]["wife"] is not None:
            result_list[i].wife = Person.people[people[i]["wife"]]
        if "husband" in people[i] and people[i]["husband"] is not None:
            result_list[i].husband = Person.people[people[i]["husband"]]
    return result_list
