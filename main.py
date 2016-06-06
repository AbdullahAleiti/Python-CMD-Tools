# -*- coding: UTF-8 -*-

import Time
import os
import Tkinter
import tkMessageBox
import platform
from Tkinter import Entry,Label

dictionary = {1: "clear", 2: "cls", 3: "exit", 4: "rename", 5: "about", 6: "start gui", 8: "history",
              9: "whatsnew", 10: "show date", 11: "show cl", 12: "sqr", 13: "help", 14: "pwd", 15: "clear history",
              16: "pycont",17 : "test",18 : "getx"}
ver = "0.80"
AppVersion = "Aleiti Systems \nversion %s\nLast update on 2016/06/06" % ver
Counter = 0
History = []
platform = platform.system()
new_user = False

def clisetup(toggle):
    userName = raw_input("enter your %sname please : " % toggle)
    userinfo = open("user.txt", "w+")
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
        userinfo = open("user.txt", "r")
        return userinfo.read()
        userinfo.close()

def changelog():
    changelogfile = open("changelog", "r")
    text_to_print = changelogfile.read()
    changelogfile.close()
    return text_to_print


def isitempty():
    if os.path.isfile("user.txt") \
            and os.path.getsize("user.txt"):
        return False
    else:
        return True

userName = get_name(False);

def sqr(number):
    return number * number

def getx():
    bx1 = bx2 = by1 = by2 = False
    
    def printvalue(var,value):
        print "%s = %s" % (var, value)

    def error():
	   print "Error : more than one unknown value." 

    print ("\n******* GetX 1.4 *******")

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

    # the end of input

    if bx1:
        try:
            x = x2*y1/y2
            printvalue(x1,x)
        except TypeError :
            error() 
            return

    if bx2:
        try:
            x = x1*y2/y1 
            printvalue(x2,x)
        except TypeError :
            error()
            return

    if by1:
        try:
            x = x1*y2/x2
            printvalue(y1,x)
        except TypeError:
            error()
            return

    if by2:
        try:
            x = x2*y1/x1
            printvalue(y2,x)
        except TypeError:
            error()
            return

class Gui():
    def __init__(self, name):
        top = Tkinter.Tk()

        def helloCallBack():
            tkMessageBox.showinfo("time", Time.getTime(False))

        B = Tkinter.Button(top, text="show time", bg="gray", command=helloCallBack)
        L = Tkinter.Label(top, text="hi %s" % name , fg = "orange")
        Label(top,text="enter anything :").grid(row=1 ,column=0)
        E = Entry(top)
        L.grid(row=0 ,column=1)
        E.grid(row=1 ,column=1)
        B.grid(row=3 , column=1)
        Text = E.get();
        Label(top,text=Text).grid(row=4 ,column=1)
        top.mainloop()

# main loop
while True:
    if Counter == 0 and not new_user:
        print "welcome back %s" % userName
        Counter += 1
    cli = raw_input("%s@%s : " % (userName, platform))
    if len(cli) > 0:
        History.append(cli)
    if cli == dictionary[3]:
        exit()
    elif cli == dictionary[4]:
        userName = get_name(True)
    elif cli == dictionary[10]:
        Time.getTime(True)
    elif cli == dictionary[6]:
        Gui(userName)
    elif cli == dictionary[1] or cli == dictionary[2]:
        if platform == "Windows":
            os.system('cls')
        elif platform == "Linux":
            os.system("clear")
    elif cli == dictionary[5]:
        print AppVersion
    elif cli == dictionary[8]:
        count = 0
        for i in History:
            print (str(count) + "-" + i)
            count += 1
    elif cli == dictionary[15]:
        del History[:]
    elif cli == dictionary[9] or cli == dictionary[11]:
        print changelog()
    elif cli == dictionary[13]:
        for each_command in dictionary:
            print dictionary[each_command]
    elif cli == dictionary[12]:
        while 1:
            cli = raw_input("%s@%s(sqr): " % (userName, platform))
            try:
                if cli == dictionary[3]:
                    break
                number = float(cli)
                print sqr(number)
            except ValueError:
                print "please enter a valid number"
    elif cli == dictionary[14]:
        print os.getcwd()
    elif cli == dictionary[16]:
        import pycont
        pycont.start()
    elif cli == dictionary[17]:
        import Test
        Test.method(3,5)
    elif cli == dictionary[18]:
        getx()
    elif len(cli) == 0:
        pass
    else:
        print "%s is not recognized as a command " % cli
