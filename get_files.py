#!/usr/bin/env python3

# Author - Shane Carnahan
# Email - Shane.Carnahan1@gmail.com
# Date - 9/12/19
# Project - mlh_network_staging
# Version - 1.0

import os

def get_files_list(working_dir):
    shpfiles = []
    current_directory = os.getcwd()
    # print("The current directory is: " + current_directory)
    os.chdir(working_dir)
    for dirpath, subdirs, files in os.walk(".", topdown=False):
        for file in files:
            if file.endswith('.md5') or file.endswith('.sha1'):
                continue
            else:
                shpfiles.append(os.path.join(dirpath, file))
    # print(shpfiles)
    os.chdir(current_directory)
    # print("The current directory is: " + os.getcwd())
    return shpfiles

def main():
    working_dir = "/tmp/ztp/tftproot"
    get_files_list(working_dir)

if __name__ == '__main__':
    main()