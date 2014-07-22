#!/usr/bin/python

from json_wrapper import JSON_Wrapper
import sys
import operator

wrapper = JSON_Wrapper()
file_in = sys.stdin

# convert input into json
json = wrapper.json(file_in)
entries = json["entries"]
errors = json["errors"]

# format output with whitespace and such
out = '{\n'
out += '  "entries": [\n'
sorted_entries = sorted(entries, key=operator.itemgetter('lastname', 'firstname'))
for dict in sorted_entries:
	out += '    {\n'
	sorted_dict = sorted(dict)
	for key in sorted_dict:
		out += '      "' + key + '": "' + dict[key] + '"'
		if key != sorted_dict[-1]:
			out += ','
		out += '\n'
	out += '    }'
	if dict != sorted_entries[-1]:
		out += ','
	out += '\n'
out += '  ],\n'
out += '  "errors": [\n'
sorted_errors = sorted(errors)
for num in sorted_errors:
	out += '      ' + str(num)
	if num != sorted_errors[-1]:
		out += ','
	out += '\n'
out += '  ]\n'
out += '}'

# write to file
file_out = open('result.out', 'w')
file_out.write(out)
file_out.close()