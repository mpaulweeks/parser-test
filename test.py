import unittest
from parser import Parser

# Tests for the different cases and fails states of Parsing
class ParseTests(unittest.TestCase):

	parser = Parser()
	
	def has_error(self, result):
		return "error" in result

	def test_empty(self):
		line = ""
		result = self.parser.parse_line(line)
		self.assertTrue(self.has_error(result))

	def test_gibberish(self):
		line = "fghjk3u4kj43jk"
		result = self.parser.parse_line(line)
		self.assertTrue(self.has_error(result))

	def test_short_phonenumber(self):
		line = "Booker T., Washington, 87360, 738023, yellow"
		result = self.parser.parse_line(line)
		self.assertTrue(self.has_error(result))

	def test_long_phonenumber(self):
		line = "Booker T., Washington, 87360, 739090908023, yellow"
		result = self.parser.parse_line(line)
		self.assertTrue(self.has_error(result))

	def test_short_zipcode(self):
		line = "Booker T., Washington, 8736, 373 781 7380, yellow"
		result = self.parser.parse_line(line)
		self.assertTrue(self.has_error(result))

	def test_long_zipcode(self):
		line = "Booker T., Washington, 873600, 373 781 7380, yellow"
		result = self.parser.parse_line(line)
		self.assertTrue(self.has_error(result))

	def test_tooManyFields(self):
		line = "Booker T., Washington, 873600, 373 781 7380, yellow, 234"
		result = self.parser.parse_line(line)
		self.assertTrue(self.has_error(result))

	def test_tooFewFields(self):
		line = "Booker T., Washington, 873600, 373 781 7380"
		result = self.parser.parse_line(line)
		self.assertTrue(self.has_error(result))

	def test_cases(self):
		case1 = "Murphy, James, 018 154 6474, yellow, 83880"
		case2 = "James Murphy, yellow, 83880, 018 154 6474"
		case3 = "James, Murphy, 83880, 018 154 6474, yellow"
		results = []
		results.append(self.parser.parse_line(case1))
		results.append(self.parser.parse_line(case2))
		results.append(self.parser.parse_line(case3))
		for result in results:
			self.assertEqual(result["firstname"], 'James')
			self.assertEqual(result["lastname"], 'Murphy')
			self.assertEqual(result["color"], 'yellow')
			self.assertEqual(result["zipcode"], '83880')
			self.assertEqual(result["phonenumber"], '018-154-6474')

unittest.main()
