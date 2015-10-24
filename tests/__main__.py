import unittest
import normalization


class TestNormalization(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(normalization.normalize("This is a normal sentence."), "This is a normal sentence.")

    def test_whitespace(self):
        self.assertEqual(\
            normalization.whitespace("This is not a normal sentence structure .  The spaces are incoherant  ."),\
            "This is not a normal sentence structure. The spaces are incoherant.")
    def test_capitalize(self):
        self.assertEqual(\
            normalization.capitalize("this is not capitalized. it should be."),\
            "This is not capitalized. It should be.")
    def test_abbreviations(self):
        self.assertEqual(\
            normalization.abbreviations("Dr. where were you on aug 5th?"), "Doctor where were you on August fifth?")
    def test_british(self):
        self.assertEqual(\
            normalization.british("axe apologise"), "ax apologize")
    def test_contractions(self):
        self.assertEqual(\
            normalization.contractions("I'll listen to y'all"), "I will listen to you all")
    def test_spellfix(self):
        self.assertEqual(\
            normalization.spellfix("This sentance is acceptible."), "This sentence is acceptable.")
  
if __name__ == '__main__':
    unittest.main()