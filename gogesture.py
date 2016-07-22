# Gesture GO created by Weiqi 
# 07-19-2016
#!/usr/bin/env python
import subprocess
import os
import time

# touch parameter 
EV_SYN = 0
EV_ABS = 3
EV_NUMBER = 0

SYN_REPORT = 0;

#ABS_MT_SLOT = 47;
#ABS_MT_TOUCH_MAJOR = 48;
#ABS_MT_POSITION_X = 53;
#ABS_MT_POSITION_Y = 54;
#ABS_MT_TRACKING_ID = 57;
#ABS_MT_PRESSURE = 58;

#ADB command

#SENDEVENT_CMD = 'sendevent '
#EVENT_LOCATION = '/dev/input/'
#EVENT_ID = 'event1'

SHELL_CMD = 'adb shell '
CMD_INPUT = 'input '
CMD_SWIPE = 'swipe '
CMD_TAP = 'tap '
CMD_KEY = 'keyevent '

ABS_MOV_START_X = 300
ABS_MOV_START_Y = 300
ABS_MOV_END_RX = 400
ABS_MOV_END_LX = 200
ABS_MOV_END_Y = 400

ABS_MOV_SPD_SLOW = 1200
ABS_MOV_SPD_NML = 800
ABS_MOV_SPD_FAST = 400
ABS_MOV_SPD_SUPER = 100

ABS_MOV_LEFT_ROTATE_X = 0
ABS_MOV_RIGHT_ROTATE_X = 600
ABS_MOV_SPD_ROTATE = 1000
CMD_BACK_KEY = 4


# Main Menu
def showMenu():
	print '- Gesture GO Action List:'
	print '- [m]: Main Menu'
	print '- [b]: Back'
	print '- [c]: Click 9 block square'
	print '----  [c1] [c2] [c3]'
	print '----  [c4] [c5] [c6]'
	print '----  [c7] [c8] [c9]'
	print '- [l1]: Left rotate'
	print '- [r1]: Right rotate'
	print '- [q]: Quit'
	print '--- Waiting for your action: ---'

def doAction(action):
	os.popen(action)
	return

def actionCMD(param1, param2, param3):
	actioncmd = SENDEVENT_CMD + EVENT_LOCATION + EVENT_ID + ' ' + param1 + ' ' + param2 + ' ' + param3
	return actioncmd

def actionReport():
	cmd = actionCMD(0,0,0)
	return cmd

def actionPress():
	cmd = actionCMD(1, 330, 1)
	return cmd

def actionRelease():
	cmd = actionCMD(1, 330, 1)
	return cmd

def actionPosition(x, y):
	cmd = actionCMD()
	return cmd

def actionSwipeXY(x1, x2, y1, y2, speed):
	action = SHELL_CMD + CMD_INPUT + CMD_SWIPE + str(x1) + ' ' + str(x2) + ' ' + str(y1) + ' ' + str(y2) + ' ' + str(speed)
	doAction(action)
	return

def actionPress(key):
	aciton = SHELL_CMD + CMD_INPUT + CMD_KEY + str(key)
	print action
	doAction(action)
	return

def actionEnd():
	cmd = actionCMD()
	return cmd

def actionMainMenu():
	actionTAP()
	return

def actionMovLeft():
	actionSwipeXY(ABS_MOV_START_X, ABS_MOV_START_Y, ABS_MOV_END_LX, ABS_MOV_END_Y, ABS_MOV_SPD_NML)
	return
def actionMovRight():
	actionSwipeXY(ABS_MOV_START_X, ABS_MOV_START_Y, ABS_MOV_END_RX, ABS_MOV_END_Y, ABS_MOV_SPD_NML)
	return

def actionMovLeftFast():
	actionSwipeXY(ABS_MOV_START_X, ABS_MOV_START_Y, ABS_MOV_END_LX, ABS_MOV_END_Y, ABS_MOV_SPD_FAST)
	return
def actionMovRightFast():
	actionSwipeXY(ABS_MOV_START_X, ABS_MOV_START_Y, ABS_MOV_END_RX, ABS_MOV_END_Y, ABS_MOV_SPD_FAST)
	return

def actionMovLeftRotate():
	while True:
		actionSwipeXY(ABS_MOV_START_X, ABS_MOV_START_Y, ABS_MOV_LEFT_ROTATE_X, ABS_MOV_LEFT_ROTATE_X, ABS_MOV_SPD_ROTATE)
	return

def actionMovRightRotate():
	while True:
		actionSwipeXY(ABS_MOV_START_X, ABS_MOV_START_Y, ABS_MOV_RIGHT_ROTATE_X, ABS_MOV_RIGHT_ROTATE_X, ABS_MOV_SPD_ROTATE)
	return

def actionBack():
	actionPress(CMD_BACK_KEY)
	return

def action9C():
	return


showMenu()

while True:
	action = raw_input('INPUT: ')
	if action is not None :
		if action == "m" :
			print 'press m'
		if action == "l" :
			actionMovLeft()
		if action == "lf" :
			actionMovLeftFast()
		if action == "rl" :
			actionMovLeftRotate()
		if action == "r" :
			actionMovRight()
		if action == "rf" :
			actionMovRightFast()
		if action == "rr" :
			actionMovRightRotate()
		if action == "b":
			os.popen('adb shell input keyevent 4')
		if action == "q" :
			print '.....Quit'
			break

#Waiting for the action
#action = raw_input("Input Command: ")
#print action


#Actions:
#1. main button
#2. back button
#3. click 9 blick square: c1 ~ c9
## click center: c5

#run ellipse
## moving like a ellipse