import appread
import os
EXTREME = 5
HIGH = 4
MEDIUM = 3
NORMAL = 2
SMALL = 1
EXTREME_SMALL = 0

ADMINSTATOR = {"name": "ADMINSTATOR", "LEVEL": HIGH}
INTELLIGENTE = {"name": "INTELLIGENTE", "LEVEL": EXTREME}
USER = {"name": "USER", "LEVEL": MEDIUM}
RESTRICTED = {"name": "RESTRICTED", "LEVEL": NORMAL}
SMALLU = {"name": "SMALLU", "LEVEL": SMALL}
NONE = {"name": "NONE", "LEVEL": EXTREME_SMALL}

PERMISSIONS = [ADMINSTATOR, INTELLIGENTE, USER, RESTRICTED, SMALLU, NONE]
PERMISSION = PERMISSIONS[1]
VIRTUAL = True if "Hyper" in appread.apps else False
if VIRTUAL:
    PERMISSION = PERMISSIONS[3]
    os.system("msg * Warning: Running DataGarm on a Virtual Machine is not supported the permission is: Restricted. Counintue?")
'''
Operator files. If the user tries to modify or delete them PermissonERR() will execute in PERMISSON_FINDER.py
'''
OPF=[] 
C = {"Name": "C:"} # A drive
D = {"Name": "D:"} # A drive
OPDRS=[C]
DRS = [D]
F = []
OPF = []
C = {"Name": "C:"}
OPD = [C]
D = "???"
F = "???"
