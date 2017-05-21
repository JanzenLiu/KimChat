from config import *
from json import loads
import urllib.request
import urllib

def replyWrapper():
	flag = True
	def getReply(msg):
		nonlocal flag
		if(not msg.text):
			print("Error: Can not handle message without text")
			return
		if(flag and msg.text == stop):
			flag = False
		elif(not flag and msg.text == restart):
			flag = True
		if(flag):
			params = {
				"key": APIKey,
				"info": msg.text
			}
			data = urllib.parse.urlencode(params)
			bData = data.encode('utf-8')
			req = urllib.request.Request(APIUrl, data=bData)
			res = urllib.request.urlopen(req)
			reply = res.read().decode('utf-8')
			reply = loads(reply)
			return reply['text']
	return getReply

def handleInMsg(msg):
	for emotion in emotions:
		if emotion in msg:
			msg = msg.replace(emotion, emotion[1:-1]) # remove the square brackets
	return msg

def handleOutMsg(msg):
	for emotion in emotions:
		if emotion[1:-1] in msg:
			msg = msg.replace(emotion[1:-1], emotion)
	return msg

getReply = replyWrapper()

signature = ' ----来自Kimthe1st聊天机器人'
header = '[系统自动回复] '
stop = '苟利国家生死以'
restart = '岂因祸福避趋之'