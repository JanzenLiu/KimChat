import itchat
from itchat.content import TEXT, PICTURE
from MsgHandler import *
from config import signature, header

@itchat.msg_register(TEXT)
def simply_reply(msg):
	msg.text = handleInMsg(msg.text)
	print("In: %s" % msg.text)
	reply = getReply(msg)
	reply = handleOutMsg(reply)
	print("Out: %s" % reply)
	return(header + reply)
@itchat.msg_register(PICTURE)
def sticker_reply(msg):
	print(msg)

itchat.auto_login()
itchat.run()