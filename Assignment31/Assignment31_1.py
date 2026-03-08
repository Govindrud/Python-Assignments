import sys
import os

def DirectoryScanner(DirName):
    Ret = False

    Ret = os.path.exists(DirName)

    if (Ret== False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if (Ret == False):
        print("It is not a directory")
        return
