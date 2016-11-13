import json
import urllib2
import sys
from flask import Flask, render_template
from flask_socketio import SocketIO
import time

#cue support
#from cue_sdk import *



foods = ["Restaurant", "Fast Food", "Alcohol & Bars",]
ents = ["Shopping", "Entertainment", "Electronics & Software"] #"Travel", 
necs = ["Groceries", "Home Improvement"]
food = []
ent = []
nec = []
fkeys = []
ekeys = []
nkeys = []
mode = 2

col1 = [5, 2, 3, 4, 14, 15, 16, 17, 26, 27, 28, 29, 38, 39, 40, 41, 49, 51, 52, 53]
col2 = [6, 7, 8, 9, 19, 20, 21, 22, 31, 32, 33, 34, 43, 44, 45, 46, 55, 56, 57, 58]
col3 = [10, 11, 12, 73, 24, 85, 87, 36, 80, 81, 48, 83, 60, 91]
col4 = range(103, 121)
whitecols = [18, 30, 42, 54, 23, 35, 47, 59]

row1 = range(25, 37)
row2 = range(37, 49)
row3 = range(49, 61)
row4 = range(14, 25)+[85]


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
	else:
		a = 255//g
	r *= a
	g *= a
	return (int(r), int(g))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('userinput')
def receive(userinput):
	global uinp
	uinp = json.loads(userinput)

@socketio.on('mode')
def chmd(md):
	global mode
	global uinp
	global myout

	mode = md

	


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

	

if __name__ == '__main__':
    socketio.run(app)