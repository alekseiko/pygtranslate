#!/usr/bin/env python

import simplejson
import urllib
import sys

GOOGLE_TRANSLATE_AJAX_URL = "http://ajax.googleapis.com/ajax/services/language/translate?v=1.0&langpair=en%7Cru&q=hello"
def main(args):
	print simplejson.load(urllib.urlopen(GOOGLE_TRANSLATE_AJAX_URL))["responseData"]["translatedText"]

if __name__ == "__main__":
	main(sys.argv[1:])
