from tkinter import *
import tkinter
from tkinter import ttk, scrolledtext, filedialog, messagebox, Scrollbar
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import webbrowser
import time,sys
from time import sleep
from subprocess import Popen
from math import *
from datetime import datetime
import urllib
import urllib.request
import re
import socket
import subprocess
import random
import os

def make_menu(ccp):
    global the_menu
    the_menu = tkinter.Menu(ccp, tearoff=0)
    the_menu.add_command(label="Cut")
    the_menu.add_command(label="Copy")
    the_menu.add_command(label="Paste")

def show_menu(sm):
    ccp = sm.widget
    the_menu.entryconfigure("Cut", command=lambda: ccp.event_generate("<<Cut>>"))
    the_menu.entryconfigure("Copy", command=lambda: ccp.event_generate("<<Copy>>"))
    the_menu.entryconfigure("Paste", command=lambda: ccp.event_generate("<<Paste>>"))
    the_menu.tk.call("tk_popup", the_menu, sm.x_root, sm.y_root)

root = tk.Tk()
menu = tkinter.Menu(root)
root.config(menu=menu)
make_menu(root)

root.title('TIDE - Terminal Insanity Desktop Environment')
w = 1600
h = 775
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 1) - (w / 0.9)
y = (hs / 1) - (h / 0.8)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(0, 0)
root.option_add("*Label.Font", "helvetica 9")
#root.overrideredirect(0)

#Program Main Framework

mf = ttk.Notebook(root)
mf.grid(row=1, column=1, sticky='NESW')
mf1 = ttk.Frame(mf)
mf.add(mf1, text=' TIDE HOME ')
mf2 = ttk.Frame(mf)
mf.add(mf2, text=' NETWORK TOOLS ')
mf4 = ttk.Frame(mf)
mf.add(mf4, text=' WIFI MONITOR FULLSCREEN ')
mf6 = ttk.Frame(mf)
mf.add(mf6, text=' NETWORK MAPPING ')
mf8 = ttk.Frame(mf)
mf.add(mf8, text=' WIFI HOTSPOT ')
mf9 = ttk.Frame(mf)
mf.add(mf9, text=' MITM ')
mf3 = ttk.Frame(mf)
mf.add(mf3, text=' INTERNET TOOLS ')
mf5 = ttk.Frame(mf)
mf.add(mf5, text=' HASHING TOOLS ')
mf10 = ttk.Frame(mf)
mf.add(mf10, text=' SQL TOOLS ')
mf11 = ttk.Frame(mf)
mf.add(mf11, text=' EXPLOIT FRAMEWORK ')



#Network mapping tab
label1 = Label(mf6, text='\nThis feature is currently in development and not operational\n', fg='red', font='100')
label1.grid(row=0, column=0)
#Wifi Hotspot tab
label1 = Label(mf8, text='\nThis feature is currently in development and not fully operational\n', fg='red', font='100')
label1.grid(row=0, column=0)
#MITM tab
label1 = Label(mf9, text='\nThis feature is currently in development and not operational\n', fg='red', font='100')
label1.grid(row=0, column=0)
#SQL Tools tab
label1 = Label(mf10, text='\nThis feature is currently in development and not operational\n', fg='red', font='100')
label1.grid(row=0, column=0)
#Hashing Tools tab
label1 = Label(mf5, text='\nThis feature is currently in development and not operational\n', fg='red', font='100')
label1.grid(row=0, column=0)
#Exploit Framework tab
label1 = Label(mf11, text='\nThis feature is currently in development and not operational\n', fg='red', font='100')
label1.grid(row=0, column=0)

#Tide home tab
tide = Frame(mf1)
tide.pack()

tide1 = Label(tide, text="\n\n\n")
tide1.pack()
tide1 = Label(tide, text="TIDE v1.0\n\nTerminal Insanity Desktop Environment\n", fg='blue', font='100')
tide1.pack()
tide1 = Label(tide, text="\nXterm is required to use TIDE, Please install Xterm if you do not have it.\nsudo apt-get update\nsudo apt-get -y install xterm\n", fg='red')
tide1.pack()
tide1 = Label(tide, text="The correct resolution for TIDE is 1600 x 900 or greater\nPlease make sure to input information where required\n", fg='red')
tide1.pack()
tide1 = Label(tide, text="TIDE is still in the development phase and best run 'sudo'.\nPlease remember to place mouse cursor over a terminal to input.\n", fg='red')
tide1.pack()
tide1 = Label(tide, text="Welcome to TIDE. Please use the Tabs to navigate to different Terminals\n", font='100')
tide1.pack()
tide1 = Label(tide, text="TIDE is a GUI created to better manage terminals and tasks in Kali Linux\n", font='100')
tide1.pack()
tide1 = Label(tide, text="\nCompiled and created by Elle Eeddee and Cle Ju", fg='blue')
tide1.pack()
tide1 = Label(tide, text="\n\n\nTIDE has no affiliation and/or endorsement to any of the applications/programs used within it's code, but wishes to thank the creators of these applications/programs for their dedication in their creations.")
tide1.pack()
tide1 = Label(tide, text="\nFurther gratitude is given to all persons, forms, tutorials, QnA and the like that exist in assisting the creation of TIDE.")
tide1.pack()
tide1 = Label(tide, text="\n\n\nTIDE has no persistent features and has been written for use with Kali Linux and Xterm. If an application/program is required for use of some of the functions")
tide1.pack()
tide1 = Label(tide, text="\na button to download that requirement is provided.")
tide1.pack()
tide1 = Label(tide, text="\n\n\nThe applications/programs leveraged by TIDE each have their own Usage Warnings and/or Disclaimers. The creator of TIDE does not condone the usage of these applications/programs")
tide1.pack()
tide1 = Label(tide, text="\nfor illegal activities and/or usage without prior consent. TIDE was created for educational purposes and is distributed under a GNU GPLv3 or any later version, which entitles the running, studying, sharing, and modifying of TIDE.")
tide1.pack()


# Wifi Monitor Fullscreen Framework
wifi = Frame(mf4)
wifi.grid(row=0, column=0)

wifim = Frame(wifi, height=775, width=1600)
wifim.pack()
wifimm = wifim.winfo_id()

#Network Tools Framework
#Main Screen
topmain = Frame(mf2)
topmain.grid(row=0, column=0)

#Left Framework
topmainl = Frame(topmain)
topmainl.grid(row=1, column=0, sticky='NESW')

termt = Frame(topmainl, height=180, width=1350)
termt.grid(row=1, column=0, sticky='NESW')
tert = termt.winfo_id()

termtb = Frame(topmainl, height=500, width=1350)
termtb.grid(row=2, column=0, sticky='NESW')
tertb = termtb.winfo_id()

#Bottom Tabs Framework
bt = ttk.Notebook(termtb)
bt.grid(row=1, column=0, sticky='NESW')
bt2 = ttk.Frame(bt)
bt.add(bt2, text=' Terminal ')
bt6 = ttk.Frame(bt)
bt.add(bt6, text=' Mac Address Changer ')
bt7 = ttk.Frame(bt)
bt.add(bt7, text=' Stop / Start Monitor Mode ')
bt9 = ttk.Frame(bt)
bt.add(bt9, text=' Wifi Monitor ')
bt10 = ttk.Frame(bt)
bt.add(bt10, text=' Deauthentication ')
bt11 = ttk.Frame(bt)
bt.add(bt11, text=' Ping ')
bt12 = ttk.Frame(bt)
bt.add(bt12, text=' Nmap Scans ')

#Terminal tab
bt22 = Frame(bt2, height=500, width=1350)
bt22.grid(row=1, column=0, sticky='NESW')
bt222 = bt22.winfo_id()

bt22ff = Frame(bt22, height=500, width=1070)
bt22ff.grid(row=1, column=1, sticky='NESW')
bt202ff = bt22ff.winfo_id()

bt22f = Frame(bt22, height=500, width=200)
bt22f.grid(row=1, column=2, sticky='NESW')
bt202f = bt22f.winfo_id()

#Mac Changer tab
bt66 = Frame(bt6, height=500, width=1350)
bt66.grid(row=1, column=0, sticky='NESW')
bt666 = bt66.winfo_id()

bt66ff = Frame(bt66, height=500, width=1070)
bt66ff.grid(row=1, column=1, sticky='NESW')
bt606ff = bt66ff.winfo_id()

bt66f = Frame(bt66, height=500, width=200)
bt66f.grid(row=1, column=2, sticky='NESW')
bt606f = bt66f.winfo_id()

#Airmon-ng tab
bt77 = Frame(bt7, height=500, width=1350)
bt77.grid(row=1, column=0, sticky='NESW')
bt777 = bt77.winfo_id()

bt77ff = Frame(bt77, height=500, width=1070)
bt77ff.grid(row=1, column=1, sticky='NESW')
bt707ff = bt77ff.winfo_id()

bt77f = Frame(bt77, height=500, width=200)
bt77f.grid(row=1, column=2, sticky='NESW')
bt707f = bt77f.winfo_id()

#Airodump-ng tab
bt99 = Frame(bt9, height=500, width=1350)
bt99.grid(row=1, column=0, sticky='NESW')
bt999 = bt99.winfo_id()

bt99ff = Frame(bt99, height=500, width=1070)
bt99ff.grid(row=1, column=1, sticky='NESW')
bt909ff = bt99ff.winfo_id()

bt99f = Frame(bt99, height=500, width=200)
bt99f.grid(row=1, column=2, sticky='NESW')
bt909f = bt99f.winfo_id()

#Deauth tab
bta10 = Frame(bt10, height=500, width=1350)
bta10.grid(row=1, column=0, sticky='NESW')
bta101 = bta10.winfo_id()

bta10ff = Frame(bta10, height=500, width=1070)
bta10ff.grid(row=1, column=1, sticky='NESW')
bta101ff = bta10ff.winfo_id()

bta10f = Frame(bta10, height=500, width=200)
bta10f.grid(row=1, column=2, sticky='NESW')
bta101f = bta10f.winfo_id()

#Ping tab
bta11 = Frame(bt11, height=500, width=1350)
bta11.grid(row=1, column=0, sticky='NESW')
bta111 = bta11.winfo_id()

#Nmap Scanstab
bta12 = Frame(bt12, height=500, width=1350)
bta12.grid(row=1, column=0, sticky='NESW')
bta121 = bta12.winfo_id()


#Right Framework
nb = ttk.Notebook(topmain)
nb.grid(row=1, column=2, sticky='NESW')
tab2 = ttk.Frame(nb)
nb.add(tab2, text='Main Tools')
tab3 = ttk.Frame(nb)
nb.add(tab3, text='Information Gathering')

#Network Tools - Notepad

label0 = Label(termt, text="NOTES")
label0.grid(row=1, column=0)

def save_command():
    file = filedialog.asksaveasfile(parent=root, mode='w', title='Save File', defaultextension=".txt")
    if file is not None:
        data = textPad.get('1.0', END)
        file.write(data)
        file.close()

note1 = Frame(termt)
note1.grid(row=2, column=0)
textPad = ScrolledText(note1, width=165, height=10)
textPad.grid()
textPad.bind()
textPad.bind_class("ScrolledText", "<Button-3><ButtonRelease-3>", show_menu)  # Not working
note2 = Frame(termt)
note2.grid(row=3, column=0)
save1 = Button(note2, text="Save", command=save_command)
save1.config(width=20)
save1.grid()

#Network Tools - Buttons and Functions

#Interface Name

topint = Frame(tab2)
topint.grid(row=120, column=0)

label1 = Label(topint, text='\nPlease Enter Interface Name Below', fg='red')
label1.grid(row=1, column=0)
label1 = Label(topint, text='Features Will Not Work If No Input\n\nPlease Remember To Update\nInterface Name During Work Flow\n', fg='red')
label1.grid(row=3, column=0)
entryint = tk.Entry(topint, width=20)
entryint.grid(row=2, column=0)
entryint.bind()
entryint.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
os.environ['int'] = entryint.get()

def buttonclickqqq():
	os.environ['int'] = entryint.get()
	os.popen('xterm -hold -e sudo airmon-ng check kill')
	sleep(5)
	os.popen('xterm -hold -e sudo airmon-ng start "$int"')
	sleep(5)
	os.popen('xterm -hold -e sudo kismet -c "$int"')
	sleep(5)
	webbrowser.open('http://localhost:2501')
        
button1 = tk.Button(topint, text='DO IT QUICK', command=lambda: buttonclickqqq(), width=10, height=1, bg='Black', fg='white')
button1.grid(row=8, column=0, sticky=NSEW)
button1.bind()

label1 = Label(topint, text='\nDO IT QUICK will start the interface\nabove in monitoring mode\nand launch Kismet with gui.\n', fg='blue')
label1.grid(row=9, column=0)
label1 = Label(topint, text='DO IT QUICK only works if\nyour interface does not\nchange name\n', fg='blue')
label1.grid(row=10, column=0)
label1 = Label(topint, text='DO IT QUICK command list:-\nairmon-ng check kill\nairmon-ng start <interface>\nkismet -c <interface>\nopen browser localhost:2501', fg='blue')
label1.grid(row=11, column=0)

#Terminal tab

top1 = Frame(bt22f)
top1.grid(row=20, column=0)

label1 = Label(bt22f, text='\nCLICK TERMINAL TO START\n', fg='blue')
label1.grid(row=1, column=0)

def buttonclick1():
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10' % bt202ff)
            
button1 = tk.Button(bt22f, text='Terminal', command=lambda: buttonclick1(), width=25, height=1)
button1.grid(row=4, column=0, sticky=W)
button1.bind()

def buttonclick5():
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e ifconfig' % bt202ff)
    
button1 = tk.Button(bt22f, text='Ifconfig', command=lambda: buttonclick5(), width=25, height=1)
button1.grid(row=7, column=0, sticky=W)
button1.bind()

def buttonclick7():
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e iwconfig' % bt202ff)
    
button1 = tk.Button(bt22f, text='Iwconfig', command=lambda: buttonclick7(), width=25, height=1)
button1.grid(row=9, column=0, sticky=W)
button1.bind()

def buttonclicka30():
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo service NetworkManager stop' % bt202ff)

button1 = tk.Button(bt22f, text='Network Manager Stop', command=lambda: buttonclicka30(), width=25, height=1)
button1.grid(row=11, column=0, sticky=W)
button1.bind()

def buttonclicka31():
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo service NetworkManager start' % bt202ff)

button1 = tk.Button(bt22f, text='Network Manager Start', command=lambda: buttonclicka31(), width=25, height=1)
button1.grid(row=13, column=0, sticky=W)
button1.bind()

def buttonclicka32():
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo service NetworkManager restart' % bt202ff)

button1 = tk.Button(bt22f, text='Network Manager Restart', command=lambda: buttonclicka32(), width=25, height=1)
button1.grid(row=15, column=0, sticky=W)
button1.bind()

# Mac Changer tab

label1 = Label(bt66f, text='\nMacChanger Tools\n', fg='blue')
label1.grid(row=1, column=0)

def buttonclick9():
	os.environ['int'] = entryint.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo ifconfig "$int" down' % bt606ff)		

button1 = tk.Button(bt66f, text='Ifconfig Down', command=lambda: buttonclick9(), width=25, height=1)
button1.grid(row=3, column=0, sticky=W)
button1.bind()

label1 = Label(bt66f, text='')
label1.grid(row=4, column=0)

topa1 = Frame(bt66f)
topa1.grid(row=5, column=0)

entry21set = tk.Entry(topa1, width=22)
entry21set.grid(row=3, column=0, sticky=W)
entry21set.bind()
entry21set.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

topb1 = Frame(bt66f)
topb1.grid(row=7, column=0)

def buttonclick11set():
	os.environ['int'] = entryint.get()
	os.environ['e21aset'] = entry21set.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo macchanger -m "$e21aset" "$int"' % bt606ff)	

button1 = tk.Button(topb1, text='Set the above Mac Address', command=lambda: buttonclick11set(), width=25, height=1)
button1.grid(row=4, column=0, sticky=W)
button1.bind()

label1 = Label(topb1, text='')
label1.grid(row=5, column=0)

def buttonclick11():
	os.environ['int'] = entryint.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo macchanger -r "$int"' % bt606ff)

button1 = tk.Button(topb1, text='Random Mac Address', command=lambda: buttonclick11(), width=25, height=1)
button1.grid(row=9, column=0, sticky=W)
button1.bind()

label1 = Label(bt66f, text='')
label1.grid(row=14, column=0)

def buttonclick13():
	os.environ['int'] = entryint.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo ifconfig "$int" up' % bt606ff)		

button1 = tk.Button(bt66f, text='Ifconfig Up', command=lambda: buttonclick13(), width=25, height=1)
button1.grid(row=15, column=0, sticky=W)
button1.bind()

#Airmon-ng tab

label1 = Label(bt77f, text='\nAirmon-ng Tools\n', fg='blue')
label1.grid(row=2, column=0)

def buttonclick15():
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo airmon-ng check kill' % bt707ff)

button1 = tk.Button(bt77f, text='Airmon-ng Check Kill', command=lambda: buttonclick15(), width=25, height=1)
button1.grid(row=4, column=0, sticky=W)
button1.bind()

label1 = Label(bt77f, text='')
label1.grid(row=5, column=0)

def buttonclick17():
	os.environ['int'] = entryint.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo airmon-ng start "$int"' % bt707ff)
    
button1 = tk.Button(bt77f, text='Start Wireless Monitor', command=lambda: buttonclick17(), width=25, height=1)
button1.grid(row=8, column=0, sticky=W)
button1.bind()

label1 = Label(bt77f, text='')
label1.grid(row=9, column=0)

def buttonclick30():
	os.environ['int'] = entryint.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo airmon-ng stop "$int"' % bt707ff)

button1 = tk.Button(bt77f, text='Stop Wireless Monitor', command=lambda: buttonclick30(), width=25, height=1)
button1.grid(row=10, column=0, sticky=W)
button1.bind()

#Airodump-ng tab

label1 = Label(bt99f, text='\nAirodump-ng Tools\n', fg='blue')
label1.grid(row=1, column=0)

i1 = IntVar()
r11 = tk.Radiobutton(bt99f, text="Display in Current Tab", variable=i1, value=1)
r11.grid(row=2, column=0, sticky=W)
r11.invoke()
r11 = tk.Radiobutton(bt99f, text="Display in Fullscreen Tab", variable=i1, value=2)
r11.grid(row=3, column=0, sticky=W)

label1 = Label(bt99f, text='')
label1.grid(row=4, column=0)

i = IntVar()
r1 = tk.Radiobutton(bt99f, text="Filter Unassociated Clients", variable=i, value=1)
r1.grid(row=5, column=0, sticky=W)
r1.invoke()
r1 = tk.Radiobutton(bt99f, text="Don't Filter Unassociated Clients", variable=i, value=2)
r1.grid(row=6, column=0, sticky=W)
label1 = Label(bt99f, text='')
label1.grid(row=7, column=0)

def buttonclick19():
	os.environ['int'] = entryint.get()
	if (i.get() ==1) & (i1.get() ==2):
		os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -hold -e sudo airodump-ng "$int" -a --manufacturer --uptime --wps' % wifimm)
	elif (i.get() ==1) & (i1.get() ==1):
		os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 9 -hold -e sudo airodump-ng "$int" -a --manufacturer --uptime --wps' % bt909ff)	
	elif (i.get() ==2) & (i1.get() ==2):
		os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -hold -e sudo airodump-ng "$int" --manufacturer --uptime --wps' % wifimm)
	elif (i.get() ==2) & (i1.get() ==1):
		os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 9 -hold -e sudo airodump-ng "$int" --manufacturer --uptime --wps' % bt909ff)
	    
button1 = tk.Button(bt99f, text='Monitor All Channels (no save)', command=lambda: buttonclick19(), width=25, height=1)
button1.grid(row=9, column=0, sticky=W)
button1.bind()

label1 = Label(bt99f, text='')
label1.grid(row=10, column=0)

topc11 = Frame(bt99f)
topc11.grid(row=11, column=0, sticky=W)

labelc21 = Label(topc11, text='File name:       ')
labelc21.grid(row=1, column=0, sticky=W)
entryc21 = tk.Entry(topc11, width=15)
entryc21.grid(row=1, column=1, sticky=W)
entryc21.bind()
entryc21.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

def buttonclickc19sa():
	os.environ['fn1'] = entryc21.get()
	os.environ['int'] = entryint.get()
	if (i.get() ==1) & (i1.get() ==2):
		os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 9 -hold -e sudo airodump-ng -w "$fn1" "$int" -a --manufacturer --uptime --wps' % wifimm)
	elif (i.get() ==1) & (i1.get() ==1):
		os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 9 -hold -e sudo airodump-ng -w "$fn1" "$int" -a --manufacturer --uptime --wps' % bt909ff)	
	elif (i.get() ==2) & (i1.get() ==2):
		os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 9 -hold -e sudo airodump-ng -w "$fn1" "$int" -a --manufacturer --uptime --wps' % wifimm)
	elif (i.get() ==2) & (i1.get() ==1):
		os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 9 -hold -e sudo airodump-ng -w "$fn1" "$int" -a --manufacturer --uptime --wps' % bt909ff)

button1 = tk.Button(bt99f, text='Monitor All Channels (save)', command=lambda: buttonclickc19sa(), width=25, height=1)
button1.grid(row=13, column=0, sticky=W)
button1.bind()

label1 = Label(bt99f, text='')
label1.grid(row=17, column=0)

top111 = Frame(bt99f)
top111.grid(row=18, column=0, sticky=W)

entry235 = tk.Entry(top111, width=13)
entry235.grid(row=21, column=1, sticky=W)
entry235.bind()
entry235.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

def buttonclick277():
	os.environ['int'] = entryint.get()
	os.environ['e235'] = entry235.get()
	if (i1.get() ==2):
		os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 9 -hold -e sudo airodump-ng --channel "$e235" -w channel"$e235" "$int" --manufacturer --uptime --wps' % wifimm)
	elif (i1.get() ==1):
		os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 9 -hold -e sudo airodump-ng --channel "$e235" -w channel"$e235" "$int" --manufacturer --uptime --wps' % bt909ff)	
	
button1 = tk.Button(top111, text='Monitor Channel', command=lambda: buttonclick277(), width=11, height=1)
button1.grid(row=21, column=0, sticky=W)
button1.bind()

entry2355 = tk.Entry(top111, width=13)
entry2355.grid(row=22, column=1, sticky=W)
entry2355.bind()
entry2355.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

def buttonclick2775():
	os.environ['int'] = entryint.get()
	os.environ['e2355'] = entry2355.get()
	if (i1.get() ==2):
		os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 9 -hold -e sudo airodump-ng --bssid "$e2355" -w Bssid"$e2355" "$int" --manufacturer --uptime --wps' % wifimm)
	elif (i1.get() ==1):
		os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 9 -hold -e sudo airodump-ng --bssid "$e2355" -w Bssid"$e2355" "$int" --manufacturer --uptime --wps' % bt909ff)	
		
button1 = tk.Button(top111, text='Monitor Bssid', command=lambda: buttonclick2775(), width=11, height=1)
button1.grid(row=22, column=0, sticky=W)
button1.bind()

label1 = Label(bt99f, text='\nUse the "s" key over the\nterminal to sort\n\nCtrl+C over the terminal to STOP', fg='blue')
label1.grid(row=21, column=0)

#Deauthentication tab

topm3 = Frame(bta10f)
topm3.grid(row=1, column=0)

labelm22 = Label(topm3, text='\nDEAUTHENTICATION\n', fg='red')
labelm22.grid(row=2, column=0, sticky=W)

top3 = Frame(topm3)
top3.grid(row=8, column=0)

label21 = Label(top3, text='Bssid')
label21.grid(row=3, column=0, sticky=W)
entry21 = tk.Entry(top3, width=15)
entry21.grid(row=3, column=1, sticky=W)
entry21.bind()
entry21.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

label22 = Label(top3, text='Station')
label22.grid(row=4, column=0, sticky=W)
entry22 = tk.Entry(top3, width=15)
entry22.grid(row=4, column=1, sticky=W)
entry22.bind()
entry22.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

label23 = Label(top3, text='No: of Packets')
label23.grid(row=6, column=0, sticky=W)
entry23 = tk.Entry(top3, width=15)
entry23.grid(row=6, column=1, sticky=W)
entry23.bind()
entry23.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

top2 = Frame(bta10f)
top2.grid(row=2, column=0)

def buttonclick26():
	os.environ['int'] = entryint.get()
	os.environ['e21'] = entry21.get()
	os.environ['e22'] = entry21.get()
	os.environ['e23'] = entry21.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo aireplay-ng --deauth "$e23" -a "$e21" -c "$e22" "$int"' % bta101ff)		#test

button1 = tk.Button(top2, text='Deauth With Above Info', command=lambda: buttonclick26(), width=25, height=1)
button1.grid(row=21, column=0, sticky=W)
button1.bind()

top10 = Frame(bta10f)
top10.grid(row=12, column=0)

labelm23 = Label(top10, text='')
labelm23.grid(row=3, column=0, sticky=W)

entry233 = tk.Entry(top10, width=5)
entry233.grid(row=21, column=1, sticky=W)
entry233.bind()
entry233.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

def buttonclick27():
	os.environ['int'] = entryint.get()
	os.environ['e233'] = entry233.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo mdk3 "$int" d -c["$e233"]' % bbta101ff)

button1 = tk.Button(top10, text='Deauth Channel', command=lambda: buttonclick27(), width=19, height=1)
button1.grid(row=21, column=0, sticky=W)
button1.bind()

top10dd = Frame(bta10f)
top10dd.grid(row=13, column=0)

labelm23 = Label(top10dd, text='')
labelm23.grid(row=3, column=0, sticky=W)

def buttonclick28():
	os.environ['int'] = entryint.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo mdk3 "$int" d' % bta101ff)	

button1 = tk.Button(top10dd, text='DEAUTH EVERTHING', command=lambda: buttonclick28(), width=25, height=1)
button1.grid(row=23, column=0, sticky=W)
button1.bind()

labelm23 = Label(top10dd, text='')
labelm23.grid(row=24, column=0, sticky=W)

labelstop = Label(top10dd, text='Ctrl+C over the terminal to STOP', fg='red')
labelstop.grid(row=26, column=0)

top4 = Frame(tab2)
top4.grid(row=14, column=0)

#Sidebar 1

def buttonclickmous():
	os.popen("sudo mousepad")
            
button1 = tk.Button(top4, text='Launch Mousepad', command=lambda: buttonclickmous(), width=25, height=1)
button1.grid(row=2, column=0, sticky=W)
button1.bind()

#if zenmap installed
#def buttonclickzen():
#	os.popen('sudo zenmap')
#
#button1 = tk.Button(top4, text='Launch Zenmap', command=lambda: buttonclickzen(), width=10, height=1)
#button1.grid(row=3, column=0, sticky=NSEW)
#button1.bind()

def buttonclickwire():
	os.popen('sudo wireshark')

button1 = tk.Button(top4, text='Launch Wireshark', command=lambda: buttonclickwire(), width=10, height=1)
button1.grid(row=4, column=0, sticky=NSEW)
button1.bind()

def buttonclickkis():
	os.environ['int'] = entryint.get()
	os.popen('xterm -hold -e sudo kismet -c "$int"')

button1 = tk.Button(top4, text='Launch Kismet', command=lambda: buttonclickkis(), width=10, height=1)
button1.grid(row=6, column=0, sticky=NSEW)
button1.bind()

#if armitage installed
#def buttonclickarm():
#	os.environ['int'] = entryint.get()
#	os.popen('sudo armitage')

#button1 = tk.Button(top4, text='Launch Armitage', command=lambda: buttonclickarm(), width=10, height=1)
#button1.grid(row=7, column=0, sticky=NSEW)
#button1.bind()

top331 = Frame(tab2)
top331.grid(row=8, column=0)

topint3 = Frame(top331)
topint3.grid(row=0, column=0)

labelentr = Label(topint3, text='Enter Address Below', fg='blue' )
labelentr.grid(row=1, column=0)

entry301 = tk.Entry(topint3, width=27)
entry301.grid(row=21, column=0, sticky=NSEW)
entry301.bind()
entry301.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

def buttonclickt31():
	os.environ['e301'] = entry301.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo ping -c 7 "$e301"' % bta111)			

button1 = tk.Button(top331, text='Ping (7)', command=lambda: buttonclickt31(), width=25, height=1)
button1.grid(row=22, column=0, sticky=NSEW)
button1.bind()

def buttonclickt32():
	os.environ['e301'] = entry301.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo nmap -Pn "$e301"' % bta121)

button1 = tk.Button(top331, text='Nmap (lite)', command=lambda: buttonclickt32(), width=25, height=1)
button1.grid(row=25, column=0, sticky=NSEW)
button1.bind()

def buttonclickt33():
	os.environ['e301'] = entry301.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo nmap -T4 -A -v -Pn "$e301"' % bta121)

button1 = tk.Button(top331, text='Nmap (heavy)', command=lambda: buttonclickt33(), width=25, height=1)
button1.grid(row=26, column=0, sticky=NSEW)
button1.bind()

#Public and Local IP

topip = Frame(tab2)
topip.grid(row=70, column=0)

# Public IP
def buttonclicktrf():
	try:
		pip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
		pip1 = "Public IP: " + (pip)
		label2ip = tkinter.Label(topip, text=pip1, fg='green')
		label2ip.grid(row=102, column=1, sticky=W)

	except:
		pip1 = "Public IP: No Internet           "
		label2ip = tkinter.Label(topip, text=pip1, fg='green')
		label2ip.grid(row=102, column=1, sticky=W)

# Local IP   
def buttonclicktrf1():
	try:
		lip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		lip.connect(("10.255.255.255", 1))
		lip2 = "Local IP: " + lip.getsockname()[0]
		label4ip = tkinter.Label(topip, text=lip2, fg='green')
		label4ip.grid(row=103, column=1, sticky=W)

	except:
		lip2 = ('Local IP: No Connection    ')
		label4ip = tkinter.Label(topip, text=lip2, fg='green')
		label4ip.grid(row=103, column=1, sticky=W)

button1 = tk.Button(tab2, text='Get / Refresh IPs', command=lambda: [buttonclicktrf(),  buttonclicktrf1()], width=10, height=1)  
button1.grid(row=50, column=0, sticky=NSEW)
button1.bind()

#Sidebar 2 - no working

cred1 = Frame(tab3)
cred1.grid(row=0, column=0)
cred2 = Frame(tab3)
cred2.grid(row=1, column=0)
cred3 = Frame(tab3)
cred3.grid(row=2, column=0)

label1 = Label(cred1, text='\nThis feature is currently in development\nand not operational\n', fg='red')
label1.grid(row=0, column=0)

#label1 = Label(cred1, text='\nThe following buttons will gather\ninformation from different operating\nsystems and store it within the\nfolder name provided.\n', fg='blue')
#label1.grid(row=1, column=0)

#label1 = Label(cred1, text='\nThis feature requires TIDE\nto be running on the system\nyou are looking to get the\ninformation from.\n', fg='red')
#label1.grid(row=5, column=0)

#label1 = Label(cred2, text='\nPlease Enter Folder Name Below', fg='blue')
#label1.grid(row=1, column=0)

#entryfi = tk.Entry(cred2, width=20)
#entryfi.grid(row=2, column=0)
#entryfi.bind()
#entryfi.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
#os.environ['fic'] = entryfi.get()

#label1 = Label(cred2, text='\n')
#label1.grid(row=3, column=0)

#def buttonclickcwin():
#	os.environ['fic'] = entryfi.get()
	
#button1 = tk.Button(cred3, text='Windows Information', command=lambda: buttonclickcwin(), width=25, height=1)
#button1.grid(row=1, column=0, sticky=NSEW)
#button1.bind()

#def buttonclickcapp():
#	os.environ['fic'] = entryfi.get()
	
#button1 = tk.Button(cred3, text='Apple Information', command=lambda: buttonclickcapp(), width=25, height=1)
#button1.grid(row=3, column=0, sticky=NSEW)
#button1.bind()


#def buttonclickclin1():
#	os.environ['fic'] = entryfi.get()
	
#button1 = tk.Button(cred3, text='Linux Information', command=lambda: buttonclickclin1(), width=25, height=1)
#button1.grid(row=5, column=0, sticky=NSEW)
#button1.bind()

#WIFI HOTSPOT tab
#Main Screen

label1 = Label(mf8, text="\n")
label1.grid(row=2, column=0)

topmainab = Frame(mf8)
topmainab.grid(row=3, column=0)

#buttons
termmsabinfoa = Frame(topmainab)
termmsabinfoa.grid(row=1, column=2, sticky=NW)
#buttons
termmsabinfod = Frame(topmainab)
termmsabinfod.grid(row=1, column=3, sticky=NW)

#Blank
termmsabinfoc = Frame(topmainab)
termmsabinfoc.grid(row=1, column=1, sticky=NW)

label1 = Label(termmsabinfoc, text='                                    ')
label1.grid(row=7, column=0, sticky=E)

#inputs
termmsabinfob = Frame(topmainab)
termmsabinfob.grid(row=1, column=0, sticky=NW)

label1 = Label(termmsabinfob, text='Your Wireless Interface Name  ')
label1.grid(row=3, column=1, sticky=E)
entryint11 = tk.Entry(termmsabinfob, width=13)
entryint11.grid(row=3, column=2)
entryint11.bind()
entryint11.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
label1 = Label(termmsabinfob, text='Eg: wlan0, wlan1 ') #only working with wlan0
label1.grid(row=3, column=3, sticky=W)

label1 = Label(termmsabinfob, text='Name For The AP You Want To Broadcast  ')
label1.grid(row=5, column=1, sticky=E)
entryint33 = tk.Entry(termmsabinfob, width=13)
entryint33.grid(row=5, column=2)
entryint33.bind()
entryint33.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
label1 = Label(termmsabinfob, text='Eg: Guest, Free Wifi, Evil Twin')
label1.grid(row=5, column=3, sticky=W)

label1 = Label(termmsabinfob, text='The Channel For The AP To Broadcast On  ')
label1.grid(row=6, column=1, sticky=E)
entryint44 = tk.Entry(termmsabinfob, width=13)
entryint44.grid(row=6, column=2)
entryint44.bind()
entryint44.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
label1 = Label(termmsabinfob, text='Eg: 1, 6, 11')
label1.grid(row=6, column=3, sticky=W)

#password entry not added at this time due to wpa issues
label1 = Label(termmsabinfob, text='The Password For The AP  ')
label1.grid(row=7, column=1, sticky=E)
entryint55 = tk.Entry(termmsabinfob, width=13)
entryint55.grid(row=7, column=2)
entryint55.bind()
entryint55.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
label1 = Label(termmsabinfob, text='Eg: Guest123, Password')
label1.grid(row=7, column=3, sticky=W)

def buttonclickrogueup():
	os.environ['int11'] = entryint11.get()
	os.environ['int33'] = entryint33.get()
	os.environ['int44'] = entryint44.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo nmcli con add type wifi ifname "$int11" con-name "$int33" autoconnect yes ssid "$int33"' % termsabc)
	sleep(1)
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo nmcli con modify "$int33" 802-11-wireless.channel "$int44" 802-11-wireless.mode ap 802-11-wireless.band bg 				ipv4.method shared' % termsabc)
	sleep(1)
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo nmcli con up "$int33"' % termsabc)
	
button1 = tk.Button(termmsabinfoa, text='Start the Hotspot', command=lambda: buttonclickrogueup(), width=35, height=1, bg='Black', fg='white')
button1.grid(row=2, column=0, sticky=W)
button1.bind()

def buttonclickroguedown():
	os.environ['int11'] = entryint11.get()
	os.environ['int33'] = entryint33.get()
	os.environ['int44'] = entryint44.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo nmcli con down "$int33"' % termsabc)
	
button1 = tk.Button(termmsabinfoa, text='Stop the Hotspot', command=lambda: buttonclickroguedown(), width=35, height=1, bg='Black', fg='white')
button1.grid(row=3, column=0, sticky=W)
button1.bind()

def buttonclicknmclishow():
	os.environ['int11'] = entryint11.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo nmcli con show' % mbt202ffa)

button1 = tk.Button(termmsabinfoa, text='Show Connection', command=lambda: buttonclicknmclishow(), width=35, height=1, bg='Blue', fg='white')
button1.grid(row=4, column=0, sticky=W)
button1.bind()

def buttonclicknmclidel():
	os.environ['int11'] = entryint11.get()
	os.environ['int33'] = entryint33.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo nmcli con delete "$int33"' % mbt202ffa)

button1 = tk.Button(termmsabinfoa, text='Delete Connection', command=lambda: buttonclicknmclidel(), width=35, height=1, bg='Red', fg='black')
button1.grid(row=5, column=0, sticky=W)
button1.bind()

def buttonclickwire123():
	os.popen('sudo wireshark')

button1 = tk.Button(termmsabinfod, text='Launch Wireshark', command=lambda: buttonclickwire123(), width=35, height=1)
button1.grid(row=2, column=0, sticky=NSEW)
button1.bind()

def buttonclickurlsnarf():
	os.environ['int11'] = entryint11.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo urlsnarf -i "$int11"' % mbt202ffb)

button1 = tk.Button(termmsabinfod, text='Launch Urlsnarf', command=lambda: buttonclickurlsnarf(), width=35, height=1)
button1.grid(row=3, column=0, sticky=W)
button1.bind()

#def buttonclickdrift():
#	os.environ['int11'] = entryint11.get()
#	os.popen('sudo driftnet -i "$int11"')

#button1 = tk.Button(termmsabinfod, text='Launch Driftnet', command=lambda: buttonclickdrift(), width=35, height=1)
#button1.grid(row=4, column=0, sticky=NSEW)
#button1.bind()

def buttonclickblank():
	os.popen('')

button1 = tk.Button(termmsabinfod, text='', command=lambda: buttonclickdblank(), width=35, height=1)
button1.grid(row=5, column=0, sticky=NSEW)
button1.bind()

label1 = Label(termmsabinfob, text='\n\n\n\n\n\n\n')
label1.grid(row=8, column=0, sticky=E)

termmsab = Frame(mf8)
termmsab.grid(row=4, column=0)

mbtab = ttk.Notebook(mf8)
mbtab.grid(row=8, column=0, sticky='NESW')
mbt2ab = ttk.Frame(mbtab)
mbtab.add(mbt2ab, text=' Main Terminal ')
mbt8ab = ttk.Frame(mbtab)
mbtab.add(mbt8ab, text=' Hotspot Terminal ')
mbt10ab = ttk.Frame(mbtab)
mbtab.add(mbt10ab, text=' Show / Delete Connections ')
mbt11ab = ttk.Frame(mbtab)
mbtab.add(mbt11ab, text=' Urlsnarf ')

termmsbabc = Frame(mbt8ab, height=500, width=1600)
termmsbabc.grid(row=1, column=0)
termsabc = termmsbabc.winfo_id()

mbt22 = Frame(mbt2ab, height=500, width=1350)
mbt22.grid(row=1, column=3, sticky='NESW')
mbt222 = mbt22.winfo_id()

mbt22ff = Frame(mbt2ab, height=500, width=1600)
mbt22ff.grid(row=1, column=1, sticky='NESW')
mbt202ff = mbt22ff.winfo_id()

mbt22ffa = Frame(mbt10ab, height=500, width=1600)
mbt22ffa.grid(row=1, column=1, sticky='NESW')
mbt202ffa = mbt22ffa.winfo_id()

mbt22ffb = Frame(mbt11ab, height=500, width=1600)
mbt22ffb.grid(row=1, column=1, sticky='NESW')
mbt202ffb = mbt22ffb.winfo_id()

mbt22f = Frame(mbt2ab, height=500, width=1600)
mbt22f.grid(row=1, column=0, sticky='NESW')
mbt202f = mbt22f.winfo_id()

top1 = Frame(mbt22)
top1.grid(row=20, column=0)

topint = Frame(top1)
topint.grid(row=0, column=0)

label1 = Label(mbt22f, text='\nCLICK TERMINAL TO START', fg='blue')
label1.grid(row=1, column=0)

label1 = Label(mbt22f, text='')
label1.grid(row=2, column=0)

def buttonclick1m():
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 ' % mbt202ff)
            
button1 = tk.Button(mbt22f, text='Terminal', command=lambda: buttonclick1m(), width=25, height=1)
button1.grid(row=4, column=0, sticky=W)
button1.bind()

def buttonclick5m():
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e ifconfig' % mbt202ff)
    
button1 = tk.Button(mbt22f, text='Ifconfig', command=lambda: buttonclick5m(), width=25, height=1)
button1.grid(row=7, column=0, sticky=W)
button1.bind()

def buttonclick7m():
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e iwconfig' % mbt202ff)
    
button1 = tk.Button(mbt22f, text='Iwconfig', command=lambda: buttonclick7m(), width=25, height=1)
button1.grid(row=9, column=0, sticky=W)
button1.bind()

def buttonclicka30m():
    os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo service NetworkManager stop' % mbt202ff)

button1 = tk.Button(mbt22f, text='Network Manager Stop', command=lambda: buttonclicka30m(), width=25, height=1)
button1.grid(row=11, column=0, sticky=W)
button1.bind()

def buttonclicka31m():
    os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo service NetworkManager start' % mbt202ff)

button1 = tk.Button(mbt22f, text='Network Manager Start', command=lambda: buttonclicka31m(), width=25, height=1)
button1.grid(row=13, column=0, sticky=W)
button1.bind()

def buttonclicka32m():
    os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo service NetworkManager restart' % mbt202ff)

button1 = tk.Button(mbt22f, text='Network Manager Restart', command=lambda: buttonclicka32m(), width=25, height=1)
button1.grid(row=15, column=0, sticky=W)
button1.bind()

#Internet Tools Framework
#Main Screen
btopmain = Frame(mf3)
btopmain.grid(row=0, column=0)

#Left Framework
btopmainl = Frame(btopmain)
btopmainl.grid(row=1, column=0, sticky='NESW')

btermt = Frame(btopmainl, height=180, width=1350)
btermt.grid(row=1, column=0, sticky='NESW')
btert = btermt.winfo_id()

btermtb = Frame(btopmainl, height=500, width=1350)
btermtb.grid(row=2, column=0, sticky='NESW')
btertb = btermtb.winfo_id()

#Bottom Tabs Framework
bbt = ttk.Notebook(btermtb)
bbt.grid(row=1, column=0, sticky='NESW')
bbt1 = ttk.Frame(bbt)
bbt.add(bbt1, text='Terminal')
bbt2 = ttk.Frame(bbt)
bbt.add(bbt2, text='Ping')
bbt3 = ttk.Frame(bbt)
bbt.add(bbt3, text='Whois')
bbt4 = ttk.Frame(bbt)
bbt.add(bbt4, text='Traceroute')
bbt5 = ttk.Frame(bbt)
bbt.add(bbt5, text='Nmap Lite Scan')
bbt6 = ttk.Frame(bbt)
bbt.add(bbt6, text='Nmap Heavy Scan')
bbt7 = ttk.Frame(bbt)
bbt.add(bbt7, text='Harvester')
bbt8 = ttk.Frame(bbt)
bbt.add(bbt8, text='Clone Page')

#Terminal tab
bbt11 = Frame(bbt1, height=500, width=1350)
bbt11.grid(row=1, column=0, sticky='NESW')
bbt111 = bbt11.winfo_id()

#Ping tab
bbt22 = Frame(bbt2, height=500, width=1350)
bbt22.grid(row=1, column=0, sticky='NESW')
bbt222 = bbt22.winfo_id()

#Whois tab
bbt33 = Frame(bbt3, height=500, width=1350)
bbt33.grid(row=1, column=0, sticky='NESW')
bbt333 = bbt33.winfo_id()

#Traceroute tab
bbt44 = Frame(bbt4, height=500, width=1350)
bbt44.grid(row=1, column=0, sticky='NESW')
bbt444 = bbt44.winfo_id()

#Nmap Lite Scan tab
bbt55 = Frame(bbt5, height=500, width=1350)
bbt55.grid(row=1, column=0, sticky='NESW')
bbt555 = bbt55.winfo_id()

#Nmap Heavy Scan tab
bbt66 = Frame(bbt6, height=500, width=1350)
bbt66.grid(row=1, column=0, sticky='NESW')
bbt666 = bbt66.winfo_id()

#Harvester tab
bbt77 = Frame(bbt7, height=500, width=1350)
bbt77.grid(row=1, column=0, sticky='NESW')
bbt777 = bbt77.winfo_id()

#Clone tab
bbt88 = Frame(bbt8, height=500, width=1350)
bbt88.grid(row=1, column=0, sticky='NESW')
bbt888 = bbt88.winfo_id()

#Right Framework
bnb = ttk.Notebook(btopmain)
bnb.grid(row=1, column=2, sticky='NESW')
btab2 = ttk.Frame(bnb)
bnb.add(btab2, text='Main Tools')
#btab3 = ttk.Frame(bnb)
#bnb.add(btab3, text='Internet Tools 2')

#Internet Tools - Notepad

label1 = Label(btermt, text="NOTES")
label1.grid(row=1, column=0)

def save_command():
    file = filedialog.asksaveasfile(parent=root, mode='w', title='Save File', defaultextension=".txt")
    if file is not None:
        data = textPad.get('1.0', END)
        file.write(data)
        file.close()

note1 = Frame(btermt)
note1.grid(row=2, column=0)
textPad = ScrolledText(note1, width=165, height=10)
textPad.grid()
textPad.bind()
textPad.bind_class("ScrolledText", "<Button-3><ButtonRelease-3>", show_menu)  # Not working
note2 = Frame(btermt)
note2.grid(row=3, column=0)
save1 = Button(note2, text="Save", command=save_command)
save1.config(width=20)
save1.grid()

#Internet Tools - Buttons and Functions

top12 = Frame(btab2)
top12.grid(row=1, column=0)

def buttonclick1t2():
    os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10' % bbt111) 
            
button1 = tk.Button(top12, text='Launch Terminal in Tab', command=lambda: buttonclick1t2(), width=25, height=1)
button1.grid(row=1, column=0, sticky=W)
button1.bind()

entry101 = tk.Entry(top12, width=27)
entry101.grid(row=21, column=0, sticky=NSEW)
entry101.bind()
entry101.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

label1 = Label(top12, text='Please enter details in bar below', fg='blue')
label1.grid(row=3, column=0, sticky=NSEW)

top122 = Frame(btab2)
top122.grid(row=2, column=0)

def buttonclick101():
    webbrowser.open('https://google.com/search?q=' + entry101.get())

button1 = tk.Button(top122, text='Google', command=lambda: buttonclick101(), width=12, height=1)
button1.grid(row=22, column=0, sticky=NSEW)
button1.bind()

def buttonclick10111():
	os.environ['e101'] = entry101.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo ping -c 7 "$e101"' % bbt222)

button1 = tk.Button(top122, text='Ping (7)', command=lambda: buttonclick10111(), width=12, height=1)
button1.grid(row=22, column=1, sticky=NSEW)
button1.bind()

def buttonclick1012():
	os.environ['e101'] = entry101.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo whois "$e101"' % bbt333)

button1 = tk.Button(top122, text='Whois', command=lambda: buttonclick1012(), width=12, height=1)
button1.grid(row=23, column=0, sticky=NSEW)
button1.bind()

def buttonclick1013():
	os.environ['e101'] = entry101.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo traceroute "$e101"' % bbt444)

button1 = tk.Button(top122, text='Traceroute', command=lambda: buttonclick1013(), width=12, height=1)
button1.grid(row=23, column=1, sticky=NSEW)
button1.bind()

def buttonclick10144():
	os.environ['e101'] = entry101.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo nmap -Pn "$e101"' % bbt555)

button1 = tk.Button(top122, text='Nmap (lite)', command=lambda: buttonclick10144(), width=12, height=1)
button1.grid(row=25, column=0, sticky=NSEW)
button1.bind()

def buttonclick101444():
	os.environ['e101'] = entry101.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo nmap -T4 -A -v -Pn "$e101"' % bbt666)

button1 = tk.Button(top122, text='Nmap (heavy)', command=lambda: buttonclick101444(), width=12, height=1)
button1.grid(row=25, column=1, sticky=NSEW)
button1.bind()

def buttonclick1014():
	os.environ['e101'] = entry101.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo theHarvester -d "$e101"' % bbt777)

button1 = tk.Button(top122, text='Harvester', command=lambda: buttonclick1014(), width=12, height=1)
button1.grid(row=26, column=0, sticky=NSEW)
button1.bind()

def buttonclick101445():
	os.environ['e101'] = entry101.get()
	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo wget "$e101"' % bbt888)  #maybe wget

button1 = tk.Button(top122, text='Clone', command=lambda: buttonclick101445(), width=12, height=1)
button1.grid(row=26, column=1, sticky=NSEW)
button1.bind()

top11a = Frame(btab2)
top11a.grid(row=5, column=0)

label1 = Label(top11a, text='\nThe below is Google search options.\nPlease fill in the required and\nclick the button.\nThis will open your browser.\n', fg='blue')
label1.grid(row=15, column=0, sticky=NSEW)

top11 = Frame(btab2)
top11.grid(row=7, column=0)

lines = []
applabels = []
appinputs = []
buttons = []

lines.append(["Index Of :", "index.of. :"])
lines.append(["File Type :", "filetype :"])
lines.append(["Site :", "site :"])
lines.append(["In Url :", "inurl :"])
lines.append(["In Text :", "intext :"])
lines.append(["In Title :", "intitle :"])
lines.append(["All In Url :", "allinurl :"])
lines.append(["All In Text :", "allintext :"])
lines.append(["All In Title :", "allintitle :"])

for entry in range(len(lines)):
    applabels.append(Label(top11, text=lines[entry][0]))
    applabels[-1].grid(row=entry, column=0, sticky=W)
    appinputs.append(tk.Entry(top11, width=16))
    appinputs[-1].grid(row=entry, column=1)
    appinputs[-1].bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

def buttonclick():
    searchstring = ""
    for entry in range(len(lines)):
        if (appinputs[entry].get() == "") is False:
            searchstring += lines[entry][1] + appinputs[entry].get() + " "

    if (searchstring == "") is True:
        webbrowser.open("http://google.com")
    else:
        sleep(1), webbrowser.open("https://google.com/search?q=" + searchstring)

for entry in range(len(lines)):
    appinputs[entry].bind(lambda x: buttonclick())

dtbutton = Button(top11, text="Google Search", command=lambda: buttonclick(), width=13, height=1)
dtbutton.grid(row=len(lines), column=1, sticky=NSEW)

top11ab = Frame(btab2)
top11ab.grid(row=19, column=0)

label1 = Label(top11ab, text='\nThe below is a person search.\nPlease fill in the required and\nclick the button.\nThis will open your browser.\n', fg='blue')
label1.grid(row=15, column=0, sticky=NSEW)

top1111 = Frame(btab2)
top1111.grid(row=20, column=0)

label1 = Label(top1111, text="First Name :")
label1.grid(row=16, column=0, sticky=W)
entry20p = tk.Entry(top1111, width=15)
entry20p.grid(row=16, column=1, sticky=W)
entry20p.bind()
entry20p.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

label1 = Label(top1111, text="Second Name :")
label1.grid(row=17, column=0, sticky=W)
entry21p = tk.Entry(top1111, width=15)
entry21p.grid(row=17, column=1, sticky=W)
entry21p.bind()
entry21p.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

label1 = Label(top1111, text="Last Name :")
label1.grid(row=18, column=0, sticky=W)
entry22p = tk.Entry(top1111, width=15)
entry22p.grid(row=18, column=1, sticky=W)
entry22p.bind()
entry22p.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

label1 = Label(top1111, text="Location :")
label1.grid(row=19, column=0, sticky=W)
entry23p = tk.Entry(top1111, width=15)
entry23p.grid(row=19, column=1, sticky=W)
entry23p.bind()
entry23p.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

def buttonClickp11(target):
	sleep(1), webbrowser.open('https://google.com/search?q=' + entry20p.get() + '+' + entry21p.get() + '+'
                              + entry22p.get() + '+' + entry23p.get())
	sleep(1), webbrowser.open('https://www.facebook.com/search/top?q=' + entry20p.get() + '-' + entry21p.get() + '-'
                              + entry22p.get())
	sleep(1), webbrowser.open('https://pipl.com/search/?q=' + entry20p.get() + '+' + entry21p.get() + '+'
                              + entry22p.get() + '&l=' + entry23p.get())
	sleep(1), webbrowser.open('https://www.linkedin.com/pub/dir/' + entry20p.get() + '/' + entry22p.get())
	sleep(1), webbrowser.open('https://www.peekyou.com/' + entry20p.get() + '_' + entry22p.get())

buttons.append(Button(top1111, text='Person Search', command=lambda entry=entry: buttonClickp11(entry), width=11, height=1))
buttons[-1].grid(row=20, column=1, sticky=NSEW)

# Hashing Tools
# Hashing Tools Framework 
#hash1 = Frame(mf5)
#hash1.grid(row=0, column=0)
#
#hash2 = Frame(mf5)
#hash2.grid(row=1, column=0)

#hashm = Frame(hash2, height=520, width=800)
#hashm.grid(row=3, column=0, sticky=W)
#hashmm = hashm.winfo_id()

#hashml = Frame(hash2, height=520, width=800)
#hashml.grid(row=3, column=1)
#hashmll = hashm.winfo_id()

#Hashing Tools - Right Side Panel Text 
#label1 = Label(hash1, text='\nHASHING TOOLS\n', fg='blue')
#label1.grid(row=1, column=0, sticky=W)

#label1 = Label(hashml, text='\nJTR USAGE & Mask Options\n', fg='green')
#label1.grid(row=0, column=0, sticky=W)

#label1 = Label(hashml, text="Use '0' in 'Progress in Seconds' to not show Progress. Use 'q' or 'Ctrl-c' over the Terminal to Stop Scan.\n\n?l lower-case ASCII letters\n ?u upper-case ASCII letters\n?d digits\n?s specials (all printable ASCII characters not in ?l, ?u or ?d)\n?a full 'printable' ASCII.\n?B all 8-bit (0x80-0xff)\n?b all (0x01-0xff).\n?h lower-case HEX digits (0-9, a-f)\n?H upper-case HEX digits (0-9, A-F)\n?L lower-case non-ASCII letters\n?U upper-case non-ASCII letters\n?D non-ASCII digits\n?S non-ASCII specials\n?A all valid characters (including ASCII).\n?1 .. ?9 user-defined place-holder 1 .. 9 Placeholders for Hybrid Mask mode:\n?w is a placeholder for the original word produced by the parent mode in Hybrid Mask mode.\n?W is just like ?w except the original word is case toggled (so PassWord becomes pASSwORD).")
#label1.grid(row=1, column=0, sticky=W)

# Hashing Tools - Buttons and Functions
#label1 = Label(hash1, text="File Name:")
#label1.grid(row=3, column=0, sticky=W)
#entryhash1 = tk.Entry(hash1, width=25)
#entryhash1.grid(row=3, column=1, sticky=W)
#entryhash1.bind()
#entryhash1.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

#def buttonclickhash1():
#	os.environ['hname'] = entryhash1.get()
#	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e wpapcap2john "$hname".pcap' % hashmm)
	
#button1 = tk.Button(hash1, text='Test Hash Capture', command=lambda: buttonclickhash1(), width=25, height=1)
#button1.grid(row=3, column=2, sticky=W)
#button1.bind()

#def buttonclickhash2():
#	os.environ['hname'] = entryhash1.get()
#	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e aircrack-ng "$hname".pcap -J "$hname"hash' % hashmm)
#	sleep(3)
#	os.popen('xterm -e hccap2john "$hname"hash.hccap > "$hname"hash')  # resolve issue not writing info to file for JTR

#button1 = tk.Button(hash1, text='Convert File for Hashcat & JTR', command=lambda: buttonclickhash2(), width=25, height=1)
#button1.grid(row=3, column=3, sticky=W)
#button1.bind()

#label1 = Label(hash1, text="JTR Progress in Seconds: ")
#label1.grid(row=4, column=0, sticky=W)
#entryhash111 = tk.Entry(hash1, width=25)
#entryhash111.grid(row=4, column=1, sticky=W)
#entryhash111.bind()
#entryhash111.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

#label1 = Label(hash1, text="JTR Mask:")
#label1.grid(row=5, column=0, sticky=W)
#entryhash11 = tk.Entry(hash1, width=25)
#entryhash11.grid(row=5, column=1, sticky=W)
#entryhash11.bind()
#entryhash11.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

#def buttonclickjohn0():
#	os.environ['mask1'] = entryhash11.get()
#	os.environ['hname'] = entryhash1.get()
#	os.environ['prog'] = entryhash111.get()
#	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e john --mask="$mask1" "$hname"hash --progress="$prog"' % hashmm)
            
#button1 = tk.Button(hash1, text='JTR with provided mask', command=lambda: buttonclickjohn0(), width=25, height=1)
#button1.grid(row=4, column=2, sticky=W)
#button1.bind()

#def buttonclickjohn1():
#	os.environ['hname'] = entryhash1.get()
#	os.environ['prog'] = entryhash111.get()
#	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e john "$hname"hash --progress="$prog"' % hashmm)
            
#button1 = tk.Button(hash1, text='JTR Full Scan', command=lambda: buttonclickjohn1(), width=25, height=1)
#button1.grid(row=4, column=3, sticky=W)
#button1.bind()

#def buttonclickjohn2():
#	os.environ['hname'] = entryhash1.get()
#	os.environ['prog'] = entryhash111.get()
#	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e john --single "$hname"hash --progress="$prog"' % hashmm)
            
#button1 = tk.Button(hash1, text='JTR Single Scan', command=lambda: buttonclickjohn2(), width=25, height=1)
#button1.grid(row=5, column=2, sticky=W)
#button1.bind()

#def buttonclickjohn3():
#	os.environ['hname'] = entryhash1.get()
#	os.environ['prog'] = entryhash111.get()
#	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e john --wordlist=wordlist.txt "$hname"hash --progress="$prog" --format=wpapsk-pmk' % hashmm)
            
#button1 = tk.Button(hash1, text='JTR Wordlist Scan', command=lambda: buttonclickjohn3(), width=25, height=1)
#button1.grid(row=5, column=3, sticky=W)
#button1.bind()

#label11 = Label(hash1, text="")
#label11.grid(row=7, column=0, sticky=W)

#Exploit Framework Tab
#Main Screen
#topmainmsf = Frame(mf11)
#topmainmsf.grid(row=0, column=0)

#label1 = Label(topmainmsf, text="\nEXPLOIT FRAMEWORK\n\n", fg='green', font='25')
#label1.grid(row=2, column=0)

#termmsfb = Frame(topmainmsf)
#termmsfb.grid(row=7, column=0)

#mbt = ttk.Notebook(topmainmsf)
#mbt.grid(row=8, column=0, sticky='NESW')
#mbt2 = ttk.Frame(mbt)
#mbt.add(mbt2, text='Metasploit Framework')
#mbt6 = ttk.Frame(mbt)
#mbt.add(mbt6, text='Metasploit Venom')
#mbt6s = ttk.Frame(mbt)
#mbt.add(mbt6s, text='S.E.T.')
#mbt6ss = ttk.Frame(mbt)
#mbt.add(mbt6ss, text='Searchsploit')

#termmsf = Frame(mbt2, height=560, width=1600)
#termmsf.grid(row=1, column=0)
#termsf = termmsf.winfo_id()

#termmsfv = Frame(mbt6, height=560, width=1600)
#termmsfv.grid(row=1, column=0)
#termsfv = termmsfv.winfo_id()

#termmsfvss = Frame(mbt6ss, height=560, width=1600)
#termmsfvss.grid(row=1, column=0)
#termsfvss = termmsfvss.winfo_id()

#termmsfv1 = Frame(mbt6s, height=560, width=1600)
#termmsfv1.grid(row=1, column=0)
#termsfv1 = termmsfv1.winfo_id()

#def buttonclickmc():
#	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo msfconsole' % termsf)			#java issue

#button1 = tk.Button(termmsfb, text='Start Metasploit Framework', command=lambda: buttonclickmc(), width=25, height=1)
#button1.grid(row=1, column=0)
#button1.bind()

#def buttonclickmsfv():
#	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo msfvenom -h' % termsfv)			#not returning to terminal

#button1 = tk.Button(termmsfb, text='Start Metasploit Venom', command=lambda: buttonclickmsfv(), width=25, height=1)
#button1.grid(row=1, column=1)
#button1.bind()

#def buttonclickmsfs():
#	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo setoolkit' % termsfv1)

#button1 = tk.Button(termmsfb, text='Start Social Engineer Toolkit', command=lambda: buttonclickmsfs(), width=25, height=1)
#button1.grid(row=1, column=2)
#button1.bind()

#def buttonclickmsfsss():
#	os.popen('xterm -into %d -geometry 200x300 -fa "Monospace" -fs 10 -hold -e sudo searchsploit' % termsfvss)		#fix load , add entry
#
#button1 = tk.Button(termmsfb, text='Start Searchspliot', command=lambda: buttonclickmsfsss(), width=25, height=1)
#button1.grid(row=3, column=0)
#button1.bind()

#def buttonclickarm():
#	os.popen('armitage')
#
#button1 = tk.Button(termmsfb, text='Launch Armitage', command=lambda: buttonclickarm(), width=25, height=1)
#button1.grid(row=3, column=1)
#button1.bind()

root.mainloop()
