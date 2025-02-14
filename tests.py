from credit_card_validator import credit_card_validator
import random
import string
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        testToGenerate = 800000
        for i in range(testToGenerate):
            lengths = [15, 16, 17]

            length = random.choice(lengths)

            digits = string.digits

            num = ''
            num = num + ''.join(random.choice(digits) for i in range(length))

            credit_card_validator(num)


if __name__ == '__main__':
    unittest.main()
