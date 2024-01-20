import re


class Email:
    PATTERN = (r'^(\"[^@]{1,62}\"@[a-zA-Z\d]+\.[a-zA-Z]{2,}$)'
               r'|'
               r"^[!#$%&'*+/=?^_`{|}~a-zA-Z\d]+([\.-]\w+)*(?<![\.-])@[a-zA-Z\d]+\.[a-zA-Z]{2,}$")

    def __init__(self, email):
        self.email = email

    @classmethod
    def validate(cls, email):
        """validates email on:
        Local part
        - uppercase and lowercase Latin letters A to Z and a to z
        - digits 0 to 9
        - printable characters !#$%&'*+-/=?^_`{|}~
        - dot ., provided that it is not the first or last character and
            provided also that it does not appear consecutively (e.g., John..Doe@example.com is not allowed)
        - If quoted, it may contain Space, Horizontal Tab (HT), any ASCII graphic except Backslash and Quote and
            a quoted-pair consisting of a Backslash followed by HT, Space or any ASCII graphic;
            it may also be split between lines anywhere that HT or Space appears. In contrast to unquoted local-parts,
            the addresses ".John.Doe"@example.com, "John.Doe."@example.com and "John..Doe"@example.com are allowed.
        - The maximum total length of the local-part of an email address is 64 octets
        Domain
        - Uppercase and lowercase Latin letters A to Z and a to z;
        - Digits 0 to 9, provided that top-level domain names are not all-numeric.
            """

        if re.fullmatch(cls.PATTERN, email):
            if len(email.split("@")[0]) <= 64:
                return True
        return False

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if self.validate(value):
            self._email = value
        else:
            raise ValueError(
                f'{self} -> {value} - Provided email is not valid'
            )


if __name__ == "__main__":
    validator = Email("asdasdasd@middleearth.com")
    print(validator.email)
