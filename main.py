import itchat
import xmltodict
import json
from bs4 import BeautifulSoup
from itchat.content import TEXT, PICTURE
from MsgHandler import *

@itchat.msg_register(TEXT)
def simply_reply(msg):
	msg.text = handleInMsg(msg.text)
	print("In: %s" % msg.text)
	reply = getReply(msg)
	if(reply):
		reply = handleOutMsg(reply)
		print("Out: %s" % reply)
		return(header + reply)

@itchat.msg_register(PICTURE)
def sticker_reply(msg):
	with open("MsgLog.txt", "w") as file:
		for item in msg.items():
			file.write("%s: %s\n" % (item[0], item[1]))
			print(item[0], ": ", item[1])
	content = BeautifulSoup(msg.Content, 'xml')
	cdnurl = content.emoji.attrs['cdnurl']
	with open("stickerLog.txt","a") as file:
		file.write("%s\n" % cdnurl)
	# itchat.send_raw_msg(msg["MsgType"], msg["Content"], msg["FromUserName"])
	# content = xmltodict.parse(content)
	# content = json.dumps(content)
	# print(content)
	itchat.send_image("facepalm.png", msg["FromUserName"])
	return cdnurl 

#itchat.auto_login()
itchat.auto_login(enableCmdQR=2) # enabled when run on the cloud server
itchat.run()
