# coding=utf-8

#########################
# Author: João Chaminé  #
#########################
# imports
import glob
import os
import pyAesCrypt
from res.teams import Teams


class Encryption:
    def __init__(self, folders_to_encrypt, PASS, SYSTEM):
        self.folders_to_encrypt = folders_to_encrypt
        self.PASS = PASS
        self.SYSTEM = SYSTEM

    def crypt(self):
        for folder in self.folders_to_encrypt:
            if self.SYSTEM.lower() == "windows":
                for item in glob.glob(f'{folder}\\**\\*', recursive=True):
                    if os.path.isfile(item):
                        file_encrypt = item + ".encrypted"
                        pyAesCrypt.encryptFile(infile=item, outfile=file_encrypt, passw=self.PASS)
                        os.remove(item)
            else:
                for item in glob.glob(f'{folder}/**/*', recursive=True):
                    if os.path.isfile(item):
                        file_encrypt = item + ".encrypted"
                        pyAesCrypt.encryptFile(infile=item, outfile=file_encrypt, passw=self.PASS)
                        os.remove(item)
            msg_teams = Teams(text=f"Files of the folder {folder} were encrypted!!!", title=f"{folder} Encrypted")
            msg_teams.send_teams_message()

    def decrypt(self):
        for folder in self.folders_to_encrypt:
            if self.SYSTEM.lower() == "windows":
                for item in glob.glob(f'{folder}\\**\\*', recursive=True):
                    if os.path.isfile(item):
                        file = item.replace(".encrypted", "")
                        pyAesCrypt.encryptFile(infile=item, outfile=file, passw=self.PASS)
                        os.remove(item)
            else:
                for item in glob.glob(f'{folder}/**/*', recursive=True):
                    if os.path.isfile(item):
                        file = item.replace(".encrypted", "")
                        pyAesCrypt.encryptFile(infile=item, outfile=file, passw=self.PASS)
                        os.remove(item)
            msg_teams = Teams(text=f"Files of the folder {folder} were decrypted!!!", title=f"{folder} Decrypted")
            msg_teams.send_teams_message()