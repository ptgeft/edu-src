#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import requests
import re
import libs.file as file
import time
import random

def get_firm_detail(id):
	url = 'https://src.edu-info.edu.cn/list/firm/' + str(id)
	firm_name = ''
	vul_num = ''
	try:
		r = requests.get(url)
		firm_name = re.search('<h2>(.*)</h2>', r.content).group(1)[15:].strip()
		vul_num = re.search('<h3 style="margin-top: 0em;">(.*)&nbsp;&nbsp;', r.content).group(1)[15:].strip()
		print str(id) + ',' + firm_name + ',' + vul_num
	except Exception as e:
		print e

	return firm_name, vul_num

def main(argv):
	filename = 'list_firm.csv'
	
	# currently 3076-7220
	start_id = 3075
	end_id = 7222
	try:
		if argv[1] == 'new':
			file.write_file(filename, '', 'w+')
	except Exception as e:
		if file.isfile(filename):
			firm_list = file.read_file(filename, True)
			if len(firm_list) > 2:
				start_id = int(firm_list[len(firm_list) - 1].split(',')[0]) + 1
	print start_id

	for id in xrange(start_id, end_id):
		firm_name, vul_num = get_firm_detail(id)
		if firm_name != '':
			data = str(id) + ',' + firm_name + ',' + vul_num + '\n'
			file.write_file(filename, data)
		#time.sleep(0.5 + random.random())

if __name__ == "__main__":
	main(sys.argv)
