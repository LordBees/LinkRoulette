##http://bit.do/list-of-url-shorteners.php
##http://www.hongkiat.com/blog/url-shortening-services-the-ultimate-list/
import random,webbrowser,os
from tkinter import *
from tkinter import messagebox
FILE_HISTORY = 'history.dat'
vchars = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
history = []
#settings in order Warn_Skiplink , History_Track
settings = []
#Menu_settings_window_DATA = []##global datastore for settings window maynot need as objectified
root = Tk()
linktype_Radio = IntVar()
linktype_Random = IntVar()
gennedlink = StringVar()
def openrng():##button funct
    global gennedlink
    global settings
    print('link = ',gennedlink.get())
    #0 = prompt
    print(settings[0])
    if int(settings[0]) == 1:##functionise instead?
        print('no prompt')
        webbrowser.open(gennedlink.get())
        
    else:
        if messagebox.askokcancel(title = 'confirm open',message = 'are you sure\nthere is NO guaruntee the link will be safe!'):
            webbrowser.open(gennedlink.get())
        
    
def googlehome():##button funct
    webbrowser.open('google.co.uk')

    
def save_file(name,data,overwrite = False,array = False):#saving funct
    if overwrite:
        f = open(name,'r+')
    else:
        f = open(name,'w')
    if array:
        for x in data:
            f.write(x+'\n')
    else:
        for x in data:
            f.write(x)
    f.close()


def loadfile(name):##loading funct
    contents = []
    f = open(name,'r')
    for x in f.readlines():
        contents.append(x.strip('\n'))
    f.close()
    return contents

def array2csv(array):##from beelib
        temp = ''
        for fl in array:
            print(fl)
            temp += str(fl)+','
        temp+=','
        return temp
    
def csv2array(csvstr):##may need os.isfile() or whatever it is to check file is in dir before declaring eofsame for array2csv      ##from beelib
    arrayreturn = []
    temp = ''
    flag = False
    for x in csvstr:#range(len(csvnames)):
        if flag and (x==','):## ,, delimiter
            break
        if x ==',':
            arrayreturn.append(temp)
            temp = ''
            flag = True
        else:
            temp+=x
            flag = False
    return arrayreturn

def load_history_ext():##unused
    global history
    if askokcancel():
        history = loadfile(FILE_HISTORY)

def load_history():
    global history
    if FILE_HISTORY in os.listdir():
        history = loadfile(FILE_HISTORY)
    else:
        save_file(FILE_HISTORY,['the history file'])

    
def save_history():
    global history
    save_file(FILE_HISTORY,history,array = True)

def refresh_Hbox():##refreshes listbox to update it
    history_Listbox.delete(0,history_Listbox.size())
    for x in history:
        history_Listbox.insert(END,x)

        
def clearhistory():##temp clears urlbox
    if messagebox.askokcancel(title = 'confirm clear',message = 'delete your history?'):
        save_file(FILE_HISTORY,['the history file'],overwrite = False)
        history_Listbox.delete(0,history_Listbox.size())
        refresh_Hbox()
        print('cleared')
    else:
        print('no')
    
def loadsettings():
    global settings
    print('loading settings...')
    if 'SETTINGS.CFF' in os.listdir():##my add as a function instead(exists checker)
        f = open('SETTINGS.CFF','r+')
        data = csv2array(f.readline())
        f.close()
        #print(data)
        settings = data
        print ('loaded: ',data)
        

def genlink():##button funct
    global settings
    if linktype_Random.get() == 1:
        linktype_Radio.set(random.randint(1,3))##randomises the link(change values to allow for all radios(UPDATE)
        ##genlink()
        
    if linktype_Radio.get() == 0:
        pass

    else:
        ##if linktype_Radio.get() == -1:
            ##linktype_Radio.set(random.randint(1,3))##randomises the link(change values to allow for all radios(UPDATE)
            ##genlink()
        if linktype_Radio.get()   ==  1:
            gennedlink.set(get_tinyurl())##eg http://tinyurl.com/DlJzJ
        elif linktype_Radio.get() ==  2:
            gennedlink.set(get_BitLy())
        elif linktype_Radio.get() ==  3:
            gennedlink.set(get_googl())
        if int(settings[1]) == 1:##skips saving link to array and disk
            print('skipped saving history')
        else:
            history.append(gennedlink.get())
            save_history()
        linkbox_Label.config(text = str(gennedlink.get()))
        refresh_Hbox()

        
def setlink():
    global history_listbox
    if history_Listbox.curselection() == None:##checks if valid
        pass
    else:
        gennedlink.set(history_Listbox.get(history_Listbox.curselection()))
        linkbox_Label.config(text = str(gennedlink.get()))


def get_tinyurl():   
    link = ''
    leng = random.randint(4,6)#4-6 chars
    for x in range(0,leng):
        link+=vchars[random.randint(0,len(vchars))]
    return 'http://tinyurl.com/'+link


def get_BitLy():
    link = ''
    leng = random.randint(4,6)#4-6 chars
    for x in range(0,leng):##can be longer as https://bit.ly/zzzzzzzzzzzzzzzzz is valid
        link+=vchars[random.randint(0,len(vchars))]
    return 'http://bit.ly/'+link


def get_googl():
    link = ''
    leng = random.randint(4,6)#4-6 chars
    for x in range(0,leng):
        link+=vchars[random.randint(0,len(vchars))]
    return 'http://goo.gl/'+link
    
def on_run():##bootup setup
    load_history()
    refresh_Hbox()
    loadsettings()

    
def on_close():##cleanup on close
    #save_history()##better to save direct
    print('cleanup')
    
    
def asciidump_ext():
	chrs = []
	for x in range(0,255):
		chrs.append(str(chr(x)))
	return chrs


#def genrandom():#save_file(name,data,overwrite = False,array = False)
#    pass ##implemented in class

##def Menu_settings_window():
##    global root
##    #global Menu_settings_window_DATA
##    Warn_Skiplink = IntVar()
##    
##    optionsmenu = Toplevel()
##    OCL = LabelFrame(optionsmenu,text = 'toggle options')##options_Checkboxes_labelframe
##    OBL = LabelFrame(optionsmenu,text = 'buttons')##options_buttons_labelframe
##    
##    SKIPWARN_check = Checkbutton(OCL,text = 'skip openbox on link open',variable = Warn_Skiplink,onvalue = 1,offvalue =0)
##    KEEPHISTORY_checks = Checkbutton(OCL,text = 'keep history',variable = Warn_Skiplink,onvalue = 1,offvalue =0)
##
##    OCL.pack()
##    OBL.pack()
##
##    SKIPWARN_check.pack()
##    KEEPHISTORY_checks.pack()
##
##    #root.config()
##    optionsmenu.title('options')
##    optionsmenu.mainloop()
##
##def Menu_settings_savesettings():
##    #global Menu_settings_window_DATA

###subwindow classes#
class Menu_settings_window:
    Warn_Skiplink = IntVar()##settings[0]
    History_Track = IntVar()##settings[1]
    SETTINGS_filename = 'SETTINGS.CFF'
    
    def __init__(self):

        self.Menu_settings_loadsettings()
        
        optionsmenu = Toplevel()
        OCL = LabelFrame(optionsmenu,text = 'toggle options')##options_Checkboxes_labelframe
        OBL = LabelFrame(optionsmenu,text = 'buttons')##options_buttons_labelframe
        
        SKIPWARN_check = Checkbutton(OCL,text = 'skip openbox on link open',variable = self.Warn_Skiplink,onvalue = 1,offvalue =0)
        KEEPHISTORY_checks = Checkbutton(OCL,text = "DON'T keep history",variable = self.History_Track,onvalue = 1,offvalue =0)

        SAVESETTINGS_button = Button(OBL,text = 'Save settings',command = self.Menu_settings_savesettings)##'may be able to put into eventloop a check for the changes
        WIPESETTINGS_button = Button(OBL,text = 'clear settings',command = self.Menu_settings_wipesettings)

        OCL.pack()
        OBL.pack()

        SKIPWARN_check.pack()
        KEEPHISTORY_checks.pack()

        SAVESETTINGS_button.pack()
        WIPESETTINGS_button.pack()
        
        #root.config()
        optionsmenu.title('options')
        optionsmenu.mainloop()
        
    def Menu_settings_loadsettings(self):
        if 'SETTINGS.CFF' in os.listdir():
            f  = open(self.SETTINGS_filename,'r+')
            data = self.csv2array(f.readline())
            print(data)
            f.close()
            self.Warn_Skiplink.set(data[0])
            self.History_Track.set(data[1])
            #print(data)

        else:
            print('file not found!')
            
        
    def Menu_settings_savesettings(self):##saves settings to SETTINGS.CFF
        #def save_file(name,data,overwrite = False,array = False):#saving funct
        data = self.array2csv(self.Menu_settings_getsettings())

        f = open(self.SETTINGS_filename,'w')
        f.write(data)
        #for x in data:
            #f.write(x+'\n')
        f.close()
        
    def Menu_settings_getsettings(self):##return settings data
        returner = [
        self.Warn_Skiplink.get(),
        self.History_Track.get()
        ]
        print(returner)
        return returner
    
    def Menu_settings_wipesettings(self):
    #def save_file(name,data,overwrite = False,array = False):#saving funct
        data = self.array2csv(([0]*len(settings)))

        f = open(self.SETTINGS_filename,'w')
        f.write(data)
        #for x in data:
            #f.write(x+'\n')
        f.close()
        self.Menu_settings_loadsettings()#reload settings to memory
        
    def array2csv(self,array):##from beelib
        temp = ''
        for fl in array:
            print(fl)
            temp += str(fl)+','
        temp+=','
        return temp
    
    def csv2array(self,csvstr):##may need os.isfile() or whatever it is to check file is in dir before declaring eofsame for array2csv      ##from beelib
        arrayreturn = []
        temp = ''
        flag = False
        for x in csvstr:#range(len(csvnames)):
            if flag and (x==','):## ,, delimiter
                break
            if x ==',':
                arrayreturn.append(temp)
                temp = ''
                flag = True
            else:
                temp+=x
                flag = False
        return arrayreturn
    ###



ol_LF = LabelFrame(root,text = 'open link')##openlink 
lr_LF = LabelFrame(root,text = 'pick a link type')##linkradio
hb_LF = LabelFrame(root,text = 'link history')##historybox
historyscroller_Scrollbar = Scrollbar(hb_LF)
history_Listbox = Listbox(hb_LF,yscrollcommand = historyscroller_Scrollbar.set)
historyscroller_Scrollbar.config(command = history_Listbox.yview)

tinyurl_radio = Radiobutton(lr_LF,text = 'tinyurl',variable = linktype_Radio,value = 1)
bitly_radio = Radiobutton(lr_LF,text = 'Bit.ly',variable = linktype_Radio,value = 2)
googl_radio = Radiobutton(lr_LF,text = 'goo.gl',variable = linktype_Radio,value = 3)
random_chkbox = Checkbutton(lr_LF,text = 'Random!',variable = linktype_Random,onvalue = 1,offvalue =0)
genlnk_Button = Button(ol_LF,command = genlink,text = 'generate\nlink')
openlnk_Button = Button(ol_LF,command = openrng,text = 'open link')
opengoogle_Button = Button(root,command = googlehome,text = 'google homepage')
selectlink_Button = Button(hb_LF,command = setlink,text = 'select link')
clearhistory_Button  = Button(root,command = clearhistory,text = 'clear history')
linkbox_Label = Label(root)


lr_LF.pack()
ol_LF.pack()
hb_LF.pack()

tinyurl_radio.pack()
bitly_radio.pack()
googl_radio.pack()
random_chkbox.pack()
genlnk_Button.pack()
openlnk_Button.pack()
opengoogle_Button.pack()
selectlink_Button.pack()
clearhistory_Button.pack()
linkbox_Label.pack()
history_Listbox.pack(side = LEFT)
historyscroller_Scrollbar.pack(side = RIGHT,fill = Y)


def event_TED():##custom event loop
    ##event code here##
    
    ##END EVENT CODE##
    root.after(2000, event_TED)


Menu_settings = Menu(root)
#Menu_settings = Menu(menubar, tearoff=0)
Menu_settings.add_command(label="options", command=Menu_settings_window)    
on_run()
root.config(menu=Menu_settings,)#title = 'Link Roulette'
root.title('Link Roulette')
root.geometry('300x300')
root.after(2000, event_TED)
root.mainloop()
on_close()

