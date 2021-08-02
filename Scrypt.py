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
PROXY = "http://proxy.multicert.inet:8080"
HASH = "NVZNfGwjZGhJelQ0JFpVejlVMUIK"
SYSTEM = platform.system()


def main():
    
    # Select folders to encrypt/decrypt
    if SYSTEM.lower() == "windows":
        folders_to_encrypt = ["C:\\Users\\jchamine\\Downloads"]
    else:
        if SYSTEM.lower() == "linux":
            USER = os.popen("echo $USER | tr -d '\n'").read()
            folders_to_encrypt = [f"/home/{USER}/Downloads"]
        else:
            print("Not linux or windows")

    # Decode Password
    password_encode = HASH.encode('ascii')
    pass_decode = base64.b64decode(password_encode)
    PASS = pass_decode.decode("ascii")

    # Options treatment
    parser = optparse.OptionParser()
    parser.add_option("-m", "--method", help="Methods: Encrypt or Decrypt")
    (options, args) = parser.parse_args()

    mode = options.method
    mode.lower()

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
