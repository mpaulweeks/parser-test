class Parser:

	# Case1: Lastname, Firstname, (703)-742-0996, Blue, 10013
	# Case2: Firstname Lastname, Red, 11237, 703 955 0373
	# Case3: Firstname, Lastname, 10013, 646 111 0101, Green

	def clean_phonenumber(self, raw):
		return raw	

	def parse_line(self, raw):
		text = raw.rstrip()
		chunks = text.split(", ")
		
		color = ""
		firstname = ""
		lastname = ""
		phonenumber = ""
		zipcode = ""
		
		if len(chunks) == 4:
			#Case2
			firstname, junk, lastname = chunks[0].partition(' ')
			color = chunks[1]
			zipcode = chunks[2]
			phonenumber = chunks[3]
		elif len(chunks) == 5:
			if chunks[4].isalpha():
				#Case3
				firstname = chunks[0]
				lastname = chunks[1]
				zipcode = chunks[2]
				phonenumber = chunks[3]
				color = chunks[4]
			elif chunks[3].isalpha():
				#Case1
				lastname = chunks[0]
				firstname = chunks[1]
				phonenumber = chunks[2]
				color = chunks[3]
				zipcode = chunks[4]
		
		phonenumber = self.clean_phonenumber(phonenumber)
		
		if not (firstname and lastname and phonenumber and color and zipcode):
			return {"error": True}
		else:
			return {
				"color": color,
				"firstname": firstname,
				"lastname": lastname,
				"phonenumber": phonenumber,
				"zipcode": zipcode,
				}