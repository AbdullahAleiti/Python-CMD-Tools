# -*- coding: UTF-8 -*-
import Time
import os
import sys
import platform
import re
import subprocess

ver = "0.90.10"
AppVersion = "Python Tools by Aleiti Technologies\nversion %s\nLast update on 2016/07/23" % ver
History = []
platform = platform.system()
new_user = False

#check if the current platform is cygwin
iscygwin = re.search("cygwin",r"{0}".format(platform),flags=re.IGNORECASE)
#change directory to the script location
os.chdir(sys.path[0])

def clisetup(toggle):
    userName = raw_input("enter your %sname please : " % toggle)
    userinfo = open("user", "w+")
    userinfo.truncate()
    userinfo.write(userName)
    userinfo.close()
    return userName

def get_name(toggle):
    global new_user
    if isitempty():
        new_user = True
        return clisetup("")
    elif toggle:
        new_user = True
        return clisetup("new ")
    elif not toggle:
        userinfo = open("user", "r")
        return userinfo.read()
        userinfo.close()

def changelog():
    changelogfile = open("changelog", "r")
    print changelogfile.read()
    changelogfile.close()

def isitempty():
    if os.path.isfile("user") \
            and os.path.getsize("user"):
        return False
    else:
        return True

def getx():
    bx1 = bx2 = by1 = by2 = False
    
    def printvalue(var,value): print "%s = %s" % (var, value)
    def error(): print "Error : more than one unknown value." 

    print ("\n******* GetX 1.4 *******")
    #get input
    x1 = raw_input("for each ")
    if x1.isalpha():
        bx1 = True
    else:
        x1 = float(x1)
    x2 = raw_input("you got ")
    if x2.isalpha():
        bx2 = True
    else:
        x2 = float(x2)
    y1 = raw_input("that means for each ")
    if y1.isalpha():
        by1 = True
    else:
        y1 = float(y1)
    y2 = raw_input("you got ")
    if y2.isalpha():
        by2 = True
    else:
        y2 = float(y2)

    #calculation
    if bx1:
        try:
            x = x2*y1/y2
            printvalue(x1,x)
        except TypeError :
            error() 
            return
    elif bx2:
        try:
            x = x1*y2/y1 
            printvalue(x2,x)
        except TypeError :
            error()
            return
    elif by1:
        try:
            x = x1*y2/x2
            printvalue(y1,x)
        except TypeError:
            error()
            return
    elif by2:
        try:
            x = x2*y1/x1
            printvalue(y2,x)
        except TypeError:
            error()
            return

def percent(arg):
    try:
        if len(arg) != 3:
            print "usage : pc {relative number} {whole number}"
            return
        elif int(arg[2]) == 100:
            print "dude!it's already calculated,but however it's {0}%".format(arg[1])
            return
        solution = (float(arg[1])*100.0) / float(arg[2])
        print solution,"%"
    except ValueError:
        print "please enter valid numbers."

def sigma(number):
    if number == 0:
        return 0
    else:
        return number + sigma(number - 1)

userName = get_name(False);
if not new_user:
    print "welcome back %s" % userName

# main loop
while True:
    cli = raw_input("%s@%s : " % (userName, platform))
    if len(cli) > 0:
        History.append(cli)
    if cli == "exit":
        temp = ["arg_parser.pyc" ,"Time.pyc","gui.pyc" ,"pycont.pyc"]
        for f in temp:
            try:os.remove(f)  
            except:pass
        exit()
    elif cli == 'rename':
        userName = get_name(True)
    elif cli == "date":
        Time.getTime(True)
    elif cli == "gui":
        import gui
        gui.parent(userName)
    elif cli in ('clear','cls'):
        if platform == "Windows":
            os.system('cls')
        elif platform in ["Android","Linux"]:
            os.system('clear')
        elif iscygwin:
            #cygwin has no clear command so i used this bash to do it
            bash = "printf \"\\033c\""
            p = subprocess.Popen(bash , shell=True)
    elif cli == "about":
        print AppVersion
    elif cli == 'history':
        count = 0
        for i in History:
            print (str(count) + "-" + i)
            count += 1
    elif cli == 'clear history':
        del History[:]
    elif cli == 'whatsnew':
        changelog()
    elif cli == "sqr":
        while 1:
            cli = raw_input("%s@%s(sqr): " % (userName, platform))
            try:
                if cli == 'exit':
                    break
                number = float(cli)
                print number*number
            except ValueError:
                print "please enter a valid number"
    elif cli == 'pwd':
        print os.getcwd()
    elif cli == 'pycont':
        import pycont
        pycont.start()
    elif cli == "getx":
        getx()
    elif len(cli) == 0:
        pass
    else:
        args = cli.split()
        arg_length = len(args)
        if args[0] in ["pc","pc "]:
            percent(args)
        elif args[0] == "sg" and arg_length == 2:
            if args[1].isdigit():print sigma(int(args[1]))
            else:print "please enter a valid number."
        else:
            print "%s is not recognized as a command " % cli
