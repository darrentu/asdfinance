import json
import urllib2
import sys
#cue support
# from cue_sdk import *
# Corsair = CUESDK("CUESDK.x64_2013.dll")
# Corsair.RequestControl(CAM.ExclusiveLightingControl)
foods = ["Restaurant", "Fast Food", "Alcohol & Bars",]
ents = ["Travel", "Shopping", "Entertainment"]
necs = ["Groceries", "Home Improvement"]
food = []
ent = []
nec = []

mint =  json.load(urllib2.urlopen("http://intuit-mint.herokuapp.com/api/v1/user/transactions"))
for i in mint:
	if i['category'] in foods:
		food.append((-1*i['amount'], i['name']))
	elif i['category'] in ents:
		ent.append((-1*i['amount'], i['name']))
	elif i['category'] in necs:
		nec.append((-1*i['amount'], i['name']))

ftot = 0
etot = 0
ntot = 0
i = 0
while raw_input() == "next":
	ftot += food[i][0]
	etot += ent[i][0]
	ntot += nec[i][0]
	print ftot
	print etot
	print ntot