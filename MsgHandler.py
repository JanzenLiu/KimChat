from config import *
from json import loads
from bs4 import BeautifulSoup
from itchat.content import TEXT, PICTURE
import itchat
import urllib.request
import urllib
import json
import random
import os

def replyWrapper():
	# flag = True
	cache = {}

	def reply_text(msg):
		nonlocal cache
		fromUser = msg["FromUserName"]
		text = msg.text
		if(cache[fromUser]['unreply_wait'] == -1):
			cache[fromUser]['unreply_wait'] = random.randint(0,MAX_UNREPLY)
		cache[fromUser]['unreply_num'] += 1
		cache[fromUser]['msg'].append(text)
		print("Wait Until: ", cache[fromUser]['unreply_wait'])
		print("Unreplied: ", cache[fromUser]['unreply_num'])
		text = handleInMsg(text)
		print("In: %s" % text)
		if(is_funny(msg)):
			itchat.send_image("facepalm.png", fromUser)
		if(cache[fromUser]['unreply_num'] >= cache[fromUser]['unreply_wait']):
			cache[fromUser]['unreply_wait'] = -1
			cache[fromUser]['unreply_num'] = 0
			params = {
				"key": APIKey,
				"info": text
			}
			data = urllib.parse.urlencode(params)
			bData = data.encode('utf-8')
			req = urllib.request.Request(APIUrl, data=bData)
			res = urllib.request.urlopen(req)
			reply = res.read().decode('utf-8')
			reply = json.loads(reply)['text']
			if(reply):
				reply = handleOutMsg(reply)
				print("Out: %s" % reply)
				return(header + reply)

	def reply_sticker(msg):
		# with open("MsgLog.txt", "w") as file:
		# 	for item in msg.items():
		# 		file.write("%s: %s\n" % (item[0], item[1]))
		# 		print(item[0], ": ", item[1])
		content = BeautifulSoup(msg.Content, 'xml')
		if(content.emoji):
			# cdnurl = content.emoji.attrs['cdnurl']
			# with open("stickerLog.txt","a") as file:
			# 	file.write("%s\n" % cdnurl)
			# itchat.send_raw_msg(msg["MsgType"], msg["Content"], msg["FromUserName"])
			# content = xmltodict.parse(content)
			# content = json.dumps(content)
			# print(content)
			msg['Text'](os.path.join(STICKER_DIR, msg.fileName))
			itchat.send_image(os.path.join(STICKER_DIR, msg.fileName), msg['FromUserName'])
			# return cdnurl
		else:
			# msg['Text'](msg.fileName)
			# itchat.send_image(msg.fileName, msg['FromUserName'])
			itchat.send_image('sticker/facepalm.gif', msg['FromUserName'])

	def getReply(msg):
		nonlocal cache
		# print(msg)
		# print(msg['Type'])
		# print(msg['MsgType'])
		fromUser = msg["FromUserName"]
		if(not fromUser in cache):
			cache[fromUser] = {
				'flag': True,
				'unreply_num': 0,
				'unreply_wait': -1,
				'msg': []
			}
		if(cache[fromUser]['flag'] and msg.text == stop):
			cache[fromUser]['flag'] = False
			print("Pause auto replying")
		elif(not cache[fromUser]['flag'] and msg.text == restart):
			cache[fromUser]['flag'] = True
			print("Restart auto replying")
		if(cache[fromUser]['flag']):
			if(msg['Type'] == TEXT):
				return reply_text(msg)
			elif(msg['MsgType'] == 47):
				return reply_sticker(msg)
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

def funnyWrapper():
	funnyDict = {'hhh', '。。。', '哈哈哈'}
	def funny(msg):
		for word in funnyDict:
			if word in msg.text:
				return True
		return False
	return funny

getReply = replyWrapper()
is_funny = funnyWrapper()

signature = ' ----来自Kimthe1st聊天机器人'
header = '[系统自动回复] '
stop = '苟利国家生死以'
restart = '岂因祸福避趋之'
emotions = ('[微笑]','[撇嘴]','[色]','[发呆]','[得意]','[流泪]','[害羞]','[闭嘴]','[睡]','[大哭]','[尴尬]','[发怒]','[调皮]','[呲牙]','[惊讶]','[难过]','[囧]','[抓狂]','[吐]','[偷笑]','[愉快]','[白眼]','[傲慢]','[困]','[惊恐]','[流汗]','[憨笑]','[悠闲]','[奋斗]','[咒骂]','[疑问]','[嘘]','[晕]','[衰]','[骷髅]','[敲打]','[再见]','[擦汗]','[抠鼻]','[鼓掌]','[坏笑]','[左哼哼]','[右哼哼]','[哈欠]','[鄙视]','[委屈]','[快哭了]','[阴险]','[亲亲]','[可怜]','[菜刀]','[西瓜]','[啤酒]','[咖啡]','[猪头]','[玫瑰]','[凋谢]','[嘴唇]','[爱心]','[心碎]','[蛋糕]','[炸弹]','[便便]','[月亮]','[太阳]','[拥抱]','[强]','[弱]','[握手]','[胜利]','[抱拳]','[勾引]','[拳头]','[OK]','[跳跳]','[发抖]','[怄火]','[转圈]',
		# '😄','😷','😂','😝','😳','😱','😔','😒',
		'[嘿哈]','[捂脸]','[奸笑]','[机智]','[皱眉]','[耶]',
		# '👻','🙏','💪','🎉','📦',
		'[红包]','[鸡]')

MAX_UNREPLY = 3