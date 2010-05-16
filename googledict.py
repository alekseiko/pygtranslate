#!/usr/bin/env python

import simplejson
import urllib
import sys

GOOGLE_TRANSLATE_AJAX_URL = "http://ajax.googleapis.com/ajax/services/language/translate?"
LANGUAGE_SEPARATOR = "|"
RESPONSE_STATUS = "responseStatus"
RESPONSE_DATA = "responseData"
TRANSLATED_TEXT = "translatedText"

def translate(fromLanguage, toLanguage, text):
	""" Translate text using google translate service"""
	# Generate url
	url = GOOGLE_TRANSLATE_AJAX_URL + urllib.urlencode({"v" : "1.0", \
			"langpair" : fromLanguage + LANGUAGE_SEPARATOR + toLanguage, \
			"q" : text})

	result = simplejson.load(urllib.urlopen(url))
	
	if (result[RESPONSE_STATUS]== 200):
		return result[RESPONSE_DATA][TRANSLATED_TEXT]
