import unittest
import main


class TestMain(unittest.TestCase):
    def do_test_case(self):
        test_param = 10
        result = main.do_num_plus_five(test_param)
        self.assertEqual(result, 15)

    def do_test_case2(self):
        test_param = 'check'
        result = main.do_num_plus_five(test_param)
        self.assertEqual(result, TypeError)


unittest.main()
