#/Pr_Tools/Python/autobackup/autoback.py, v1.0.1, 2020.01.08

import nuke
import os
import time

def backupfolder():
	backuproot=os.path.expanduser('~')+'/.nuke/pr_backup/'+os.path.basename(nuke.root().name()).split('.')[0]
	if not os.path.exists(backuproot):
		os.makedirs(backuproot)
	return backuproot



def deletextra(number):
	allist=os.listdir(backupfolder())
	allist.sort()
	if len(allist)>number:
		deletelist=allist[:-number]
		for nk in deletelist:
			os.remove(backupfolder()+'/'+nk)

def savebackup():
	save=backupfolder()+'/'+time.strftime('%Y_%m_%d_%H_%M', time.localtime(time.time()))+'_'+os.path.basename(nuke.root().name()).split('.')[0]+'.nk'
	try:
		nuke.removeOnScriptSave(savebackup)
		nuke.scriptSave(save)
		nuke.addOnScriptSave(savebackup)
	except:
		nuke.message('Backup failed!(Pr_ToolKit)')