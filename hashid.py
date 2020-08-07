#!/usr/bin/python3

import hashlib
import sys
import optparse
import random
import time
try:
    import keyboard
except ImportError:
    print ("[x] Module 'keyboard' not installed, please install now!")
    sys.exit()
    
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

class Other:
    def __init__(self):
        self.file = sys.argv[0]
        self.color = color()

    def banner(self):
        logo = f"""{self.color.reset}
{self.color.yellow}    _  _          {self.color.reset}HashID [{self.color.green}0.6{self.color.reset}]
{self.color.yellow}  _| || |_ {self.color.reset} Simple tool to crack hash
{self.color.yellow} |_  __  _|
{self.color.yellow}  _| || |_  {self.color.reset} Author : Billal Fauzan
{self.color.yellow} |_  __  _| {self.color.reset} Version: 0.6
{self.color.yellow}   |_||_| {self.color.reset}
        """
        print (logo)

    def help(self):
        print ("""
Welcome to HashID, HashId is a tool to break into a hash.

Usage: hashid.py [options]

Options:
  -h, --help            show this help message and exit
  -t TARGET, --target=TARGET
                        Set target (recommended)
  -r, --random          Use wordlist from random alphabet
  -w WORDLIST, --wordlist=WORDLIST
                        Use wordlist from file (recommended)
  -l, --log             Show log
        """)

    def getTotalWordlist(self, word):
        total = len(word)
        if total == 0:
            # print ("[x] Total wordlist: 0")
            sys.exit()
        else:
            print ("[!] Total wordlist: " + str(total))

class App:
    def __init__(self):
        self.color = color()
        self.file = sys.argv[0]
        self.other = Other()
        self.word = []
        self.log = False
        self.other.banner()
        self.target = None
        self._type = []
        
    def scanType(self):
        if self.target == None:
            print ("[!] WARNING: target required")
            i = input("[?] Need help? (Y/n): ")
            if i.lower() == "y":
                self.other.help()
            sys.exit()
        else:
            length = len(self.target)
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
                print ("[!] ERROR: hash not supported")
                sys.exit()
            
    def getWodlistFromFile(self, file):
        mode = "r"
        while True:
            try:
                o = open(file, mode).read()
                for total, value in zip(range(len(o.splitlines())), o.splitlines()):
                    if self.log == True:
                        print (f"\r[{total}] Read and Append to list...", end="", flush=True)
                    self.word.append(value)
                if self.log == True:
                    print ()
                break
            except IOError:
                print (f"[x] '{file}': No such file or directory")
                sys.exit()
            except UnicodeDecodeError:
                mode = "rb"
                if self.log == True:
                    print ("[x] ERROR: failed to reading, change mode to 'rb'")
        self.other.getTotalWordlist(self.word)

    def randomWordlist(self):
        process = True
        print ("[!] Generate wordlist, press 'q' to stop")
        while process:
            try:
                if keyboard.is_pressed('q'):
                    process = False
                else:
                    word = ""
                    lWord = list("abcdefghijklmnopqrstuvwyz1234567890-=][';/.,`~!@#$%^&*()_+\|")
                    for _ in range(random.randint(1, 10)):
                        if random.randint(0, 1) == 0:
                            word += (random.choice(lWord)).upper()
                        else:
                            word += (random.choice(lWord)).lower()
                    self.word.append(word)
            except ImportError:
                print ("[x] ERROR: permission denied, please use root user.")
                process = False
        self.other.getTotalWordlist(self.word)
        
    def crack(self):
        print ("[*] Cracking...")
        isFound = False
        isTry = False
        start = time.time()
        for tipe in self._type:
            a = 0
            if self.log == True:
                if isTry and self.log:
                    print ()
                print ("[!] Trying for type: " + tipe)
            for word in self.word:
                a += 1
                try:
                    hash = hashlib.new(tipe, word.encode()).hexdigest()
                    if self.target == hash:
                        if self.log:
                            print ()
                        print ("-" * 25 + "Information" + "-" * 25)
                        print ("[!] Found: " + str(word))
                        isTry = False
                        isFound = True
                        end = time.time()
                        totalTime = str(end - start)[0:5]
                        print ("[!] Time: " + totalTime + "s")
                        break
                    if self.log == True:
                        print (f"\r[*] Cracking {a}/{len(self.word)}", end="", flush=True)
                except ValueError:
                    print ("[!] ERROR: failed hashing, skip")
                    break
            if isFound == True:
                break
            else:
                isTry = True
        if isFound != True:
            if self.log == True:
                print ()
            print ("[!] Sorry, your hash not cracked.")
            
    def parseArgument(self):
        parser = optparse.OptionParser()
        parser.add_option("-t", "--target", help="Set target (recommended)", dest="target", action="store")
        parser.add_option("-r", "--random", help="Use wordlist from random alphabet", dest="random", action="store_true")
        parser.add_option("-w", "--wordlist", help="Use wordlist from file (recommended)", dest="wordlist", action="store")
        parser.add_option("-l", "--log", help="Show log", dest="log", action="store_true")
        opt, args = parser.parse_args()

        if opt.wordlist:
            self.getWodlistFromFile(opt.wordlist)
            self.target = opt.target
            self.log = opt.log
            #if self.target != None:
            self.scanType()
            self.crack()
        elif opt.random:
            self.randomWordlist()
            self.target = opt.target
            self.log = opt.log
            #if self.target != None:
            self.scanType()
            self.crack()
        else:
            print ("[!] Please choice wordlist!")
            i = input("[?] Need help? (Y/n): ")
            if i.lower() == "y":
                self.other.help()
                
    def main(self):
        self.parseArgument()

if __name__ == "__main__":
    try:
        app = App()
        app.main()
    except SyntaxError:
        print ("[x] Please use min python3.6!")
        sys.exit()
