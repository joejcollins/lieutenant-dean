""" Classic unit test styley `python test-unittest.py` """
import unittest
import tasks

class TestTasks(unittest.TestCase):
    """ Class to contain the tests """

    def test_slowly_reverse_string(self):
        """ Test the reversed string """
        RESULT = tasks.slowly_reverse_string.s(string="qwerty").apply()
        self.assertEqual(RESULT.status, 'SUCCESS')
        reversed_string = RESULT.get()
        self.assertEqual(reversed_string, "ytrewq")

if __name__ == '__main__':
    unittest.main()
