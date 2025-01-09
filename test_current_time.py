import unittest
import time

from current_time import current_time

class TestCurrentTime(unittest.TestCase):

    def testIsString(self):
        self.assertEqual(current_time(), time.strftime("%H:%M:%S"))


if __name__ == '__main__':
    unittest.main()