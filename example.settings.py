#!/usr/bin/env python3

'''
 ------------------ SETTINGS -------------------
'''

SRC_FILE_NAME_TO_REPLACE = "foo_bar"
# SRC_STRING_TO_REPLACE = "foo_bar"

DEST_NEW_FILE_NAME = "hello_world"
# DEST_NEW_STRING = "Hello World"

REPLACE = [
    {'src':'foo' , 'dest':'hello'},
    {'src':'bar', 'dest':'world'},
]

SRC = "src/"
DEST = "dest/"
TEST_DIR = "test/"
DO_TEST = True

''' ------------ end of settings --------- '''