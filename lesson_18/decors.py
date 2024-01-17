
# class User:
#
#     def __init__(self, f, l):
#         self.fn = f
#         self.ln = l
#         # self.full_name = f"{self.fn} {self.ln}"
#
#     @property
#     def full_name(self):
#         return f"{self.fn} {self.ln}"


class User:

    def __init__(self, login: str, password: str):
        self._login = login
        self._password = password
        self.SECRET = "123123"

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        # print("PASSWORD CALLED")
        password = "*" * (len(self._password) + len(self.SECRET))

        return password

    @password.setter
    def password(self, new_password: str):
        if new_password == self._password:
            raise ValueError("You can't the same password")

        self._password = new_password  # <---- processing

    @password.deleter
    def password(self):
        print("PASSWORD CANNOT BE DELETED!")
        # raise ...


if __name__ == "__main__":
    user = User("gandalf", "magic")

    print(user.login)
    print(user.password)

    user.password = "0"
    print(user.password)

    del user.password

    print(user.password)
    print(user.password)

    print("=" * 30)
    print(hasattr(user, "login"))
    print(getattr(user, "login"))
    # print(setattr(user, "login", "frodo"))
    print(user.login)
