from hello import Hello
import unittest


class HelloTest(unittest.TestCase):
    def setUp(self):
        self.x = Hello(88)

    def testm(self):
        self.assertEqual()

    def testm1(self):
        self.sum = 12
        self.assertTrue(self.x.b(88))
        self.assertFalse(self.x.a(89))
