Michael Paul Weeks
NOTE: Written for Python 2.7

How to run:

On Mac, to run the program, enter this in Terminal:
$ python main.py < sample-paul.in

To run tests:
$ python test.py

Also:
	In the provided documentation, the three formats had their phone numbers formatted differently.
		I chose to interpret this as "they could come in any of these formats",
		not as "if the number isn't exactly in this format, it's invalid"
		because I thought the former was closer to a real-world scenario.
	Also I've never written tests in python or written projects that necessitated more than one file like this,
		so please take that lack of experience into account when assessing how I formatted my test files
		and organized my classes. I'm eager to learn best practices in this sort of the scenario, but
		for now I improvised what I thought it might look like.
	Likewise, I chose to only write tests for the parsing behavior because in a production environment,
		I wouldn't test something as thin as the JSON_Wrapper and I wouldn't use unit tests to verify
		something like the formatting of the output.