from dataclasses import dataclass, field

from behave import given, when, then
import typing
from src.person import Person

@dataclass
class LifeSteps:
    person: Person = None

    # Scenario

    @given("a person named Popeye who is 16 years old")
    def given_person_with_age(self):
        self.person = Person(name='Popeye', age=16)

    @when("Popeye celebrates a birthday")
    def when_person_celebrates_birthday(self):
        self.person.happy_birthday()

    @then("Popeye should be 17 years old")
    def then_person_has_new_age(self):
        assert self.person.age == 17

    # Scenario Outline

    @given("Person named {name} who is {age:d} years old")
    def given_person_with_age(self, name, age):
        self.person = Person(name=name, age=age)

    @when("they celebrate a birthday")
    def when_person_celebrates_birthday(self):
        self.person.happy_birthday()

    @then("they should be {older:d}")
    def then_person_has_new_age(self, older: int):
        assert self.person.age == older
