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