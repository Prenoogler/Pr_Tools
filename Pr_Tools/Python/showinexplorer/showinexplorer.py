#Pr_Tools/Python/showinexplorer/showinexplorer.py, v1.0.2, 2020.01.10
import nuke
import os
import subprocess

def open():
	file=os.path.split(nuke.thisNode()['file'].value())[0]
	print(file)
	file=file.replace('/', '\\').decode('utf-8').encode('GB2312')
	subprocess.Popen(['explorer',file])


def addbutton():
	if 'function' not in nuke.thisNode().knobs().keys():
		nuke.thisNode().addKnob(nuke.Tab_Knob('function', 'Function'))
		nuke.thisNode().addKnob(nuke.PyScript_Knob('show','Show in Explorer'))
		nuke.thisNode()['show'].setCommand("showinexplorer.open()")
	else:
		print('read,write have function tab!')