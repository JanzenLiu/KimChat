import itchat
from itchat.content import TEXT
from MsgHandler import getReply

@itchat.msg_register(TEXT)
def simply_reply(msg):
	reply = getReply(msg)
	print(msg.text)
	print(reply)
	return(reply)

itchat.auto_login()
itchat.run()