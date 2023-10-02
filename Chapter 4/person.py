import random
from typing import List, Optional
from datetime import date


class Person:
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
        self.country_of_residence = country_of_residence
        self.date_of_birth = date_of_birth or date.today()
        self.biological_gender = biological_gender or random.choice(["M", "F"])
        self.spouse = spouse
        self.children = children or []
        self.parents = parents or []


person_0 = Person(
    "John",
    "Doe",
    "France"
)

person_1 = Person(
    first_name="Sam",
    last_name="Onaisi",
    country_of_residence="France",
    date_of_birth=date(1994, 8, 1),
    children=[person_0]
)
print(person_1.first_name)
print(person_1.last_name)
print(person_1.country_of_residence)
print(person_1.date_of_birth)
print(person_1.biological_gender)
print(person_1.spouse)
print(person_1.children)
print(person_1.parents)
