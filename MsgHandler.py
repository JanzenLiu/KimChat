from config import *
from json import loads
import urllib.request
import urllib

def getReply(msg):
	if(not msg.text):
		print("Error: Can not handle message without text")
		return
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

signature = ' ----来自Kimthe1st聊天机器人'
header = '[系统自动回复] '