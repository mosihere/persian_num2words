import unittest
import src.num2words

class TestNum2Words(unittest.TestCase):

    def test_num_2_words(self):
        self.assertEqual(src.num2words.num_to_word(25), 'بیست و پنج')


if __name__ == "__main__":
    unittest.main()
