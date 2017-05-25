import itchat

itchat.auto_login()
friends = itchat.get_friends()

friend_count = len(friends)
print("%d friends in total" % friend_count)
for i in range(friend_count):
	fd = friends[i]
	if(not fd.RemarkName):
		name = fd.RemarkName
	else:
		name = fd.NickName
	print("%d %s" % ((i, name))

# itchat.create_chatroom([])['MemberList'][-1]['MemberStatus']