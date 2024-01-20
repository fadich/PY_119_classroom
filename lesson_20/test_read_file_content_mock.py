import unittest

from unittest.mock import MagicMock


# НЕ МОЖНА В ОДНОМУ ФАЙЛІ
class FileReader:

    def __init__(self, filepath: str):
        self.filepath = filepath

    @property
    def is_gandalf_file(self):
        return self.read_file_content() == "Gandalf"

    def read_file_content(self):
        with open(self.filepath, "r") as file:
            return file.read()


class FileContentTestCase(unittest.TestCase):

    def test_is_gandalf_file(self):
        reader = FileReader("gandalf.txt")
        reader.read_file_content = MagicMock(return_value="Gandalf")

        self.assertTrue(reader.is_gandalf_file)

    def test_is_not_gandalf_file(self):
        reader = FileReader("gandalf.txt")
        reader.read_file_content = MagicMock(return_value="Saruman")

        self.assertFalse(reader.is_gandalf_file)
