from dataclasses import dataclass


@dataclass
class Person:
    name: str = "Toto"
    age: int = 2
    _spouse: 'Person' = None

    def __str__(self):
        return f"Hi, I'm {self.name}. I'm {self.age} year(s) old."

    @property
    def spouse(self):
        return self._spouse

    @spouse.setter
    def spouse(self, value: 'Person'):
        if self._spouse is value:
            return

        if self._spouse is not None:
            self._spouse._spouse = None

        if value is not None:
            if value._spouse is not None:
                value._spouse._spouse = None
            value._spouse = self

        self._spouse = value

    def happy_birthday(self):
        self.age += 1

    @property
    def is_adult(self):
        return self.age >= 18

