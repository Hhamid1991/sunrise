from sunrise.actions import Calculator
import re

def parse(user_command) :
	if (bool(re.search("[-+]?[0-9]+\.?[0-9]*\s*[-+*\/]\s*[-+]?[0-9]+\.?[0-9]*", user_command))==True):
	  return Calculator()
	else :
	  return not_matched

