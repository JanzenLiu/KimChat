import itchat
import xmltodict
import json
from bs4 import BeautifulSoup
from itchat.content import TEXT, PICTURE
from MsgHandler import *

#@itchat.msg_register(TEXT)
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
	content = BeautifulSoup(msg.Content, 'xml')
	cdnurl = content.emoji.attrs['cdnurl']
	with open("stickerLog.txt","a") as file:
		file.write("%s\n" % cdnurl)
	with open("MsgLog.txt", "w") as file:
		for item in msg.items():
			file.write("%s: %s\n" % (item[0], item[1]))
			# print(item[0], ": ", item[1])
	# itchat.send_raw_msg(msg["MsgType"], msg["Content"], msg["FromUserName"])
	content = "<msg><emoji fromusername = \"wxid_p8eqd632gjmo22\" tousername=\"wxid_oox0o2ax8oiu52\" type=\"2\" idbuffer=\"media:0_0\" md5=\"286269ca0402801586bf69ef156c2622\" len = \"808866\" productid=\"\" androidmd5=\"286269ca0402801586bf69ef156c2622\" androidlen=\"808866\" s60v3md5 = \"286269ca0402801586bf69ef156c2622\" s60v3len=\"808866\" s60v5md5 = \"286269ca0402801586bf69ef156c2622\" s60v5len=\"808866\" cdnurl = \"http://emoji.qpic.cn/wx_emoji/kAyWiaDloX1oottVuAT7kumJPFiaUtHu0PXQQepn2u721474DmXUcytQ/\" designerid = \"\" thumburl = \"\" encrypturl = \"http://emoji.qpic.cn/wx_emoji/Bc2A90Kgm72Dl02PrnW954MYIepfrlWt9icBgdV5J400s60o4RUQgeQ/\" aeskey= \"49fc2b1c066b7406bcbcfc47ef30b87b\" externurl = \"http://emoji.qpic.cn/wx_emoji/BwfQo31bnx4Z8GSEmLweNmRU6WetQZib3f8MXBusAibXmbHEIIYmzyzceNn7dEfEBh/\" externmd5 = \"ac8da388aaf0866765cfdbbcfa12a684\" width= \"250\" height= \"200\" ></emoji> </msg>"
	# content = xmltodict.parse(content)
	# content = json.dumps(content)
	# print(content)
	itchat.send_image("facepalm.png", msg["FromUserName"])
	return cdnurl 

#itchat.auto_login()
itchat.auto_login(enableCmdQR=2) # enabled when run on the cloud server
itchat.run()
