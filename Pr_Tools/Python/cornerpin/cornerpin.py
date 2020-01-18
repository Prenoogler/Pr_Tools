#Pr_Tools\Python\cornerpin, v1.0.2, 2020.01.10
import nuke

def cornerpinsetreference():
    nuke.thisNode()['copy_to'].execute()
    nuke.thisNode()['from1'].clearAnimated()
    nuke.thisNode()['from2'].clearAnimated()
    nuke.thisNode()['from3'].clearAnimated()
    nuke.thisNode()['from4'].clearAnimated()

def addfunction():
	if 'function' not in nuke.thisNode().knobs().keys():
		nuke.thisNode().addKnob(nuke.Tab_Knob('function', 'Function'))
		nuke.thisNode().addKnob(nuke.PyScript_Knob('setref','Set Reference','cornerpin.cornerpinsetreference()'))
	else:
		print('cornerpin have function tab!')