import re
import os
import shutil

for root, dirs, files in os.walk("E:\俄罗斯方块视频"):
    for dir in dirs:
        # print(os.path.join(root, dir))
        dirname = re.search("[\u5408\u5e76]+$", dir)
        if dirname:
            listfile=os.listdir(root+'\\'+dir)
            source_path = os.path.join(root+'\\'+dir, listfile[0])
            print('源文件：',source_path)
            newfilename='e:\\test\\'+listfile[0]
            print('目标文件:',newfilename)
            shutil.copyfile(source_path,newfilename)


