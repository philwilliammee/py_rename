#!/usr/bin/env python3
import os
import sys
from distutils.dir_util import copy_tree
import shutil
import stat
import py_common as common

SRC_FILE_NAME_TO_REPLACE = "foo_bar"
SRC_STRING_TO_REPLACE = "foo_bar"

DEST_NEW_FILE_NAME = "hello_world"
DEST_NEW_STRING = "Hello World"

SRC = "src/"
DEST = "dest/"
TEST_DIR = "test/"
DO_TEST = True

# Copies a folder and contents to temp directory
def copy_folder(src, dest):
    # deletes the dest directory if it exists
    if (os.path.isdir("./{}".format(dest))):
        shutil.rmtree("./{}".format(dest), onerror=common.del_evenReadonly)
    fromDirectory = "./{}".format(src)
    toDirectory = "./{}".format(dest)
    copy_tree(fromDirectory, toDirectory)


def replaceFileText(fp, old, new):
    # fin = open(fp, "rt")
    # for line in fin:
    #     fout.write(line.replace(old, new))
    f = open(fp, 'r')
    s = f.read()
    f.close()
    
    f = open(fp, 'w')
    s = s.replace(old, new)
    
    f.write(s)
    f.close()


def convert_names(src, dest, old_string, new_string, old_filename, new_filename):
    for currentpath, dirs, files in os.walk(dest):
        for file in files:
            # replace windows paths
            filePath = os.path.join(currentpath, file).replace("\\", "/")

            replaceFileText(filePath, old_string, new_string)
            # not sure why I'm doing it this way and not just saving the file with a new name?
            newFilePath = filePath.replace(old_filename, new_filename)
            print(filePath)
            os.rename(filePath, newFilePath)
            print(newFilePath)


if __name__ == "__main__":
    if DO_TEST:
        SRC = TEST_DIR
    copy_folder(SRC, DEST)
    convert_names(SRC, DEST, SRC_STRING_TO_REPLACE, DEST_NEW_STRING, SRC_FILE_NAME_TO_REPLACE, DEST_NEW_FILE_NAME)
