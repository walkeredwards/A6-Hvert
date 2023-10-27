"""test hvert.py
"""

import unittest
from hvert import answer

""" 1 = Reykjavik
    2 = Akureyri
"""


class TestHvert(unittest.TestCase):
    def test_answer(self) -> None:
        data = "Gardabaer"
        ans = answer(data)
        expected = 1
        self.assertEqual(ans, expected)

    def test_answer1(self) -> None:
        self.assertEqual(answer("Fjardabyggd"), 2)
