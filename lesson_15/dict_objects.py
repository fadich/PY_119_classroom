import math


def create_character(
    name: str,
    age: float,
    power: str,
    hit_points: float,
):
    return {
        "name": name,
        "age": age,
        "power": power,
        "hit_points": hit_points,
        "damage": 10,
    }


gandalf = create_character(
    name="Gandalf",
    age=math.nan,
    power="Magic",
    hit_points=100.0,
)

saruman = create_character(
    name="Saruman",
    age=math.nan,
    power="Magic",
    hit_points=90.0,
)

aragorn = create_character(
    name="Aragorn",
    age=87,
    power="Tracking",
    hit_points=120.0,
)

characters = (
    gandalf,
    saruman,
    aragorn,
)

powers = {char.get("power").lower() for char in characters}
print(f"powers: {powers}")


def attach(attacker, defender):
    defender["hit_points"] -= attacker["damage"]


print(saruman)
attach(
    attacker=gandalf,
    defender=saruman,
)
print(saruman)
