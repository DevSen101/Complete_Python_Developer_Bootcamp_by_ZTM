import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):  # run before every test functions
        print("about to test the function")

    def test_do_stuff(self):
        """Hii!"""
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 20)

    def test_do_stuff2(self):
        test_param = "dchgs"
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please enter numbers")

    def test_do_stuff4(self):
        test_param = ""
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please enter numbers")

    def tearDown(self): # run after every test functions(use for database clean up etc)
        print("cleaning up")


# to run in single command - python3 -m unittest
if __name__ == "__main__":
    unittest.main()

# cmd for more test details - python3 -m unittest -v
