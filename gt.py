#!/usr/bin/env python

from googledict import translate
import sys

def main(args):
	
	fromLanguage = args[0][:2]
	toLanguage = args[0][2:]
	text = args[1]

	print translate(fromLanguage, toLanguage, text)

if __name__ == "__main__":
	main(sys.argv[1:])
