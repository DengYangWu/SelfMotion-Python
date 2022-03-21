import os
import time
from glob import glob
import shell
import ast

r='D:\\ftp\\'

#获取apk大小为0的文件，并移除
for filename in glob(r+'*.apk'):
    size=os.path.getsize(filename)
    if size==0:
        os.remove(filename)
#清除apk里的内容
for file_jg in glob(r+'*.apk'):

    filename=os.path.splitext(file_jg)[0]
    filetype = os.path.splitext(file_jg)[1]
    newfile=os.path.join(filename+"_"+filetype)
    os.rename(file_jg,newfile)
    f = open(newfile, 'w+')
    f.truncate()
    f.close()
    os.remove(file_jg)
    #print(filetype)




