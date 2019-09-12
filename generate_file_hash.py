#!/usr/bin/env python3

# Author - Shane Carnahan
# Email - Shane.Carnahan1@gmail.com
# Date - 9/12/19
# Project - mlh_network_staging
# Version - 1.0

"""
Working on converting this to a class but it's not working just yet....

"""

import hashlib
import os

class Hashes:

    shpfiles = []

    def __init__(self, working_dir='/etc/ztp/tftproot'):
        self.working_dir = working_dir

    def get_files_list(self, working_dir):
        self.current_directory = os.getcwd()
        print("The current directory is: " + self.current_directory)
        os.chdir(working_dir)
        for dirpath, subdirs, files in os.walk(".", topdown=False):
            for file in files:
                if file.endswith('.md5') or file.endswith('.sha1'):
                    continue
                else:
                    self.shpfiles.append(os.path.join(dirpath, file))
        print(self.shpfiles)
        os.chdir(self.current_directory)
        print("The current directory is: " + os.getcwd())
        return self.shpfiles

    def create_md5(self):
        self.shpfiles = self.get_files_list(self.working_dir)
        print(self.shpfiles)
        for file in self.shpfiles:
            current_directory = os.getcwd()
            os.chdir(self.working_dir)
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

    def create_sha1(self, working_dir='/etc/ztp/tftproot'):
        self.working_dir = working_dir
        self.shpfiles = self.get_files_list(self.working_dir)
        print(self.shpfiles)
        for file in self.shpfiles:
            current_directory = os.getcwd()
            os.chdir(working_dir)
            openedfile = open(file)
            try:
                readfile = openedfile.read()
            except:
                readfile = openedfile.read()
            try:
                sha1Hash = hashlib.sha1(readfile)
            except:
                sha1Hash = hashlib.sha1(readfile.encode('utf-8'))
            sha1Hashed = sha1Hash.hexdigest()
            print("File Name: %s" % file)
            # print("MD5: %r" % md5Hashed)
            print("SHA1: %r" % sha1Hashed)
            sha1_filename = (file + ".sha1")
            f = open(sha1_filename, "w+")
            f.write(sha1Hashed)
            f.close()
            os.chdir(current_directory)
