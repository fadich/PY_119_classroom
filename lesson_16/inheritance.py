
class Person:

    def __init__(self, n: str, a: int, x: float = 10.0):
        self.name = n
        self.age = a
        print(x)

    def breath(self):
        print(f"[{self.name}] I can breath")


class Doctor(Person):

    def heal(self, person: Person):
        assert isinstance(person, Person), (
            f"Expected person to be a Person, "
            f"{person.__class__.__name__} given"
        )

        if person is self:
            print(f"[{self.name}] I'm healing myself")
        else:
            print(f"[{self.name}] I am healing {person.name}")


if __name__ == "__main__":
    gandalf = Person(n="Gandalf", a=989)
    print(type(gandalf))

    print(
        f"Is Gandalf a Person:", isinstance(gandalf, Person)
    )

    miranda = Doctor(n="Miranda", a=18)
    print(
        f"Is Miranda a Doctor:", isinstance(miranda, Doctor)
    )
    print(
        f"Is Miranda a Person:", isinstance(miranda, Person)
    )

    miranda.heal(
        person=gandalf,
    )

    dr_house = Doctor(n="dr. House", a=20)
    miranda.heal(
        person=dr_house,
    )

    miranda.heal(
        person=miranda,
    )

    dr_house.heal(gandalf)
    # dr_house.heal([gandalf, miranda])

    dr_house.heal(
        person=Person(n="Frodo", a=18),
    )
