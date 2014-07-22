#!/usr/bin/python

from json_wrapper import JSON_Wrapper
import sys

wrapper = JSON_Wrapper()
file = sys.stdin

print wrapper.convert(file)