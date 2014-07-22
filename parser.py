class Parser:

	# Case1: Lastname, Firstname, (703)-742-0996, Blue, 10013
	# Case2: Firstname Lastname, Red, 11237, 703 955 0373
	# Case3: Firstname, Lastname, 10013, 646 111 0101, Green

	def parse_line(self, raw):
		text = raw.rstrip()
		if text == "herp":
			return {"error": True}
		return {"text": text}