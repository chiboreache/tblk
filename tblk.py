#!/bin/python
from subprocess import check_output
from prettytable import PrettyTable

f = check_output(["lsblk", "--raw"]).decode("utf-8")
ff = check_output(["lsblk", "-f", "--raw"]).decode("utf-8")

l = f.split('\n')
lf = ff.split('\n')
stringCount = len(lf) - 1

listName = []; listSize = []; listFs = []; listUUID = []; listMp = [];

for i in range(stringCount):
    name, maj, rm, size, ro, typ, mp = l[i].split(' ')
    name_, fs, lbl, uuid, mp_ = lf[i].split(' ')
    listName.append(name)
    listSize.append(size)
    listFs.append(fs)
    listUUID.append(uuid)
    listMp.append(mp)

pt = PrettyTable()
pt.add_column(listName[0],listName[1:])
pt.add_column(listSize[0],listSize[1:])
pt.add_column(listFs[0],listFs[1:])
pt.add_column(listUUID[0],listUUID[1:])
pt.add_column(listMp[0],listMp[1:])
print(pt)
