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
	comments = ''
	cookie = {'sessionid': sessionid}
	try:
		r = requests.get(url, cookies=cookie)
		if 'am-comment am-margin-top-lg' in r.content:
			comms = r.content.split('am-comment am-margin-top-lg')
			for c in comms:
				if 'am-comment-main' in c:
					user = c.split('href="/profile/', 1)[1].split('/">',1)[0]
					comm = c.split('am-comment-bd', 1)[1].split('<p>',1)[1].split('</p>', 1)[0]
					comments += str(id) + ',' + user + ',' + comm + '\n'
					print user + ',' + comm
		#print comments
	except Exception as e:
		print e
	return comments

def main(argv):
	filename = 'user_comments.csv'
	sessionid = argv[1]
	# currently 1 - max(54172)
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
		user_comments = get_comments_detail(id, sessionid)
		if user_comments != '':
			file.write_file(filename, user_comments)
		#time.sleep(0.5 + random.random())

if __name__ == "__main__":
	main(sys.argv)
	