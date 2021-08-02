#! /usr/bin/env python3
# coding=utf-8

#########################
# Author: João Chaminé  #
#########################

# imports
import os
import optparse
import base64
import platform
from res.cryptography import Encryption

# Vars
HASH = "NVZNfGwjZGhJelQ0JFpVejlVMUIK"
SYSTEM = platform.system()


def main():
    # Options treatment
    parser = optparse.OptionParser()
    parser.add_option("-m", "--method", help="Methods: Encrypt or Decrypt")
    parser.add_option("-f", "--folder", help="Folder to Encrypt or Decrypt")
    (options, args) = parser.parse_args()

    mode = options.method
    mode.lower()
    folder = options.folder
    folders_to_encrypt = folder.replace("\\", "\\\\")

    # Decode Password
    password_encode = HASH.encode('ascii')
    pass_decode = base64.b64decode(password_encode)
    PASS = pass_decode.decode("ascii")

    if mode == "encrypt":
        crypt = Encryption(folders_to_encrypt, PASS, SYSTEM)
        crypt.crypt()
    else:
        if mode == "decrypt":
            decrypt = Encryption(folders_to_encrypt, PASS, SYSTEM)
            decrypt.decrypt()
        else:
            print("Wrong Choice!!!")

if __name__ == "__main__":
    main()
