import json
import urllib2
import sys
from flask import Flask, render_template
from flask_socketio import SocketIO
import time

#cue support
from cue_sdk import *



foods = ["Restaurant", "Fast Food", "Alcohol & Bars",]
ents = ["Travel", "Shopping", "Entertainment", "Electronics & Software"]
necs = ["Groceries", "Home Improvement"]
food = []
ent = []
nec = []
fkeys = []
ekeys = []
nkeys = []
mode = 0

col1 = [1, 2, 3, 4, 14, 15, 16, 17, 26, 27, 28, 29, 38, 39, 40, 41, 49, 51, 52, 53]
col2 = [6, 7, 8, 9, 19, 20, 21, 22, 31, 32, 33, 34, 43, 44, 45, 46, 55, 56, 57, 58]
col3 = [10, 11, 12, 73, 24, 85, 87, 36, 80, 81, 48, 83, 60, 91]
col4 = range(103, 121)

row1 = range(25, 37)
row2 = range(37, 49)
row3 = range(49, 61)
row4 = range(14, 25).append(85)


mint =  json.load(urllib2.urlopen("http://intuit-mint.herokuapp.com/api/v1/user/transactions"))
l = len(mint)//30

#userinput and my ouput
uinp = {
	'f': 0.2,
	'e': 0.2,
	'n': 0.3,
	'b': 1000
}

myout = {
	'f': 0,
	'e': 0,
	'n': 0,
	'd': 0
}

def colorMaker(actual, ideal):
	tot = actual+ideal
	r = (255*actual)//tot
	g = (255*ideal)//tot
	a = 0
	if r > g:
		a = 255//r
	else 
		a = 255//g
	r *= a
	g *= a
	return (r, g)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('userinput')
def receive(userinput):
	global uinp
    uinp = json.decode(userinput)

@socketio.on('mode')
def chmd(md):
	global mode
	mode = md

	Corsair = CUESDK("CUESDK.x64_2015.dll")
	Corsair.RequestControl(CAM.ExclusiveLightingControl)
	if mode == 0:
		r, g = colorMaker(myout['f'], uinp['f']*uinp['b']*myout['d']//30)
		for key in col1:
			Corsair.SetLedsColors(CorsairLedColor(key, r, g, 0))

		r, g = colorMaker(myout['e'], uinp['e']*uinp['b']*myout['d']//30)
		for key in col2:
			Corsair.SetLedsColors(CorsairLedColor(key, r, g, 0))

		r, g = colorMaker(myout['n'], uinp['n']*uinp['b']*myout['d']//30)
		for key in col3:
			Corsair.SetLedsColors(CorsairLedColor(key, r, g, 0))

		r, g = colorMaker(myout['f'] + myout['e'] + myout['n'], 
						  (1 - uinp['f'] - uinp['e'] - uinp['n']) * 
					      uinp['b']*myout['d']//30)
		for key in col4:
			Corsair.SetLedsColors(CorsairLedColor(key, r, g, 0))
	elif mode == 1:
		tot = (myout['f']+myout['e']+myout['n'])
		if tot >= uinp['b']*(1 - uinp['f'] - uinp['e'] - uinp['n']):
			for i in range(0, 12):
				Corsair.SetLedsColors(
					CorsairLedColor(row1[i], 255, 0, 0), 
					CorsairLedColor(row2[i], 255, 0, 0), 
					CorsairLedColor(row3[i], 255, 0, 0))
				time.sleep(.1)
		else:
			keys = tot * 12 // (uinp['b']*(1 - uinp['f'] - uinp['e'] - uinp['n']))
			for i in range(0, keys+1):
				Corsair.SetLedsColors(
					CorsairLedColor(row1[i], 0, 255, 0), 
					CorsairLedColor(row2[i], 0, 255, 0), 
					CorsairLedColor(row3[i], 0, 255, 0))
				time.sleep(.1)
	elif mode == 2:
		#total bar
		tot = (myout['f']+myout['e']+myout['n'])
		if tot >= uinp['b']*(1 - uinp['f'] - uinp['e'] - uinp['n']):
			for i in range(0, 12):
				Corsair.SetLedsColors(CorsairLedColor(row4[i], 255, 0, 0)) 
				time.sleep(.1)
		else:
			keys = tot * 12 // (uinp['b']*(1 - uinp['f'] - uinp['e'] - uinp['n']))
			for i in range(0, keys+1):
				Corsair.SetLedsColors(CorsairLedColor(row4[i], 0, 255, 0))
				time.sleep(.1)

		#food
		r, g = colorMaker(myout['f'], uinp['f']*uinp['b']*myout['d']//30)
		keys = myout['f'] * 12 // (uinp['b']*uinp['f'])
		if keys > 11:
			for k in row1:
				Corsair.SetLedsColors(CorsairLedColor(k, 255, 0, 0))
		else:
			for i in range(0, keys+1):
				Corsair.SetLedsColors(CorsairLedColor(row1[key], r, g, 0))

		#ent
		r, g = colorMaker(myout['e'], uinp['e']*uinp['b']*myout['d']//30)
		keys = myout['e'] * 12 // (uinp['b']*uinp['e'])
		if keys > 11:
			for k in row2:
				Corsair.SetLedsColors(CorsairLedColor(k, 255, 0, 0))
		else:
			for i in range(0, keys+1):
				Corsair.SetLedsColors(CorsairLedColor(row2[key], r, g, 0))

		#nec
		r, g = colorMaker(myout['n'], uinp['n']*uinp['b']*myout['d']//30)
		keys = myout['n'] * 12 // (uinp['b']*uinp['n'])
		if keys > 11:
			for k in row3:
				Corsair.SetLedsColors(CorsairLedColor(k, 255, 0, 0))
		else:
			for i in range(0, keys+1):
				Corsair.SetLedsColors(CorsairLedColor(row3[key], r, g, 0))


@socketio.on('nextday')
def nextDay():
	global uinp
	global myout
	global mint
	global l
	global food
	global ent
	global nec
	global col1
	global col2
	global col3
	global col4

	if myout['d'] > 30:
		myout['d'] = 0
		mint =  json.load(urllib2.urlopen("http://intuit-mint.herokuapp.com/api/v1/user/transactions"))
		l = len(mint)//30
		myout['f'] = 0
		myout['e'] = 0
		myout['n'] = 0

	for k in range(l*myout['d'], l*(myout['d']+1)):
		t = mint[k]
		if t['category'] in foods:
			food.append((-1*t['amount'], t['name']))
			myout['f']+=-1*t['amount']
		elif t['category'] in ents:
			ent.append((-1*t['amount'], t['name']))
			myout['e']+=-1*t['amount']
		elif t['category'] in necs:
			nec.append((-1*t['amount'], t['name']))
			myout['n']+=-1*t['amount']

	socketio.emit('parsedmint', myout)
	myout['d'] += 1


	Corsair = CUESDK("CUESDK.x64_2015.dll")
	Corsair.RequestControl(CAM.ExclusiveLightingControl)
	if mode == 0:
		r, g = colorMaker(myout['f'], uinp['f']*uinp['b']*myout['d']//30)
		for key in col1:
			Corsair.SetLedsColors(CorsairLedColor(key, r, g, 0))

		r, g = colorMaker(myout['e'], uinp['e']*uinp['b']*myout['d']//30)
		for key in col2:
			Corsair.SetLedsColors(CorsairLedColor(key, r, g, 0))

		r, g = colorMaker(myout['n'], uinp['n']*uinp['b']*myout['d']//30)
		for key in col3:
			Corsair.SetLedsColors(CorsairLedColor(key, r, g, 0))

		r, g = colorMaker(myout['f'] + myout['e'] + myout['n'], 
						  (1 - uinp['f'] - uinp['e'] - uinp['n']) * 
					      uinp['b']*myout['d']//30)
		for key in col4:
			Corsair.SetLedsColors(CorsairLedColor(key, r, g, 0))
	elif mode == 1:
		tot = (myout['f']+myout['e']+myout['n'])
		if tot >= uinp['b']*(1 - uinp['f'] - uinp['e'] - uinp['n']):
			for i in range(0, 12):
				Corsair.SetLedsColors(
					CorsairLedColor(row1[i], 255, 0, 0), 
					CorsairLedColor(row2[i], 255, 0, 0), 
					CorsairLedColor(row3[i], 255, 0, 0))
				time.sleep(.1)
		else:
			keys = tot * 12 // (uinp['b']*(1 - uinp['f'] - uinp['e'] - uinp['n']))
			for i in range(0, keys+1):
				Corsair.SetLedsColors(
					CorsairLedColor(row1[i], 0, 255, 0), 
					CorsairLedColor(row2[i], 0, 255, 0), 
					CorsairLedColor(row3[i], 0, 255, 0))
				time.sleep(.1)
	elif mode == 2:
		#total bar
		tot = (myout['f']+myout['e']+myout['n'])
		if tot >= uinp['b']*(1 - uinp['f'] - uinp['e'] - uinp['n']):
			for i in range(0, 12):
				Corsair.SetLedsColors(CorsairLedColor(row4[i], 255, 0, 0)) 
				time.sleep(.1)
		else:
			keys = tot * 12 // (uinp['b']*(1 - uinp['f'] - uinp['e'] - uinp['n']))
			for i in range(0, keys+1):
				Corsair.SetLedsColors(CorsairLedColor(row4[i], 0, 255, 0))
				time.sleep(.1)

		#food
		r, g = colorMaker(myout['f'], uinp['f']*uinp['b']*myout['d']//30)
		keys = myout['f'] * 12 // (uinp['b']*uinp['f'])
		if keys > 11:
			for k in row1:
				Corsair.SetLedsColors(CorsairLedColor(k, 255, 0, 0))
		else:
			for i in range(0, keys+1):
				Corsair.SetLedsColors(CorsairLedColor(row1[key], r, g, 0))

		#ent
		r, g = colorMaker(myout['e'], uinp['e']*uinp['b']*myout['d']//30)
		keys = myout['e'] * 12 // (uinp['b']*uinp['e'])
		if keys > 11:
			for k in row2:
				Corsair.SetLedsColors(CorsairLedColor(k, 255, 0, 0))
		else:
			for i in range(0, keys+1):
				Corsair.SetLedsColors(CorsairLedColor(row2[key], r, g, 0))

		#nec
		r, g = colorMaker(myout['n'], uinp['n']*uinp['b']*myout['d']//30)
		keys = myout['n'] * 12 // (uinp['b']*uinp['n'])
		if keys > 11:
			for k in row3:
				Corsair.SetLedsColors(CorsairLedColor(k, 255, 0, 0))
		else:
			for i in range(0, keys+1):
				Corsair.SetLedsColors(CorsairLedColor(row3[key], r, g, 0))




if __name__ == '__main__':
    socketio.run(app)