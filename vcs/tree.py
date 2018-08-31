import os

def make_tree(path):
    listdir = os.listdir(path)
    topdir = os.walk(path)
    i = 0
    for dir in topdir:
        # print(dir[0])
        if len(dir[1]) > 1:
            for direct in dir[1]:
                print('\t'*i, direct)
                if len(dir[2]) > 1:
                    for file in dir[2]:
                        print('\t'*i, '\t', file)
        i += 1
