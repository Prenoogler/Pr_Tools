#Pr_Tools\Python\cornerpin, v1.0.1, 2020.01.10
import nuke
import cornerpin

nuke.addOnCreate(cornerpin.addfunction,nodeClass='CornerPin2D')