#-*-coding:utf-8-*-
from mechanize import Browser
from re import findall
from sys import argv, exit
from os import system

br = Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0')]
br.set_handle_robots(False)

bold = "\033[1m"
underline = "\033[4m"
green = "\033[92m"
blue = "\033[94m"
yellow = "\033[93m"
red = "\033[91m"
endcolor = "\033[0m"

def logo():
    print "--==["+bold+blue+"nickname"+endcolor+"] [ esw0rmer"
    print "--==["+bold+yellow+"MyGitHub"+endcolor+"] [ http://github.com/esw0rmer"
    print "--==["+bold+green+"software"+endcolor+"] [ Code Share"
    print "-"*43

def helpme():
    print "Using:"
    print "\t"+bold+"~$"+endcolor+" python codesh.py "+green+"[filename]"+endcolor
    print "\t\t<< or >>"
    print "\t"+bold+"~$"+endcolor+" python codesh.py "+green+"[filename] [language]"+endcolor
    print "\t\t<< or >>"
    print "\t"+bold+"~$"+endcolor+" python codesh.py "+green+"[filename] [language] [nickname]"+endcolor
    print "\t\t<< example >>"
    print "\t"+bold+"~$"+endcolor+" python codesh.py "+green+"myFirstProject.pl"+endcolor+" "+yellow+"perl"+endcolor+" "+blue+"esw0rmer"+endcolor
    print "\t"+bold+"~$"+endcolor+" python codesh.py "+green+"myFirstText.txt"+endcolor+" "+yellow+"text"+endcolor+" "+blue+"esw0rmer"+endcolor
    print ""

def ps_pasteubuntu(filename, language, nickname):
    languages = {"python": "python", "perl": "perl", "c": "c", "c#": "csharp", "c++": "cpp", "html": "html", "javascript": "js", "php": "php", "ruby": "ruby"}
    if language in languages:
        lang = languages[language]
    else:
        lang = "text"
    try:
        codes = open(filename, "r").read()
    except:
        print bold+red+"[-] File not found"+endcolor
        exit(1)
    br.open("http://paste.ubuntu.com")
    br.select_form("pasteform")
    br['poster'] = nickname
    br['content'] = codes
    br.find_control(name="syntax").value = [lang]
    source = br.submit().read()
    results = findall('<a class="pturl" href="/(.*?)/plain/">Download as text</a>',source)
    print bold+yellow+"PasteUbuntu:\t"+endcolor+" http://paste.ubuntu.com/"+str(results[0])

def ps_paste2(filename, language, nickname):
    languages = {"python": "python", "perl": "perl", "c": "c", "c#": "csharp", "c++": "cpp", "html": "html", "javascript": "js", "php": "php", "ruby": "rb"}
    if language in languages:
        lang = languages[language]
    else:
        lang = "text"
    try:
        codes = open(filename, "r").read()
    except:
        print bold+red+"[-] File not found"+endcolor
        exit(1)
    br.open("http://paste2.org")
    br.select_form(nr=0)
    br['code'] = codes
    br.find_control(name="lang").value = [lang]
    br["description"] = "Copy: Code Share | GitHub: http://github.com/esw0rmer"
    source = br.submit().read()
    results = findall('<a href="(.*?)/followup" title="Followup Paste">', source)
    print bold+yellow+"Paste2:\t\t "+endcolor+str(results[0])

def ps_blogtrog(filename, language, nickname):
    languages = {"python": "Python", "perl": "Perl", "c#": "C#", "html": "HTML", "javascript": "JScript", "php": "PHP"}
    if language in languages:
        lang = languages[language]
    else:
        lang = "BatchFile"
    try:
        codes = open(filename, "r").read()
    except:
        print bold+red+"[-] File not found"+endcolor
        exit(1)
    br.open("http://www.blogtrog.com")
    br.select_form(nr=0)
    br.find_control(name="ctl00$ContentPlaceHolder1$LanguageDropDownList").value = [lang]
    br["ctl00$ContentPlaceHolder1$CodeTextBox"] = codes
    source = br.submit().read()
    results = findall('value="iframe(.*?)" />', source)
    print bold+yellow+"BlogTrog:\t "+endcolor+"http://www.blogtrog.com/code.aspx?id="+str(results[0])

logo()
if len(argv) <= 1 or argv[1] == "help":
    helpme()
    exit(1)
elif len(argv) == 2:
    print bold+blue+"[+] Copy Begins"+endcolor+"\n"
    filename, language, nickname = argv[1], "text", "CodeShare"
    ps_pasteubuntu(filename, language, nickname)
    ps_paste2(filename, language, nickname)
    ps_blogtrog(filename, language, nickname)
elif len(argv) == 3:
    print bold+blue+"[+] Copy Begins"+endcolor+"\n"
    filename, language, nickname = argv[1], argv[2], "CodeShare"
    ps_pasteubuntu(filename, language, nickname)
    ps_paste2(filename, language, nickname)
    ps_blogtrog(filename, language, nickname)
elif len(argv) == 4:
    print bold+blue+"[+] Copy Begins"+endcolor+"\n"
    filename, language, nickname = argv[1], argv[2], argv[3]
    ps_pasteubuntu(filename, language, nickname)
    ps_paste2(filename, language, nickname)
    ps_blogtrog(filename, language, nickname)
else:
    helpme()
    exit(1)



# codesh.py mytext.txt
# ccodesh.py mytext.txt text
# codesh.py mytext.txt text esw0rmer
