from parser import Parser

class JSON_Wrapper:
	
	parser = Parser()

	def convert(self, file):
		entries = []
		error_lines = []
		line_number = 0
		for line in file:
			result = self.parser.parse_line(line)
			if "error" in result:
				error_lines.append(line_number)
			else:
				entries.append(result)
			line_number += 1
		json = {
			"entries": entries,
			"errors": error_lines,
			}
		return json