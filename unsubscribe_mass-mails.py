#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

sys.path.insert(0, '../')
import re
import logging
import requests, bs4
from optparse import OptionParser
from sys import argv
from os.path import abspath, dirname


logfile = logging.FileHandler('som.log')
console_out = logging.StreamHandler()

parser = OptionParser()

parser.add_option('-v', '--version', dest='version', action='store_true', default=False, help="Show version")
parser.add_option('-d', '--debug', dest='debug', action='store_true', default=False, help="Run in debug mode")
 
options, args = parser.parse_args()
 
if options.version:
    print('som_0.1')

if options.debug:
	logging.basicConfig(handlers=(logfile, console_out), level=logging.DEBUG)
else:
	logging.basicConfig(handlers=(logfile, console_out), level=logging.INFO)

if args:
    print('Остальные аргументы:', args)


try:
	fileopen = open('mail_bounced.txt', 'r')
	for line in fileopen:
		match = re.search(r'[\w\.-]+@[\w\.-]+', line)
		if match is None:
			email = str(None)
		elif match:
			email = match.group(0)
			print(email)
			session = requests.session()
			headers = {'accept': '*/*', 'user-agent': 'Mozilla/5.0 (X11; Linux armv7l; ru-ru; Vasya v1.0) CORE Vasya v1.0 for AI_SHS (alcoshopers.ru)'}
			request = session.get("https://nstopt.ru/API?TOKEN=FgT6TGdrt5dFsdas87Vgjk&command=unSubscribe&EMAIL=" + email, headers=headers)
			b = bs4.BeautifulSoup(request.text, "html.parser")
			print(b)
except KeyboardInterrupt:
	print("Завершение программы")