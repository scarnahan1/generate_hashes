#!/usr/bin/env python3

# Author - Shane Carnahan
# Email - Shane.Carnahan1@gmail.com
# Date - 9/12/19
# Project - mlh_network_staging
# Version - 1.0


import hashlib
import os

from get_files import get_files_list

def create_md5(working_dir):
    files = get_files_list(working_dir)
    # print(files)
    for file in files:
        current_directory = os.getcwd()
        os.chdir(working_dir)
        openedfile = open(file)
        try:
            readfile = openedfile.read()
        except:
            readfile = openedfile.read()
        # print(readfile)
        print("File Name: %s" % file)
        try:
            md5Hash = hashlib.md5(readfile)
        except:
            md5Hash = hashlib.md5(readfile.encode('utf-8'))
        md5Hashed = md5Hash.hexdigest()

        print("MD5: %r" % md5Hashed)
        md5_filename = (file + ".md5")
        f = open(md5_filename, "w+")
        f.write(md5Hashed)
        f.close()
        os.chdir(current_directory)

def create_sha1(working_dir):
    files = get_files_list(working_dir)
    # print(files)
    for file in files:
        current_directory = os.getcwd()
        os.chdir(working_dir)
        openedfile = open(file)
        print("File Name: %s" % file)
        try:
            readfile = openedfile.read()
        except:
            readfile = openedfile.read()

        try:
            sha1Hash = hashlib.sha1(readfile)
        except:
            sha1Hash = hashlib.sha1(readfile.encode('utf-8'))
        sha1Hashed = sha1Hash.hexdigest()

        print("SHA1: %r" % sha1Hashed)
        sha1_filename = (file + ".sha1")
        f = open(sha1_filename, "w+")
        f.write(sha1Hashed)
        f.close()
        os.chdir(current_directory)

def main():
    working_dir = "/tmp/ztp/tftproot"
    create_md5(working_dir)
    create_sha1(working_dir)

if __name__ == '__main__':
    main()
