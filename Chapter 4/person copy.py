import random
from typing import List, Optional, Tuple
from datetime import date


class PolygamyError(Exception):
    def __init__(self):
        self.message = "You can't mary two persons"
        super().__init__(self.message)


class DivorceError(Exception):
    def __init__(self):
        self.message = "You can't divorce if you are not married"
        super().__init__(self.message)


class ImmaculateConceptionError(Exception):
    def __init__(self):
        self.message = "This person is not the virgin Mary"
        super().__init__(self.message)


class Person:
    registered_people = []

    def __init__(
        self,
        first_name: str,
        last_name: str,
        country_of_residence: str,
        date_of_birth: Optional[date] = None,
        biological_gender: Optional[str] = None,
        spouse: Optional["Person"] = None,
        children: Optional[List["Person"]] = None,
        parents: Optional[List["Person"]] = None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.original_last_name = last_name
        self.country_of_residence = country_of_residence
        self.date_of_birth = date_of_birth or date.today()
        self.biological_gender = biological_gender or random.choice(["M", "F"])
        # TODO : Protect these fields so it's not updated manually
        self.spouse = []
        # If we create a Person instance with a spouse, we need to create the
        # reverse relationship.
        if spouse:
            self, self.spouse = self.mary(spouse)
        self.children = children or []
        self.parents = parents or []

        self.registered_people.append(self)

    def __str__(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    def mary(
        self, person: "Person", last_name_changes: str = "keep"
    ) -> Tuple["Person", "Person"]:
        """
        Method that handles the instance marrying another person instance

        Arguments :
            - person (Person) : person to mary
            - last_name (str) : what to with last name
                - "keep" : Both instances keep their original last name
                - "combine": combine both last names
                - "self" : keep this instance's last_name for both instances
                - "other" : keep the other instance's last_name for both instances
        """
        if self.spouse or person.spouse:
            raise PolygamyError()

        if self == person:
            raise ValueError("You can't mary yourself")

        if last_name_changes == "keep":
            self.spouse = person
            person.spouse = self
            return (self, person)
        elif last_name_changes == "combine":
            last_name = f"{self.last_name}-{person.last_name}"
        elif last_name_changes == "self":
            last_name = self.last_name
        elif last_name_changes == "other":
            last_name = person.last_name
        else:
            raise ValueError(
                f"Wrong option for last_name_changes : {last_name_changes}."
                "valid options are : keep, combine, self, other."
            )
        self.spouse = person
        person.spouse = self
        self.last_name = last_name
        person.last_name = last_name
        return (self, person)

    def divorce(self) -> "Person":
        if not self.spouse:
            raise DivorceError()
        self.spouse.last_name = self.spouse.original_last_name
        self.spouse.spouse = None
        self.last_name = self.original_last_name
        self.spouse = None
        return self

    def procreate(
        self, first_name: str, other_parent: Optional["Person"] = None
    ) -> "Person":
        other_parent = other_parent or self.spouse
        if not other_parent:
            raise ImmaculateConceptionError()
        if other_parent == self:
            raise ValueError("You can't do that")
        parents = [self, other_parent]
        last_name = random.choice(
            [p.original_last_name for p in parents]
        )
        country_of_residence = random.choice(
            [p.country_of_residence for p in parents]
        )
        child = Person(
            first_name,
            last_name,
            country_of_residence,
            parents=parents
        )
        self.children.append(child)
        other_parent.children.append(child)
        return child

    @classmethod
    def get_inhabitants_per_country(cls):
        countries = [
            p.country_of_residence
            for p in cls.registered_people
        ]
        return {
            country: countries.count(country)
            for country in set(countries)
        }

    @classmethod
    def count_married_couples_option_1(cls):
        people = cls.registered_people
        married_people = list(
            filter(
                lambda x: x.spouse, people
            )
        )
        return int(len(married_people)/2)

    @classmethod
    def count_married_couples_option_2(cls):
        people = cls.registered_people
        married_people = [
            p for p in people if p.spouse
        ]
        return int(len(married_people)/2)


person_1 = Person("John", "Doe", "France")
# person_1.mary(person_1)
# print(person_1)
person_2 = Person("Jane", "Dooooe", "Germany")
person_3 = Person("Janet", "Dodo", "France")
person_1, person_2 = person_1.mary(person_2, "combine")
person_4 = person_3.procreate("Jack", person_2)
person_5 = Person("Johnny", "Odododo", "France", spouse=person_3)
print(f"{person_5} is married to {person_5.spouse}")
print(f"{person_3} is married to {person_3.spouse}")
# print(Person.get_inhabitants_per_country())
# print(Person.count_married_couples_option_1())
# print(Person.count_married_couples_option_2())
