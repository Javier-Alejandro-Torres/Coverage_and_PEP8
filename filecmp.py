import filecmp
import unittest


class TestStringMethods(unittest.TestCase):
    def test_Comparing_files(self):
        self.assertEqual(filecmp.cmp("file1.txt", "file2.txt"), True)

    def test_Comparing_True(self):
        self.assertTrue(filecmp.cmp("file1.txt", "file2.txt"), True)

    def test_Comparing_False(self):
        self.assertFalse(filecmp.cmp("file3.txt", "file2.txt"), False)

    def test_Compare_Shallow(self):
        self.assertEqual(filecmp.cmp("file3.txt", "file2.txt", shallow=True), False)


if __name__ == '__main__':
    unittest.main()
