import unittest

import time


class FirstTest(unittest.TestCase):
    def test_assert(self):
        time.sleep(2)
        self.assertTrue(1 == 1)
