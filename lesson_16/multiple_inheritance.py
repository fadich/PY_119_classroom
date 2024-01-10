
class BaseCharacter:

    def eat(self):
        print(f"{self.__class__.__name__} maybe eats?!")


class ScifiCharacter(BaseCharacter):
    pass

    # def eat(self):
    #     print(f"{self.__class__.__name__} DOES NOT EAT!")


class Robot(ScifiCharacter):
    pass

    # def eat(self):
    #     print(f"{self.__class__.__name__} DOES NOT EAT! I am a ROBOT!")


class FantasyCharacter:
    pass

    # def eat(self):
    #     print(f"{self.__class__.__name__} eats fantasy meals")


class Elf(FantasyCharacter):

    def eat(self):
        print(f"{self.__class__.__name__} eats fruits")


class Dwarf(FantasyCharacter):

    def eat(self):
        print(f"{self.__class__.__name__} eats meat")


class Human(FantasyCharacter):

    def eat(self):
        print(f"{self.__class__.__name__} eats everything")


class Cyborg(Robot, Human):

    def eat(self):
        super().eat()

        Robot.eat(self)
        Human.eat(self)


if __name__ == "__main__":
    legolas = Elf()
    gimli = Dwarf()
    aragorn = Human()

    # print(isinstance(legolas, Elf))
    # print(isinstance(legolas, FantasyCharacter))
    # print(isinstance(legolas, Dwarf))
    # print(isinstance(legolas, Human))
    # print(isinstance(legolas, ScifiCharacter))

    bumblebee = Robot()
    # print(isinstance(bumblebee, Robot))
    # print(isinstance(bumblebee, ScifiCharacter))
    # print(isinstance(bumblebee, FantasyCharacter))

    robocop = Cyborg()
    # print(isinstance(robocop, Robot))
    # print(isinstance(robocop, Human))
    # print(isinstance(robocop, ScifiCharacter))
    # print(isinstance(robocop, FantasyCharacter))

    # aragorn.eat()
    legolas.eat()
    bumblebee.eat()
    print("----")
    robocop.eat()

    Cyborg.eat(robocop)  # robocop.eat()

    # str.lower("Abc assdASD")
    # "Abc assdASD".lower()
