import unittest
from hangman_medicine import choose_word, display_gif, check_guess

class TestHangmanMedicine(unittest.TestCase):
    def test_choose_word(self):
        # Test if the chosen word is in the list of medical terms
        medical_terms = [ "neurology", "cardiology", "ophthalmology", "pediatrics", "orthopedics"]
        word = choose_word()
        self.assertIn(word, medical_terms)

    def test_check_guess(self):
        # Test if guessed letter is present in the word
        word = "cardiology"
        guessed_letter = 'a'
        self.assertTrue(check_guess(word, [], guessed_letter))

        # Test if guessed letter is not present in the word
        guessed_letter = 'z'
        self.assertFalse(check_guess(word, [], guessed_letter))

    def test_display_gif(self):
        # Test display of GIF for a valid medical term
        word = "neurology"
        self.assertIsNotNone(display_gif(word))

        # Test display of GIF for an invalid medical term
        word = "invalid_term"
        self.assertIsNone(display_gif(word))

if __name__ == '__main__':
    unittest.main()
