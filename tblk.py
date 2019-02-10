#!/bin/python
from subprocess import check_output
from prettytable import PrettyTable


std_out_lsblk = check_output(["lsblk", "--raw"]).decode("utf-8")
std_out_lsblk_f = check_output(["lsblk", "-f", "--raw"]).decode("utf-8")


std_out_lsblk_list = std_out_lsblk.split('\n')
std_out_lsblk_f_list = std_out_lsblk_f.split('\n')


lsblk_headers = ['NAME', 'MAJ:MIN', 'RM', 'SIZE', 'RO', 'TYPE', 'MOUNTPOINT']
lsblk_f_headers = ['NAME', 'FSTYPE', 'LABEL', 'UUID', 'FSAVAIL', 'FSUSE', 'MOUNTPOINT']
tblk_headers = dict(
    NAME='NAME',
    FSTYPE='FSTYPE',
    LABEL='LABEL',
    UUID='UUID',
    FSAVAIL='FSAVAIL',
    FSUSE='FSUSE',
    MOUNTPOINT='MOUNTPOINT',
    SIZE='SIZE',
)
(
    ls_NAME,
    ls_FSTYPE,
    ls_LABEL,
    ls_UUID,
    ls_FSAVAIL,
    ls_FSUSE,
    ls_MOUNTPOINT,
    ls_SIZE,
    ) = [list() for _ in range(len(tblk_headers))]


for i in range(1, len(std_out_lsblk_f_list) - 1):
    lsblk_list_unpack = std_out_lsblk_list[i].split(' ')
    lsblk_dict = dict(zip(lsblk_headers, lsblk_list_unpack))

    lsblk_f_list_unpack = std_out_lsblk_f_list[i].split(' ')
    lsblk_f_dict = dict(zip(lsblk_f_headers, lsblk_f_list_unpack))

    ls_NAME.append(lsblk_dict['NAME'])
    ls_MOUNTPOINT.append(lsblk_dict['MOUNTPOINT'])
    ls_SIZE.append(lsblk_dict['SIZE'])

    ls_FSTYPE.append(lsblk_f_dict['FSTYPE'])
    ls_LABEL.append(lsblk_f_dict['LABEL'])
    ls_UUID.append(lsblk_f_dict['UUID'])
    ls_FSAVAIL.append(lsblk_f_dict['FSAVAIL'])
    ls_FSUSE.append(lsblk_f_dict['FSUSE'])


pt = PrettyTable()
pt.add_column(tblk_headers['NAME'], ls_NAME[1:])
pt.add_column(tblk_headers['FSTYPE'], ls_FSTYPE[1:])
pt.add_column(tblk_headers['MOUNTPOINT'], ls_MOUNTPOINT[1:])
pt.add_column(tblk_headers['SIZE'], ls_SIZE[1:])
pt.add_column(tblk_headers['FSUSE'], ls_FSUSE[1:])
pt.add_column(tblk_headers['FSAVAIL'], ls_FSAVAIL[1:])
pt.add_column(tblk_headers['UUID'], ls_UUID[1:])
print(pt)
