import zipfile
import os
import hashlib
import lxml import etre

root = '/home/psyc0p4th/roms/snes/'
dat = '/home/psyc0p4th/roms/dat/SNES.dat'
ok_count = notOk_count = 0


for path, subdirs, files in os.walk(root):
    for name in files:
        filePath = os.path.join(path, name)
        if name[-3:] == 'zip':
            archive = zipfile.ZipFile(filePath, 'r')
            romFileName = archive.namelist()[0]
            rom = archive.read(romFileName)
        elif name[-3:] is 'smc' or name[-3:] is 'smc':
            file = open(filePath, 'r')
            rom = file.read()
        if 'rom' in locals():
            print("sha1 : ", hashlib.sha1(rom).hexdigest(),
                  "\tmd5 :", hashlib.md5(rom).hexdigest(),
                  "\t", name)
