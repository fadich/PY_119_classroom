class A:

    def __init__(self):
        self.a = 1

    def jump_command_handler(self):
        pass


a = A()
print(
    getattr(a, "b", "***")   # a.a
)

a.c = 8
getattr(a, "c")

setattr(a, "d", 9)  # a.d = 9
print(a.d)


command = input("")
print(
    hasattr(a, f"{command}_command_handler")
)
getattr(a, f"{command}_command_handler")()
