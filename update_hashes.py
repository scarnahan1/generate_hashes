#!/usr/bin/env python3

# Author - Shane Carnahan
# Email - Shane.Carnahan1@gmail.com
# Date - 9/12/19
# Project - mlh_network_staging
# Version - 1.0

from generate_file_hash import Hashes
from get_files import get_files_list
from generate_hashes import create_md5
from generate_hashes import create_sha1
import argparse


def main():
    working_dir = arguments.working_dir
    hash_type = arguments.hash_type
    if hash_type == 'md5':
        create_md5(working_dir)
    if hash_type == 'sha1':
        create_sha1(working_dir)
    if hash_type == 'both':
        create_md5(working_dir)
        create_sha1(working_dir)
    else:
        print("No Arguments passed or unrecognized arguments")

# Standard call to the main() function.
if __name__ == '__main__':
    # Start the timer
    # start_time = time.time()
    # Check for missing folders before starting up fully
    # log_location = './LOGS/'
    # folder_check(log_location)
    parser = argparse.ArgumentParser(description="File Hash Update/Create", epilog='Usage: python update_hashes.py -working_dir "/etc/ztp/tftproot" -hash_type "md5"')
    parser.add_argument('-working_dir', default='/etc/ztp/tftproot', help='Location of Files to have hashes created')
    parser.add_argument('-hash_type', default='MD5', help='Hash type to create (MD5, SHA1 or BOTH)')

    arguments = parser.parse_args()

    main()