import os
import time
from glob import glob
import shell
r='D:\\ftp\\'
#删除老apk
old_apk='D:/ftp/redmeeting.apk'
if os.path.exists(old_apk):
    os.remove(old_apk)
    # res = shell.SHFileOperation((0, shellcon.FO_DELETE, old_apk, None,
    #                              shellcon.FOF_SILENT | shellcon.FOF_ALLOWUNDO | shellcon.FOF_NOCONFIRMATION, None,
    #                              None))  # 删除文件到回收站
    # if not res[1]:
    #     os.system('del ' + old_apk)
    print("已删除")
for file_jg in glob(r+'*_jiagu_sign.apk'):
    os.remove(file_jg)


#筛选最新的apk
file_result = os.listdir(r)
file_result.sort(key=lambda fn: os.path.getctime(r + fn), reverse=True)
os.rename(r + file_result[0], r + "redmeeting.apk")


