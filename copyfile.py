import re

import os


for root, dirs, files in os.walk("E:\俄罗斯方块视频"):
    # for name in files:
    #     print(name)
    for dir in dirs:
        print(os.path.join(root, dir))
        dircname = re.search("[\u5408][\u5e76]+$", dir)
        if dircname:
            f