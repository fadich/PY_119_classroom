class Firefighter:

    def __init__(self, name: str, rank: str):
        self.name = name
        self.rank = rank


class Transport:

    def __init__(self, is_combat: bool, car_type: str):
        self.is_combat = is_combat
        self.volume = self.get_volume(car_type)
        self.passengers = []

    def get_volume(self, car_type: str):
        if car_type == "fire":
            return 4.0
        else:
            return 0.0

    def add_passenger(self, passenger: Firefighter):
        self.passengers.append(passenger)


ff1 = Firefighter(name="Gandalf", rank="Sergeant")
ff2 = Firefighter(name="Frodo", rank="Junior")
captain = Firefighter(name="Bilbo", rank="Captain")

ac = Transport(
    is_combat=True,
    car_type="fire",
)

print(ac.is_combat)
print(ac.volume)

print("passengers:", ac.passengers)

ac.add_passenger(ff1)
print("passengers:", [p.name for p in ac.passengers])

ac.add_passenger(ff2)
print("passengers:", [p.name for p in ac.passengers])

ac.passengers.append(captain)
print("passengers:", [p.name for p in ac.passengers])
