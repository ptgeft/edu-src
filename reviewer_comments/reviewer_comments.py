#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import requests
#import re
sys.path.append("..")
import libs.file as file
import time
import random

def get_comments_detail(id, sessionid):
	url = 'https://src.sjtu.edu.cn/post/' + str(id) + '/'
	reviewer_comments = ''
	cookie = {'sessionid': sessionid}
	try:
		r = requests.get(url, cookies=cookie)
		reviewer_comments = r.content.split('尚不能查看。', 1)[1].split('审核评价： ', 1)[1].split('</div>', 1)[0].strip().replace(",", "，").replace("\r\n", " ")
		print str(id) + ',' + reviewer_comments
	except Exception as e:
		print e
	return reviewer_comments

def main(argv):
	filename = 'reviewer_comments.csv'
	sessionid = argv[1]
	# currently 1 - max(37942)
	start_id = 1
	end_id = int(argv[2])
	try:
		if argv[3] == 'new':
			file.write_file(filename, '', 'w+')
	except Exception as e:
		if file.isfile(filename):
			comments_list = file.read_file(filename, True)
			if len(comments_list) > 2:
				start_id = int(comments_list[len(comments_list) - 1].split(',')[0]) + 1
	print start_id

	for id in xrange(start_id, end_id):
		reviewer_comments = get_comments_detail(id, sessionid)
		if reviewer_comments != '':
			data = str(id) + ',' + reviewer_comments + '\n'
			file.write_file(filename, data)
		#time.sleep(0.5 + random.random())

if __name__ == "__main__":
	main(sys.argv)
	