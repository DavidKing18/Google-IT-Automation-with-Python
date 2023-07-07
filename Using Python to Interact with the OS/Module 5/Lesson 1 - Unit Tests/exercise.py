import re 
import unittest

my_txt = "An investment in knowledge pays the best interest."

def LetterCompiler(txt):
    if type(txt) != str:
        return "Input text not a string"
    result = re.findall(r'([a-c]).', txt)
    return result

print(LetterCompiler(my_txt))


class TestCompiler2(unittest.TestCase):
    
    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

# EDGE CASES HERE
    def test_none(self):
        testcase = ""
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)
        
    def test_not_string(self):
        testcase = ['a', 'b', 'c']
        expected = "Input text not a string"
        self.assertEqual(LetterCompiler(testcase), expected)

unittest.main(argv = ['first-arg-is-ignored'], exit = False)

