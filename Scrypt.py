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
# HASH = "NVZNfGwjZGhJelQ0JFpVejlVMUIK"
HASH = ""
SYSTEM = platform.system()


def main():
    # Options treatment
    parser = optparse.OptionParser()
    parser.add_option("-m", "--method", help="Methods: Encrypt or Decrypt")
    parser.add_option("-f", "--folder", help="Folder to Encrypt or Decrypt")
    parser.add_option("-p", "--password", help="Password to Encrypt or Decrypt files")
    (options, args) = parser.parse_args()

    mode = options.method
    mode.lower()
    folder = options.folder
    IN_PASS = options.password

    IN_PASS_bytes = IN_PASS.encode("ascii")
    IN_PASS_base64_bytes = base64.b64encode(IN_PASS_bytes)
    HASH = IN_PASS_base64_bytes.decode("ascii")

    if SYSTEM.lower() == "windows":
        folders = folder.replace("\\", "\\\\")
        folders_to_encrypt = [f"{folders}"]
    else:
        folders_to_encrypt = [f"{folder}"]

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
