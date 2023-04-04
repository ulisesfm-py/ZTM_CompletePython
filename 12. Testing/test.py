import unittest
import main


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_num = 10
        result = main.do_stuff(test_num)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'kjsalkskoa'
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))


unittest.main()
