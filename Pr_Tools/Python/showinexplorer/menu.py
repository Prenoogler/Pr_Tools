#Pr_Tools/Python/showinexplorer/memu.py, v1.0.1, 2020.01.10
import nuke
import showinexplorer

for node in ['Write','Read']:
	nuke.addOnCreate(lambda:showinexplorer.addbutton(),nodeClass=node)