import itchat
import xmltodict
import json
from bs4 import BeautifulSoup
from itchat.content import TEXT, PICTURE
from MsgHandler import *

@itchat.msg_register([TEXT, PICTURE])
def simply_reply(msg):
	reply = getReply(msg)
	if(reply):
		return reply

itchat.auto_login()
# itchat.auto_login(enableCmdQR=2) # enabled when run on the cloud server
itchat.run()

