#OneKeyInstaller.py, v1.0.2, 2020.01.18

import os
import shutil

print('即将安装Pr_Tools(www.shuaiqi.me/tools)')
os.system('pause')

userdir=os.environ['HOMEDRIVE']+os.environ['HOMEPATH']

if not os.path.exists(userdir+'\\.nuke'):
    print('未检测到.nuke文件夹，请检查是否已正确安装Nuke或参照 www.shuaiqi.me/tools 尝试手动安装')
    os.system('pause')
    exit(0)
try:
    if not os.path.exists(userdir+'\\.nuke\\init.py'):
        createinit=open(userdir+'\\.nuke\\init.py','w')
        createinit.close()
        print('init.py文件不存在，已创建成功')
    else:
        print('init.py文件已存在，不执行操作')
    with open(userdir+'\\.nuke\\init.py','r+',errors='ignore') as r:
        if "nuke.pluginAddPath('./Pr_Tools')" not in r.read():
            r.write("\nnuke.pluginAddPath('./Pr_Tools')")
            print('init.py语句不存在，已写入成功')
        else:
            print('init.py语句已存在，不执行操作')
    if os.path.exists(userdir+'\\.nuke\\Pr_Tools'):
        shutil.rmtree(userdir+'\\.nuke\\Pr_Tools')
        shutil.copytree('.\\Pr_Tools',userdir+'\\.nuke\\Pr_Tools')
        print('Pr_Tools文件夹已存在，已重装成功')
    else:
        shutil.copytree('.\\Pr_Tools',userdir+'\\.nuke\\Pr_Tools')
        print('Pr_Tools文件夹不存在，已创建成功')
except:
    print('安装失败，请参照 www.shuaiqi.me/tools 尝试手动安装')
else:
    print('安装成功，请重启Nuke')
finally:
    os.system('pause')

