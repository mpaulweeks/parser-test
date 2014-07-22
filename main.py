#!/usr/bin/python

from json_wrapper import JSON_Wrapper
import sys
import operator

wrapper = JSON_Wrapper()
file = sys.stdin

json = wrapper.json(file)
entries = json["entries"]
errors = json["errors"]

out = '{\n'
out += '  "entries": [\n'
for dict in sorted(entries, key=operator.itemgetter('lastname', 'firstname')):
	out += '    {\n'
	for key in sorted(dict):
		out += '      "' + key + '": "' + dict[key] + '",\n'
	out += '    }'
	if dict != entries[-1]:
		out += ','
	out += '\n'
out += '  ],\n'
out += '  "errors": [\n'
for num in sorted(errors):
	out += '      ' + str(num)
	if num != errors[-1]:
		out += ','
	out += '\n'
out += '  ]\n'
out += '}'

print out