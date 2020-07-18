import random
import optparse
import sys
import hashlib
import os
import keyboard
try:
    from tkinter import *
    guiSupport = True
except ImportError:
    guiSupport = False

class color:
    def __init__(self):
        super().__init__()
        self.plat = sys.platform

    @property
    def red(self):
        if self.plat == "linux":
            return "\033[31;1m"
        else:
            return ""

    @property
    def green(self):
        if self.plat == "linux":
            return "\033[32;1m"    
        else:
            return ""

    @property
    def yellow(self):
        if self.plat == "linux":
            return "\033[33;1m"
        else:
            return ""

    @property
    def blue(self):
        if self.plat == "linux":
            return "\033[34;1m"
        else:
            return ""

    @property
    def white(self):
        if self.plat == "linux":
            return "\033[37;1m"
        else:
            return ""

    @property
    def reset(self):
        if self.plat == "linux":
            return "\033[0m"
        else:
            return ""

class Gui:
    def __init__(self):
        self.tk = Tk()

    def drawMaterial(self):
        self.tk.title("HashID GUI version")
        self.tk.geometry("600x600")
        self.tk["bg"] = "black"

        self.box = Entry(self.tk)
        self.box.pack()

    def main(self):
        self.drawMaterial()
        self.tk.mainloop()

class App:
    def __init__(self):
        super().__init__()
        self.__randomWord = False
        self._word = []
        self._target = ""
        self._type = []
        self.showBanner()

    def showBanner(self):
        logo = """
    _  _          HashID [0.5]
  _| || |_  Simple tool to crack hash
 |_  __  _|
  _| || |_   Author : Billal Fauzan
 |_  __  _|  Version: 0.5
   |_||_|  """
        print (logo)

    def generateWordlist(self):
        print ("\r[!] Generate wordlist, press 'q' to stop! ")
        while True:
            try:
                wl = list("abcedfghijklmnoqrstuvwxyz1234567890-=\';/.,!@#$%^&*()_+")
                wr = ""
                for _ in range(random.randint(0, 10)):
                    if random.randint(0, 1) == 1:
                        wr += random.choice(wl).upper()
                    else:
                        wr += random.choice(wl).lower()
                self._word.append(wr)
            except KeyboardInterrupt:
                continue
            if keyboard.is_pressed('q'):
                break

    def getWordlist(self, path):
        try:
            o = open(path, "r").read()
            self._word = o.splitlines()
        except IOError:
            print (f"[!] Path '{path}' not found'")
            
    def _getTotalWordlist(self):
        print (f"[!] Total word: {len(self._word)}")

    def _helpMe(self):
        print ("""
Welcome to HashID ~Simple hash cracker~ 

{1.4} HashID is a tool that works to crack hashes, such as: md5, sha1, sha512, etc.
This tool support python 3.x

Commands                   Description
----------                -------------
  -t, --target [hash]      Set target hash
  -w, --wordlist [path]    Set wordlist from files
  -r, --random             Random wordlists
  -g, --gui                Use GUI version
        
Copyright (c) Billal Fauzan. All right reversed""")

    def checkHash(self):
        length = len(self._target)
        if length == 32:
            self._type.append("md4")
            self._type.append("md5")
        elif length == 40:
            self._type.append("ripemd160")
            self._type.append("sha1")
        elif length == 56:
            self._type.append("sha3_224")
            self._type.append("sha224")
        elif length == 64:
            self._type.append("blake2s256")
            self._type.append("sha256")
            self._type.append("blake2s")
        elif length == 72:
            self._type.append("md5-sha1")
        elif length == 96:
            self._type.append("sha384")
        elif length == 128:
            self._type.append("sha3_512")
            self._type.append("blake2b512")
            self._type.append("SHA512")
            self._type.append("blake2b")
            self._type.append("whirlpool")
        else:
            print ("[!] Hash not supported")
            sys.exit()

    def hash(self, type, word):
        hashing = hashlib.new(type, word)
        return hashing.hexdigest()

    def crack(self):
        self.isFound = False
        if self._target == "":
            print ("[!] The target has been set, please set it first!")
            sys.exit()
        else:
            if len(self._word) == 0:
                print ("[!] Wordlist null, please insert wordlist!")
            else:
                self.checkHash()
                for type in self._type:
                    i = 0
                    print (f"[x] Trying for hash: {type}")
                    for word in self._word:
                        result = self.hash(type, word.encode())
                        i += 1                    
                        if self._target == result:
                            print ("\n[+] Found: " + word)
                            self.isFound = True
                            break
                        print (f"\r[!] Trying: {i}, Word: {word}", end="", flush=True)
                    if self.isFound == True: break
                    else: print ()

    def main(self):
        global guiSupport
        parser = optparse.OptionParser()
        parser.add_option("-r", "--random", action="store_true", dest="isRandom", help="Random wordlist")
        parser.add_option("-w", "--wordlist", action="store", dest="wordlist", help="Set Wordlist")
        parser.add_option("-t", "--target", action="store", dest="target", help="Set target")
        parser.add_option("-g", "--gui", action="store_true", dest="isGUi", help="Gui Version")
        opt, args = parser.parse_args()
        if opt.target:
            try:
                self._target = opt.target
            except IndexError:
                print ("[!] Type: --help to show all commands")
                sys.exit()

        if opt.isGUi:
            if guiSupport == True:
                main_window = Gui()
                main_window.main()
                sys.exit()
            else:
                print ("[x] GUI not supported")
                sys.exit()
        if opt.isRandom:
            self.__randomWord = True

        elif opt.wordlist:
            if self.__randomWord == True:
                choice = input("[!] You are choice random wordlist, continue? (Y/n): ")
                if choice.lower() != "y":
                    sys.exit()
            
            try:
                self.getWordlist(opt.wordlist)
            except IndexError:
                print ("[!] Type: --help to show all commands")
                sys.exit()
        else:
            self._helpMe()
            sys.exit()

        if self.__randomWord == True:
            self.generateWordlist()
        
        self._getTotalWordlist()
        self.crack()

if __name__ == "__main__":
    main = App()
    main.main()