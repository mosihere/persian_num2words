import unittest
import src.main

class TestNum2Words(unittest.TestCase):

    def test_num_2_words(self):
        self.assertEqual(src.main.num_to_word(25), 'بیست و پنج')


if __name__ == "__main__":
    unittest.main()
