#/Pr_Tools/Python/autobackup/menu.py, v1.0.1, 2020.01.08

import nuke
import autoback

nuke.addOnScriptSave(autoback.savebackup)